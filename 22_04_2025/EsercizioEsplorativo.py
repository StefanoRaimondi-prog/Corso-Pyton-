import pandas as pd
import numpy as np
import random

# 1. Generazione dati casuali
nomi = ['Alice', 'Bob', 'Carla', 'David', 'Elisa', 'Franco', 'Gina', 'Luca', 'Marta', 'Nico']
città = ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna']
dati = {
    'Nome': random.choices(nomi, k=15),
    'Età': np.random.choice([15, 22, 35, 42, 67, 80, np.nan], 15),
    'Città': random.choices(città, k=15),
    'Salario': np.random.choice([1200, 1500, 1800, 2000, 2500, np.nan], 15)
}
df = pd.DataFrame(dati)

# 2. Prime e ultime 5 righe
print(" Prime 5 righe:")
print(df.head())
print("\n Ultime 5 righe:")
print(df.tail())

# 3. Tipi di dati
print("\n Tipi di dati:")
print(df.dtypes)

# 4. Statistiche descrittive
print("\n Statistiche descrittive:")
print(df.describe())

# 5. Rimozione duplicati
df = df.drop_duplicates()

# 6. Gestione dei valori mancanti con mediana
df['Età'].fillna(df['Età'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)

# 7. Aggiunta colonna 'Categoria Età'
def categoria_eta(età):
    if età <= 18:
        return 'Giovane'
    elif età <= 65:
        return 'Adulto'
    else:
        return 'Senior'

df['Categoria Età'] = df['Età'].apply(categoria_eta)

# 8. Salvataggio CSV
df.to_csv('dati_puliti.csv', index=False)

print("\n DataFrame pulito e salvato come 'dati_puliti.csv'")
print(df)
