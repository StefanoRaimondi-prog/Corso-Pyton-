import pandas as pd

# 1. Caricare i dati in un DataFrame
data = {
    'Prodotto': ['Mouse', 'Tastiera', 'Monitor', 'Mouse', 'Monitor', 'Tastiera', 'Mouse'],
    'Quantità': [5, 3, 2, 4, 1, 2, 6],
    'Prezzo Unitario': [20, 45, 150, 20, 150, 45, 20],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma']
}
df = pd.DataFrame(data)

# 2. Aggiungere una colonna "Totale Vendite" = Quantità * Prezzo Unitario
df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']

# 3. Raggruppare i dati per prodotto e calcolare il totale delle vendite per ciascun prodotto
vendite_per_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()

# 4. Trovare il prodotto più venduto in termini di Quantità
prodotto_piu_venduto = df.groupby('Prodotto')['Quantità'].sum().idxmax()

# 5. Identificare la città con il maggior volume di vendite totali
citta_top = df.groupby('Città')['Totale Vendite'].sum().idxmax()

# 6. Creare un nuovo DataFrame con vendite superiori a 1000 euro
df_superiori_1000 = df[df['Totale Vendite'] > 1000]

# 7. Ordinare il DataFrame originale in ordine decrescente per "Totale Vendite"
df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)

# 8. Visualizzare il totale delle vendite per ogni città
vendite_per_citta = df.groupby('Città')['Totale Vendite'].sum()

# Output dei risultati
print("DataFrame originale con colonna 'Totale Vendite':")
print(df)

print("\nTotale vendite per prodotto:")
print(vendite_per_prodotto)

print(f"\nProdotto più venduto per quantità: {prodotto_piu_venduto}")

print(f"\nCittà con il maggior volume di vendite: {citta_top}")

print("\nVendite superiori a 1000 euro:")
print(df_superiori_1000)

print("\nDataFrame ordinato per 'Totale Vendite' (decrescente):")
print(df_ordinato)

print("\nTotale delle vendite per ogni città:")
print(vendite_per_citta)
