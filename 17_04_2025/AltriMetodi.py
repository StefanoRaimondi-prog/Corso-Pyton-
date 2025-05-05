import numpy as np

# Esercizio su arange
print("Esercizio con arange:")
arr = np.arange(10)
print("Array generato con arange(10):", arr)
# Output atteso: [0 1 2 3 4 5 6 7 8 9]

print("\nEsercizio con reshape:")
# Esercizio su reshape
arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print("Array originale:", arr)
print("Array rimodellato con reshape((2, 3)):\n", reshaped_arr)
# Output atteso:
# [[0 1 2]
#  [3 4 5]]
