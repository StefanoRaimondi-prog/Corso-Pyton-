import numpy as np

# 1. Crea un array di numeri interi da 10 a 49
array = np.arange(10, 50)
print("Array iniziale:")
print(array)

# 2. Verifica il tipo di dato (dtype)
print("Tipo di dato iniziale:", array.dtype)

# 3. Cambia il tipo di dato in float64
array_float = array.astype(np.float64)
print("Tipo di dato dopo la conversione:", array_float.dtype)

# 4. Stampa la forma dell'array (shape)
print("Forma dell'array:", array_float.shape)
