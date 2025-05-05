import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])  # Output: 1

# Slicing
print(arr[1:3])  # Output: [2 3]

# Boolean Indexing
print(arr[arr > 2])  # Output: [3 4 5]