import numpy as np

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing sulle righe
print(arr_2d[1:3])    # Output: [[ 5  6  7  8]
                      #          [ 9 10 11 12]]

# Slicing sulle colonne
print(arr_2d[:, 1:3]) # Output: [[ 2  3]
                      #          [ 6  7]
                      #          [10 11]]

# Slicing misto
print(arr_2d[1:, 1:3]) # Output: [[ 6  7]
                       #          [10 11]]
