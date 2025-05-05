import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Dataset di esempio: 200 campioni, 5 feature
np.random.seed(42)
X = np.random.rand(200, 5)

# 2. Normalizzazione delle feature (consigliata)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Configura PCA per ridurre a 2 componenti principali
n_components = 2
pca = PCA(n_components=n_components)

# 4. Applica PCA
X_pca = pca.fit_transform(X_scaled)

# 5. Stampa varianza spiegata da ciascuna componente
print(
    "Varianza spiegata da ciascuna componente:",
    pca.explained_variance_ratio_
)

# 6. Visualizza i dati proiettati sulle 2 componenti principali
plt.figure(figsize=(8, 6))
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c='blue',
    edgecolor='k',
    alpha=0.7
)
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")
plt.title("Visualizzazione dati dopo PCA (2D)")
plt.grid(True)
plt.tight_layout()
plt.show()
