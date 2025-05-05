from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier

# 1. Carica il dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# 2. Suddividi in train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# 3. Definisci la griglia di iper-parametri
param_grid = {
    'max_depth': [3, 5, 7],
    'criterion': ['gini', 'entropy']
}

# 4. Imposta GridSearchCV su DecisionTreeClassifier
grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'  # opzionale, di default usa 'accuracy'
)

# 5. Esegui la ricerca esaustiva
grid_search.fit(X_train, y_train)

# 6. Stampa i risultati
print("Migliori parametri:", grid_search.best_params_)
print(f"Best CV score: {grid_search.best_score_:.3f}")

# 7. Valuta il modello ottimale sul test set
best_tree = grid_search.best_estimator_
print(f"Accuratezza sul test set: {best_tree.score(X_test, y_test):.3f}")
