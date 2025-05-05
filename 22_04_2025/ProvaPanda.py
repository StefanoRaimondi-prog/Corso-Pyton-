import pandas as pd
import numpy as np
import os

# Percorso assoluto basato sulla posizione dello script
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, 'vendite.csv')

# Verifica per sicurezza
print(" Percorso completo:", file_path)
print(" File esiste?", os.path.exists(file_path))

# Lettura del file
df = pd.read_csv(file_path)
print(df.head())
print(df.info())
