import numpy as np

# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50
array = np.random.randint(10, 51, size=20)
print("Array originale:")
print(array)

# 2. Estrai i primi 10 elementi
primi_10 = array[:10]
print("\nPrimi 10 elementi:")
print(primi_10)

# 3. Estrai gli ultimi 5 elementi
ultimi_5 = array[-5:]
print("\nUltimi 5 elementi:")
print(ultimi_5)

# 4. Estrai gli elementi dall'indice 5 all'indice 15 (escluso)
dal_5_al_15 = array[5:15]
print("\nElementi dall'indice 5 al 15 (escluso):")
print(dal_5_al_15)

# 5. Estrai ogni terzo elemento dell'array
ogni_terzo = array[::3]
print("\nOgni terzo elemento:")
print(ogni_terzo)

# 6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99
array[5:10] = 99
print("\nArray dopo la modifica (indici 5-9 impostati a 99):")
print(array)
