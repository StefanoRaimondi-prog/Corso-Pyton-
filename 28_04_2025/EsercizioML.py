# Importare le librerie necessarie
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Caricare il dataset Wine
data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.info()
print(df.head())
X = data.data  # Caratteristiche
y = data.target  # Etichette

# 2. Standardizzare le caratteristiche
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Suddividere i dati in training (70%) e test (30%)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# 4. Applicare DecisionTreeClassifier per la classificazione
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# 5. Valutare la performance del modello
y_pred = clf.predict(X_test)
print("Classification Report:")
print(
    classification_report(
        y_test, y_pred, target_names=data.target_names
    )
)

# 6. Visualizzare la matrice di confusione
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=data.target_names,
    yticklabels=data.target_names
)
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Confusion Matrix')
plt.show()
