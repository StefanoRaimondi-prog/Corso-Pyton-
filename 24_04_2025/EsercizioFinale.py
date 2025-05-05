# Importazione delle librerie necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Impostazione del seed per la riproducibilità dei risultati
np.random.seed(0)

# Numero di giorni da generare
giorni = 365

# Creazione dell'intervallo di date giornaliere
date = pd.date_range(start="2024-01-01", periods=giorni)

# Parametri statistici della distribuzione dei visitatori
media = 2000
deviazione = 500

# Simulazione di un trend di crescita lineare della popolarità del parco
trend = np.linspace(0, 1000, giorni)

# Generazione dei visitatori come distribuzione normale con trend crescente
visitatori = np.random.normal(media, deviazione, giorni) + trend

# Creazione del DataFrame con le date come indice
df = pd.DataFrame({'Data': date, 'Visitatori': visitatori})
df.set_index('Data', inplace=True)

# Calcolo della media mensile dei visitatori
media_mensile = df.resample('M').mean()

# Calcolo della deviazione standard mensile
deviazione_mensile = df.resample('M').std()

# Primo grafico: linee dei visitatori giornalieri + media mobile a 7 giorni
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri')
plt.plot(df['Visitatori'].rolling(window=7).mean(), label='Media mobile a 7 giorni', linewidth=2)
plt.title('Visitatori Giornalieri con Media Mobile Settimanale')
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Secondo grafico: barra della media mensile
plt.figure(figsize=(10, 5))
plt.bar(media_mensile.index.strftime('%Y-%m'), media_mensile['Visitatori'])
plt.title('Media Mensile dei Visitatori')
plt.xlabel('Mese')
plt.ylabel('Numero Medio di Visitatori')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
