# main.py

import os
import argparse
import pandas as pd
import json

from data_cleaning import load_data, clean_data
from feature_engineering import add_features, scale_features
from model_training import (
    train_linear_regression,
    train_xgboost,
    evaluate_model,
    save_model
)
from visualizer import run_menu


def parse_args():
    parser = argparse.ArgumentParser(
        description="Pipeline interattiva: visualizza dati, scegli regressore, allena e stima prezzi"
    )
    parser.add_argument(
        "-i", "--input",
        type=str,
        default="kc_house_data.csv",
        help="Percorso al CSV di input"
    )
    return parser.parse_args()


def resolve_input_path(fpath: str) -> str:
    if not os.path.isfile(fpath):
        alt = os.path.join(os.path.dirname(__file__), fpath)
        if os.path.isfile(alt):
            return alt
    return fpath


def train_flow(df: pd.DataFrame):
    # 1) Prepara le feature
    df_clean = clean_data(df)
    df_feat  = add_features(df_clean)
    X, y     = scale_features(df_feat, target_column='price')

    # 2) Scegli l'algoritmo
    print("\nScegli il regressore:")
    print("  1) Linear Regression")
    print("  2) XGBoost Regressor")
    choice = input("Seleziona [1/2]: ").strip()

    if choice == '2':
        model, X_train, X_test, y_train, y_test = train_xgboost(X, y)
        algo_name = "XGBoost"
    else:
        model, X_train, X_test, y_train, y_test = train_linear_regression(X, y)
        algo_name = "Linear Regression"

    # 3) Valutazione
    metrics = evaluate_model(model, X_test, y_test)
    print(f"\n=== Risultati con {algo_name} ===")
    print(f"  R² score:   {metrics['r2']:.4f}")
    print(f"  MAE:        {metrics['mae']:.2f}")
    print(f"  RMSE:       {metrics['rmse']:.2f}")
    print(f"  Accuracy:   {metrics['r2']*100:.2f}%")

    # 4) Salva
    model_file = f"{algo_name.replace(' ', '_').lower()}_model.pkl"
    save_model(model, model_file)
    with open('metrics.json', 'w') as f:
        json.dump({'algorithm': algo_name, **metrics}, f, indent=4)
    pd.DataFrame({
        'actual_price': y_test,
        'predicted_price': model.predict(X_test)
    }).to_csv('predictions.csv', index=False)

    print(f"\nModello e risultati salvati: {model_file}, metrics.json, predictions.csv\n")


def main():
    args = parse_args()
    path = resolve_input_path(args.input)

    try:
        df = load_data(path)
    except Exception as e:
        print(f"Errore caricamento dati: {e}")
        return

    while True:
        print("\n*** MENU PRINCIPALE ***")
        print("1) Visualizza dati e grafici")
        print("2) Esegui training e valutazione")
        print("0) Esci")
        sel = input("Scelta: ").strip()

        if sel == '1':
            run_menu(path)
        elif sel == '2':
            train_flow(df)
        elif sel == '0':
            print("Uscita.")
            break
        else:
            print("Opzione non valida.")

if __name__ == '__main__':
    main()
