#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MyApp.py
Features principali:
 - Menù interattivo robusto con print/input
 - Caricamento dati con default e retry (anche da directory dello script)
 - Esplorazione dati (head, info, describe)
 - Pulizia avanzata: duplicati, NaN, outlier IQR + opzionale KNN Imputer
 - Visualizzazioni: istogrammi, heatmap, scatter matrix
 - Preprocessing: one-hot encoding, scaling, PCA opzionale
 - Addestramento XGBoost + GridSearchCV per hyper-tuning
 - Valutazione: MSE, MAE, R2, MAPE, SMAPE, cross-validation
 - Consiglio prezzo e aggiunta di nuovi BnB
 - Salvataggio/Caricamento modello
 - Logging completo su file + console
"""

import os
import sys
import argparse
import logging
import warnings
from typing import Optional, List, Tuple

import numpy as np
import pandas as pd
import xgboost as xgb

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

import matplotlib.pyplot as plt
import seaborn as sns  # solo per heatmap

# ------------------------------------------------------------
# CONFIGURAZIONE LOGGING & WARNINGS
# ------------------------------------------------------------
LOG_FILE = "ml_app.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)

# ------------------------------------------------------------
# FUNZIONI DI INPUT VALIDATO
# ------------------------------------------------------------
def prompt_int(prompt: str, valid: Optional[List[int]] = None, default: Optional[int] = None) -> int:
    """
    Richiede un intero all'utente, con range opzionale e valore di default.
    """
    while True:
        s = input(f"{prompt}" + (f" [default: {default}]" if default is not None else "") + ": ").strip()
        if s == "" and default is not None:
            return default
        try:
            v = int(s)
            if valid is not None and v not in valid:
                print(f"Valore non valido. Scegli tra {valid}.")
                continue
            return v
        except ValueError:
            print("Inserisci un numero intero valido.")

def prompt_float(prompt: str, min_val: Optional[float] = None, default: Optional[float] = None) -> float:
    """
    Richiede un float all'utente, con valore minimo e default opzionale.
    """
    while True:
        s = input(f"{prompt}" + (f" [default: {default}]" if default is not None else "") + ": ").strip()
        if s == "" and default is not None:
            return default
        try:
            v = float(s)
            if min_val is not None and v < min_val:
                print(f"Deve essere >= {min_val}.")
                continue
            return v
        except ValueError:
            print("Inserisci un numero valido (es. 12.34).")

def prompt_choice(prompt: str, options: List[str], default: Optional[str] = None) -> str:
    """
    Richiede una stringa scelta da una lista di opzioni, con default opzionale.
    """
    opts = "/".join(options)
    while True:
        s = input(f"{prompt} ({opts})" + (f" [default: {default}]" if default else "") + ": ").strip()
        if s == "" and default is not None:
            return default
        if s in options:
            return s
        print(f"Scegli tra: {opts}")

# ------------------------------------------------------------
# CARICAMENTO & SALVATAGGIO DATI
# ------------------------------------------------------------
def load_data(path: Optional[str] = None) -> pd.DataFrame:
    """
    Carica un DataFrame da CSV, con percorso default e retry su errore.
    Se non trovato nella cwd, prova a cercarlo nella directory dello script.
    """
    default = "AB_NYC_2019.csv"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        user_input = input(f"Percorso file CSV [default: {default}]: ").strip()
        p = path or (user_input or default)

        # prova percorso così com'è
        if os.path.isfile(p):
            real_path = p
        else:
            alt = os.path.join(script_dir, p)
            if os.path.isfile(alt):
                real_path = alt
            else:
                print(f"File '{p}' non trovato. Riprova.")
                logger.error("File not found: %s (anche in %s)", p, script_dir)
                path = None
                continue

        # caricamento effettivo
        try:
            df = pd.read_csv(real_path)
            logger.info("Dataset caricato: %s (%d×%d)", real_path, df.shape[0], df.shape[1])
            print(f"Caricato {real_path} con {len(df)} righe e {len(df.columns)} colonne.")
            return df
        except Exception as e:
            print(f"Errore caricamento: {e}")
            logger.exception("Errore caricamento CSV")
            path = None

def save_model(model: xgb.XGBRegressor, filename: str = "xgb_model.json"):
    """
    Salva il modello XGBoost su disco.
    """
    try:
        model.save_model(filename)
        print(f"Modello salvato in {filename}.")
        logger.info("Model saved to %s", filename)
    except Exception as e:
        print(f"Errore salvataggio modello: {e}")
        logger.exception("Error saving model")

def load_model(filename: str = "xgb_model.json") -> xgb.XGBRegressor:
    """
    Carica un modello XGBoost da file.
    """
    if not os.path.isfile(filename):
        msg = f"Modello '{filename}' non trovato."
        print(msg)
        raise FileNotFoundError(msg)
    model = xgb.XGBRegressor()
    model.load_model(filename)
    print(f"Modello caricato da {filename}.")
    return model

# ------------------------------------------------------------
# ESPLORAZIONE DATI
# ------------------------------------------------------------
def explore_data(df: pd.DataFrame):
    """
    Stampa head, info e statistiche descrittive.
    """
    print("\n--- Head ---")
    print(df.head(5))
    print("\n--- Info ---")
    buf: List[str] = []
    df.info(buf=buf)
    for line in buf:
        print(line)
    print("\n--- Statistiche Descrittive ---")
    print(df.describe(include="all").T)

# ------------------------------------------------------------
# PULIZIA DATI AVANZATA
# ------------------------------------------------------------
def clean_data(df: pd.DataFrame, use_knn: bool = False, knn_k: int = 5) -> pd.DataFrame:
    """
    Rimuove duplicati, gestisce NaN, rimuove outlier via IQR, opzionale KNN imputer.
    """
    df_clean = df.copy()
    print("\n--- Pulizia Dati ---")
    # 1) Duplicati
    n0 = len(df_clean)
    df_clean.drop_duplicates(inplace=True)
    removed = n0 - len(df_clean)
    print(f"Duplicati rimossi: {removed}")
    logger.info("Removed %d duplicates", removed)
    # 2) Valori mancanti
    num_cols = df_clean.select_dtypes(include=[np.number]).columns
    cat_cols = df_clean.select_dtypes(include=["object", "category"]).columns
    for col in num_cols:
        m = df_clean[col].isna().sum()
        if m > 0:
            med = df_clean[col].median()
            df_clean[col].fillna(med, inplace=True)
            print(f"{m} NaN in {col} => mediana {med:.2f}")
            logger.info("Filled %d NaN in %s with median %f", m, col, med)
    for col in cat_cols:
        m = df_clean[col].isna().sum()
        if m > 0:
            mode = df_clean[col].mode().iloc[0]
            df_clean[col].fillna(mode, inplace=True)
            print(f"{m} NaN in {col} => moda {mode}")
            logger.info("Filled %d NaN in %s with mode %s", m, col, mode)
    # 3) Outlier IQR
    for col in num_cols:
        Q1, Q3 = df_clean[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        low, high = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        mask = df_clean[col].between(low, high)
        rem = (~mask).sum()
        if rem > 0:
            df_clean = df_clean[mask]
            print(f"Outlier in {col}: rimossi {rem} righe ({low:.2f}–{high:.2f})")
            logger.info("Removed %d outliers in %s", rem, col)
    # 4) KNN Imputer
    if use_knn and len(num_cols) > 0:
        print(f"KNN Imputer k={knn_k} in corso…")
        im = KNNImputer(n_neighbors=knn_k)
        df_clean[num_cols] = im.fit_transform(df_clean[num_cols])
        print("KNN Imputer applicato.")
        logger.info("Applied KNNImputer with k=%d", knn_k)
    df_clean.reset_index(drop=True, inplace=True)
    print("Pulizia completata.\n")
    return df_clean

# ------------------------------------------------------------
# VISUALIZZAZIONI
# ------------------------------------------------------------
def show_distributions(df: pd.DataFrame):
    """
    Mostra istogrammi delle colonne selezionate.
    """
    cols = input("Colonne (comma-separate) [default: price]: ").strip() or "price"
    cols = [c.strip() for c in cols.split(",") if c.strip() in df.columns]
    if not cols:
        print("Nessuna colonna valida.")
        return
    for c in cols:
        plt.figure()
        df[c].hist(bins=30)
        plt.title(f"Distribuzione di {c}")
        plt.xlabel(c)
        plt.ylabel("Frequenza")
        plt.tight_layout()
        plt.show()

def show_heatmap(df: pd.DataFrame):
    """
    Mostra la heatmap delle correlazioni delle variabili numeriche.
    """
    num = df.select_dtypes(include=[np.number])
    corr = num.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="viridis")
    plt.title("Heatmap Correlazioni")
    plt.tight_layout()
    plt.show()

def show_scatter_matrix(df: pd.DataFrame):
    """
    Mostra uno scatter matrix delle prime 5 variabili numeriche.
    """
    num = df.select_dtypes(include=[np.number]).iloc[:, :5]
    pd.plotting.scatter_matrix(num, alpha=0.5, figsize=(8, 8))
    plt.suptitle("Scatter Matrix (prime 5 variabili numeriche)")
    plt.show()

# ------------------------------------------------------------
# PIPELINE & TRAINING
# ------------------------------------------------------------
def build_pipeline(df: pd.DataFrame, use_pca: bool = False, n_comp: int = 5) -> Tuple[Pipeline, pd.DataFrame, pd.Series]:
    X = df.drop("price", axis=1)
    y = df["price"]
    steps = [
        ("ohe", OneHotEncoder(sparse=False, handle_unknown="ignore")),
        ("scaler", StandardScaler())
    ]
    if use_pca:
        steps.append(("pca", PCA(n_components=n_comp)))
        print(f"PCA attivata con {n_comp} componenti.")
        logger.info("PCA with %d components", n_comp)
    pipe = Pipeline([
        ("preproc", Pipeline(steps)),
        ("model", xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100, learning_rate=0.1, random_state=42))
    ])
    print("Pipeline pronta.")
    return pipe, X, y

def train_with_tuning(pipe: Pipeline, X_tr: pd.DataFrame, y_tr: pd.Series) -> Pipeline:
    params = {
        "model__n_estimators": [50, 100],
        "model__learning_rate": [0.05, 0.1],
        "model__max_depth": [3, 5]
    }
    grid = GridSearchCV(pipe, params, cv=3, scoring="neg_mean_squared_error", n_jobs=-1)
    print("GridSearch in corso…")
    grid.fit(X_tr, y_tr)
    print("Best params:", grid.best_params_)
    logger.info("GridSearch best params: %s", grid.best_params_)
    return grid.best_estimator_

# ------------------------------------------------------------
# VALUTAZIONE
# ------------------------------------------------------------
def evaluate_advanced(model: Pipeline, X_te: pd.DataFrame, y_te: pd.Series):
    preds = model.predict(X_te)
    mse = mean_squared_error(y_te, preds)
    mae = mean_absolute_error(y_te, preds)
    r2 = r2_score(y_te, preds)
    mape = np.mean(np.abs((y_te - preds) / y_te)) * 100
    smape = np.mean(2 * np.abs(y_te - preds) / (np.abs(y_te) + np.abs(preds))) * 100

    print(f"\nMSE   : {mse:.2f}")
    print(f"MAE   : {mae:.2f}")
    print(f"R2    : {r2:.4f}")
    print(f"MAPE% : {mape:.2f}")
    print(f"SMAPE%: {smape:.2f}")

    cv = cross_val_score(model, X_te, y_te, cv=3, scoring="neg_mean_squared_error", n_jobs=-1)
    rmse_cv = np.sqrt(-cv)
    print(f"CV RMSE: {rmse_cv.mean():.2f} ± {rmse_cv.std():.2f}")

    plt.figure()
    plt.scatter(y_te, preds, alpha=0.3)
    plt.plot([y_te.min(), y_te.max()], [y_te.min(), y_te.max()], "r--")
    plt.xlabel("True Price")
    plt.ylabel("Predicted Price")
    plt.title("True vs Predicted")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------------------
# CONSIGLIO & AGGIUNTA
# ------------------------------------------------------------
def recommend_and_add(df: pd.DataFrame):
    required = {"neighbourhood_group", "room_type", "price", "minimum_nights"}
    if not required.issubset(df.columns):
        print("Dati non compatibili per consiglio.")
        return
    zones = sorted(df["neighbourhood_group"].unique())
    types = sorted(df["room_type"].unique())
    z = prompt_choice("Zona", zones)
    t = prompt_choice("Tipologia", types)
    size = prompt_float("Metratura (mq)", min_val=1.0)
    sub = df[(df["neighbourhood_group"] == z) & (df["room_type"] == t)]
    if sub.empty:
        print("Nessun dato per questa combinazione.")
        return
    avgp = sub["price"].mean()
    avgs = sub.get("square_feet", pd.Series([50]*len(sub))).median()
    rec = (avgp / avgs) * size
    print(f"\nPrezzo medio: €{avgp:.2f}")
    print(f"Mq medio campione: {avgs:.1f}")
    print(f"Prezzo consigliato per {size:.1f} mq: €{rec:.2f}")
    if prompt_choice("Aggiungere al dataset?", ["y", "n"], default="n") == "y":
        new = {}
        for c in df.columns:
            if c == "price":
                continue
            if df[c].dtype.kind in "biufc":
                new[c] = sub[c].median()
            else:
                new[c] = sub[c].mode().iloc[0]
        new.update({
            "neighbourhood_group": z,
            "room_type": t,
            "price": round(rec, 2),
            "minimum_nights": int(sub["minimum_nights"].median())
        })
        df.loc[len(df)] = new
        print("Nuovo BnB aggiunto.")

# ------------------------------------------------------------
# MENÙ PRINCIPALE
# ------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="ML App mastodontica senza C++")
    parser.add_argument("--data", default=None, help="Percorso CSV")
    args = parser.parse_args()

    df = None
    df_clean = None
    pipe = None
    model = None
    X_tr = X_te = y_tr = y_te = None

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*40)
            print("   MY ML APP - CLI EDITION")
            print("="*40)
            print(" 1. Carica dati")
            print(" 2. Esplora dati")
            print(" 3. Pulisci dati")
            print(" 4. Mostra distribuzioni")
            print(" 5. Heatmap correlazioni")
            print(" 6. Scatter matrix")
            print(" 7. Preprocess & split")
            print(" 8. Train & tuning")
            print(" 9. Valuta modello")
            print("10. Consiglia/Add BnB")
            print("11. Salva/Carica modello")
            print("12. Esci")
            print("="*40)
            choice = prompt_int("Seleziona (1-12)", valid=list(range(1, 13)))
            if choice == 1:
                df = load_data(args.data)
                df_clean = None
            elif choice == 2:
                if df is None:
                    print("Carica prima i dati.")
                else:
                    explore_data(df_clean if df_clean is not None else df)
            elif choice == 3:
                if df is None:
                    print("Carica prima i dati.")
                else:
                    use_knn = prompt_choice("Usare KNN Imputer?", ["y", "n"], default="n") == "y"
                    k = prompt_int("k per KNN", default=5) if use_knn else 5
                    df_clean = clean_data(df, use_knn, k)
            elif choice == 4:
                if df is None:
                    print("Carica prima i dati.")
                else:
                    show_distributions(df_clean if df_clean is not None else df)
            elif choice == 5:
                if df is None:
                    print("Carica prima i dati.")
                else:
                    show_heatmap(df_clean if df_clean is not None else df)
            elif choice == 6:
                if df is None:
                    print("Carica prima i dati.")
                else:
                    show_scatter_matrix(df_clean if df_clean is not None else df)
            elif choice == 7:
                src = df_clean if df_clean is not None else df
                if src is None:
                    print("Carica prima i dati.")
                else:
                    up = prompt_choice("Usare PCA?", ["y", "n"], default="n") == "y"
                    nc = prompt_int("Componenti PCA", default=5) if up else 5
                    pipe, X, y = build_pipeline(src, up, nc)
                    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
            elif choice == 8:
                if pipe is None:
                    print("Crea pipeline prima.")
                else:
                    model = train_with_tuning(pipe, X_tr, y_tr)
            elif choice == 9:
                if model is None:
                    print("Allena modello prima.")
                else:
                    evaluate_advanced(model, X_te, y_te)
            elif choice == 10:
                if df is None:
                    print("Carica prima i dati.")
                else:
                    recommend_and_add(df_clean if df_clean is not None else df)
            elif choice == 11:
                act = prompt_choice("save/load", ["save", "load"], default="save")
                if act == "save":
                    if model:
                        save_model(model)
                    else:
                        print("Nessun modello da salvare.")
                else:
                    try:
                        model = load_model()
                    except FileNotFoundError:
                        pass
            else:
                print("Uscita.")
                break
            input("\nPremi INVIO per tornare al menu...")
    except KeyboardInterrupt:
        print("\nInterrotto dall'utente.")
        logger.info("Interrotto dall'utente")
    except Exception as e:
        print(f"Errore fatale: {e}")
        logger.exception("Fatal error in main")
        sys.exit(1)

if __name__ == "__main__":
    main()
