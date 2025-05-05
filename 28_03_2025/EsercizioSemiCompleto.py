import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline


def load_and_prepare():
    """
    Carica il dataset Wine e restituisce un DataFrame con feature e target,
    più un oggetto 'wine' di scikit-learn per metadati.
    """
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['target'] = wine.target
    df['target_name'] = df['target'].map({
        i: name for i, name in enumerate(wine.target_names)
    })
    print("Dataset caricato: {} campioni, {} feature".format(*wine.data.shape))
    return df, wine


def explore(df):
    """
    Esplora il dataset: distribuzione classi e statistiche descrittive.
    """
    print("\n--- Distribuzione delle classi ---")
    print(df['target_name'].value_counts(), "\n")
    print("--- Statistiche descrittive ---")
    print(df.drop(columns=['target', 'target_name']).describe().round(2), "\n")

    ax = df['target_name'] \
        .value_counts() \
        .plot.bar(title="Distribuzione delle classi")
    ax.set_xlabel("Classe")
    ax.set_ylabel("Numero di campioni")
    plt.tight_layout()
    plt.show()


def plot_pca(df):
    """
    Riduce le feature a 2 componenti principali e le visualizza.
    """
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=2))
    ])
    X = df.drop(columns=['target', 'target_name'])
    X_pca = pipeline.fit_transform(X)

    plt.figure(figsize=(6, 5))
    plt.scatter(
        X_pca[:, 0], X_pca[:, 1],
        c=df['target'], cmap='viridis',
        edgecolor='k', alpha=0.7
    )
    plt.title("PCA: 2 componenti principali")
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def train_and_evaluate(df):
    """
    Allena una RandomForest, stampa report e ritorna modello + dati di test.
    """
    X = df.drop(columns=['target', 'target_name'])
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("\n--- Classification Report ---")
    print(classification_report(
        y_test, y_pred,
        target_names=df['target_name'].unique()
    ))
    return clf, X_test, y_test, y_pred


def plot_feature_importances(model, feature_names):
    """
    Mostra le feature più importanti del modello RandomForest.
    """
    importances = model.feature_importances_
    idx_sorted = np.argsort(importances)[::-1]

    plt.figure(figsize=(7, 4))
    plt.bar(
        range(len(importances)),
        importances[idx_sorted],
        edgecolor='k'
    )
    plt.xticks(
        range(len(importances)),
        [feature_names[i] for i in idx_sorted],
        rotation=90
    )
    plt.title("Feature Importances (Random Forest)")
    plt.tight_layout()
    plt.show()


def plot_confusion(y_test, y_pred, labels):
    """
    Visualizza la matrice di confusione.
    """
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap='Blues')
    plt.title("Matrice di Confusione")
    plt.tight_layout()
    plt.show()


def optimize_model(df):
    """
    Esegue GridSearchCV su RandomForest per n_estimators e max_depth.
    """
    X = df.drop(columns=['target', 'target_name'])
    y = df['target']
    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [None, 5, 10]
    }
    grid = GridSearchCV(
        RandomForestClassifier(random_state=42),
        param_grid, cv=5, scoring='accuracy'
    )
    grid.fit(X_train, y_train)

    print("\n--- Ottimizzazione con GridSearchCV ---")
    print("Migliori parametri:", grid.best_params_)
    print("Best CV accuracy: {:.3f}".format(grid.best_score_))


def main():
    df, wine = load_and_prepare()
    model = None
    X_test = y_test = y_pred = None

    while True:
        print("\nMenù:")
        print("1. Carica e prepara il dataset")
        print("2. Esplora il dataset")
        print("3. Riduzione dimensionale con PCA")
        print("4. Allena e valuta il modello")
        print("5. Visualizza importanza delle feature")
        print("6. Visualizza matrice di confusione")
        print("7. Ottimizza il modello con GridSearchCV")
        print("8. Esci")

        try:
            scelta = int(input("Scegli un'opzione [1-8]: "))
        except ValueError:
            print("Input non valido. Inserisci un numero da 1 a 8.")
            continue

        if scelta == 1:
            df, wine = load_and_prepare()
        elif scelta == 2:
            explore(df)
        elif scelta == 3:
            plot_pca(df)
        elif scelta == 4:
            model, X_test, y_test, y_pred = train_and_evaluate(df)
        elif scelta == 5:
            if model is None:
                print("Prima allena il modello (opzione 4).")
            else:
                plot_feature_importances(model, wine.feature_names)
        elif scelta == 6:
            if y_test is None or y_pred is None:
                print("Prima allena il modello (opzione 4).")
            else:
                plot_confusion(y_test, y_pred, wine.target_names)
        elif scelta == 7:
            optimize_model(df)
        elif scelta == 8:
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == '__main__':
    main()
# Esegui il programma