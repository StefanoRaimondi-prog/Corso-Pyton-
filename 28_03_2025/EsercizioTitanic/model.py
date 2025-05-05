# model.py

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, r2_score
from clean_data import clean_titanic_data

def train_and_predict_rf(raw_path="train.csv",
                         model_path="titanic_rf_model.joblib",
                         pred_path="predictions_rf.csv"):
    """
    Allena e ottimizza una Random Forest,
    valuta sul test set (incluso R^2 sulle probabilità)
    e salva modello + predizioni.
    """
    base = os.path.dirname(__file__)
    raw_full = raw_path if os.path.isabs(raw_path) else os.path.join(base, raw_path)

    df_raw   = pd.read_csv(raw_full)
    df_clean = clean_titanic_data(raw_full)

    ids = df_raw["PassengerId"]
    X   = df_clean.drop("Survived", axis=1)
    y   = df_clean["Survived"]

    X_train, X_test, y_train, y_test, ids_train, ids_test = train_test_split(
        X, y, ids, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(random_state=42))
    ])
    param_grid = {
        "clf__n_estimators": [50, 100, 200],
        "clf__max_depth":    [None, 5, 10, 20],
        "clf__min_samples_split": [2, 5, 10]
    }
    grid = GridSearchCV(pipeline, param_grid, cv=5,
                        scoring="accuracy", n_jobs=-1, verbose=1)
    grid.fit(X_train, y_train)
    best = grid.best_estimator_

    print("\n=== RF Best Hyperparameters ===")
    print(grid.best_params_)
    print(f"Best CV accuracy: {grid.best_score_:.3f}")

    # Predizioni e probabilità
    y_pred = best.predict(X_test)
    proba  = best.predict_proba(X_test)[:,1]

    # R^2 score sulle probabilità
    r2 = r2_score(y_test, proba)
    print(f"R^2 score (probabilities): {r2:.3f}")

    print("\n=== RF Test Set Performance ===")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Salva le predizioni
    results = pd.DataFrame({
        "PassengerId":   ids_test.values,
        "TrueLabel":     y_test.values,
        "PredLabel":     y_pred,
        "Survival_Prob": proba
    })
    results.to_csv(os.path.join(base, pred_path), index=False)
    print(f"Predictions saved to '{pred_path}'")

    joblib.dump(best, os.path.join(base, model_path))
    print(f"RF model saved to '{model_path}'")

    return best

def train_and_predict_dt(raw_path="train.csv",
                         model_path="titanic_dt_model.joblib",
                         pred_path="predictions_dt.csv"):
    """
    Allena e ottimizza un Decision Tree,
    valuta sul test set (incluso R^2 sulle probabilità)
    e salva modello + predizioni.
    """
    base = os.path.dirname(__file__)
    raw_full = raw_path if os.path.isabs(raw_path) else os.path.join(base, raw_path)

    df_raw   = pd.read_csv(raw_full)
    df_clean = clean_titanic_data(raw_full)

    ids = df_raw["PassengerId"]
    X   = df_clean.drop("Survived", axis=1)
    y   = df_clean["Survived"]

    X_train, X_test, y_train, y_test, ids_train, ids_test = train_test_split(
        X, y, ids, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", DecisionTreeClassifier(random_state=42))
    ])
    param_grid = {
        "clf__criterion": ["gini", "entropy"],
        "clf__max_depth": [None, 5, 10, 20],
        "clf__min_samples_split": [2, 5, 10]
    }
    grid = GridSearchCV(pipeline, param_grid, cv=5,
                        scoring="accuracy", n_jobs=-1, verbose=1)
    grid.fit(X_train, y_train)
    best = grid.best_estimator_

    print("\n=== DT Best Hyperparameters ===")
    print(grid.best_params_)
    print(f"Best CV accuracy: {grid.best_score_:.3f}")

    # Predizioni e probabilità
    y_pred = best.predict(X_test)
    proba  = best.predict_proba(X_test)[:,1]

    # R^2 score sulle probabilità
    r2 = r2_score(y_test, proba)
    print(f"R^2 score (probabilities): {r2:.3f}")

    print("\n=== DT Test Set Performance ===")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Salva le predizioni
    results = pd.DataFrame({
        "PassengerId":   ids_test.values,
        "TrueLabel":     y_test.values,
        "PredLabel":     y_pred,
        "Survival_Prob": proba
    })
    results.to_csv(os.path.join(base, pred_path), index=False)
    print(f"Predictions saved to '{pred_path}'")

    joblib.dump(best, os.path.join(base, model_path))
    print(f"DT model saved to '{model_path}'")

    return best

if __name__ == "__main__":
    # Per default alleniamo entrambi
    train_and_predict_rf()
    train_and_predict_dt()
