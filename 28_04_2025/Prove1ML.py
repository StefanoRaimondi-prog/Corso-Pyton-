""" # Importazione delle librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Caricamento del dataset
data = load_iris()
X = data.data  # le caratteristiche
y = data.target  # le etichette

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parametri da testare
random_states = [0, 42, 100]
n_estimators_list = [50, 100, 150]

# Lista per salvare i risultati
results = []

# Ciclo per provare diverse combinazioni di parametri
for random_state in random_states:
    for n_estimators in n_estimators_list:
        # Creazione del modello
        model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        
        # Addestramento del modello
        model.fit(X_train, y_train)

        # Predizione sul set di test
        predictions = model.predict(X_test)

        # Calcolo dell'accuratezza
        accuracy = accuracy_score(y_test, predictions)

        # Salvataggio dei risultati
        results.append((random_state, n_estimators, accuracy))

# Stampa dei risultati
for random_state, n_estimators, accuracy in results:
    print(f'Random State: {random_state}, N Estimators: {n_estimators}, Accuracy: {accuracy:.2f}') """
    
    
    # Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Caricare il dataset Iris
iris = load_iris()
X = iris.data  # Caratteristiche (lunghezza e larghezza di sepali e petali)
y = iris.target  # Etichette (specie di Iris)

# Suddividere il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parametri da testare
neighbors_list = [3, 5, 7, 9]

# Lista per salvare i risultati
results = []

# Ciclo per provare diversi valori di n_neighbors
for n_neighbors in neighbors_list:
    # Definire il modello
    model = KNeighborsClassifier(n_neighbors=n_neighbors)

    # Addestrare il modello sui dati di training
    model.fit(X_train, y_train)

    # Fare predizioni sui dati di test
    y_pred = model.predict(X_test)

    # Valutare le prestazioni del modello
    accuracy = accuracy_score(y_test, y_pred)

    # Salvataggio dei risultati
    results.append((n_neighbors, accuracy))

# Stampa dei risultati
for n_neighbors, accuracy in results:
    print(f'N Neighbors: {n_neighbors}, Accuracy: {accuracy:.2f}')
    
