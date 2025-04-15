import requests
from datetime import datetime, timedelta

# Funzione per ottenere le coordinate (latitudine e longitudine) di una città
def get_coordinates(city_name):
    # URL dell'API di geocoding per cercare la città
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=it"
    res = requests.get(url)  # Effettua una richiesta GET all'API
    data = res.json()  # Converte la risposta in formato JSON

    # Controlla se ci sono risultati per la città cercata
    if data.get("results"):
        location = data["results"][0]  # Prende il primo risultato
        return location["latitude"], location["longitude"]  # Restituisce latitudine e longitudine
    else:
        # Messaggio di errore se la città non è stata trovata
        print("Città non trovata.")
        return None, None  # Restituisce valori nulli

# Funzione per ottenere i dati meteo in base alle coordinate e ai parametri richiesti
def get_weather(lat, lon, days, extra_params):
    # Calcola la data di inizio (oggi) e la data di fine (oggi + giorni richiesti - 1)
    start_date = datetime.today().date()
    end_date = start_date + timedelta(days=days - 1)

    # URL base dell'API meteo
    base_url = "https://api.open-meteo.com/v1/forecast"
    # Parametri della richiesta, inclusi latitudine, longitudine, dati orari richiesti e intervallo di date
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ",".join(["temperature_2m"] + extra_params),  # Dati richiesti (temperatura + eventuali extra)
        "start_date": start_date,
        "end_date": end_date,
        "timezone": "auto"  # Imposta il fuso orario automaticamente
    }

    res = requests.get(base_url, params=params)  # Effettua una richiesta GET all'API con i parametri
    return res.json()  # Restituisce la risposta in formato JSON

# 1. Input utente: chiede il nome della città
city = input("Inserisci il nome della città: ").strip()

# 2. Durata: chiede per quanti giorni l'utente vuole vedere il meteo (1, 3 o 7)
while True:
    giorni = input("Per quanti giorni vuoi vedere il meteo? (1, 3 o 7): ")
    if giorni in ["1", "3", "7"]:  # Controlla che l'input sia valido
        giorni = int(giorni)  # Converte l'input in un intero
        break
    print("Scelta non valida. Scegli tra 1, 3 o 7.")  # Messaggio di errore per input non valido

# 3. Dati extra: chiede se l'utente vuole vedere dati aggiuntivi (velocità del vento, precipitazioni)
extra = []
if input("Vuoi vedere la velocità del vento? (s/n): ").lower() == "s":
    extra.append("windspeed_10m")  # Aggiunge la velocità del vento ai parametri extra
if input("Vuoi vedere le precipitazioni? (s/n): ").lower() == "s":
    extra.append("precipitation")  # Aggiunge le precipitazioni ai parametri extra

# 4. Recupero coordinate: ottiene latitudine e longitudine della città
lat, lon = get_coordinates(city)

if lat and lon:  # Procede solo se le coordinate sono valide
    # 5. Recupero meteo: ottiene i dati meteo per le coordinate e i parametri specificati
    meteo = get_weather(lat, lon, giorni, extra)
    
    # 6. Stampa: stampa i dati meteo in un formato leggibile
    print("\n METEO per", city.upper())  # Titolo con il nome della città in maiuscolo
    for i in range(len(meteo["hourly"]["time"])):  # Itera su tutti i dati orari
        ora = meteo["hourly"]["time"][i]  # Ora specifica
        temp = meteo["hourly"]["temperature_2m"][i]  # Temperatura a quell'ora
        output = f"{ora} -  {temp}°C"  # Formatta l'output con l'ora e la temperatura
        if "windspeed_10m" in meteo["hourly"]:  # Aggiunge la velocità del vento se richiesta
            output += f" |  {meteo['hourly']['windspeed_10m'][i]} km/h"
        if "precipitation" in meteo["hourly"]:  # Aggiunge le precipitazioni se richieste
            output += f" |  {meteo['hourly']['precipitation'][i]} mm"
        print(output)  # Stampa l'output per ogni ora
