import numpy as np

# 1. Crea una matrice 6x6 con numeri casuali da 1 a 100
matrice = np.random.randint(1, 101, size=(6, 6))
print("Matrice originale:\n", matrice)

# 2. Estrai la sotto-matrice centrale 4x4
sotto_matrice = matrice[1:5, 1:5]
print("\nSotto-matrice centrale 4x4:\n", sotto_matrice)

# 3. Inverti le righe della sotto-matrice
matrice_invertita = sotto_matrice[::-1]
print("\nMatrice invertita (righe invertite):\n", matrice_invertita)

# 4. Estrai la diagonale principale
diagonale = np.diag(matrice_invertita)
print("\nDiagonale principale della matrice invertita:\n", diagonale)

# 5. Sostituisci tutti i multipli di 3 con -1
modificata = matrice_invertita.copy()
modificata[modificata % 3 == 0] = -1
print("\nMatrice invertita con multipli di 3 sostituiti da -1:\n", modificata)
