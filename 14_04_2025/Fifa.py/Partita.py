import random
from Vecchie_leggende import SquadraVecchieLeggende  # Importa la classe SquadraVecchieLeggende
from Nuove_leggende import SquadraNuoveLeggende  # Importa la classe SquadraNuoveLeggende

# Funzione per mostrare il menu principale
def mostra_menu():
    print("\n--- MENU PARTITA ---")
    print("1. Scegli Vecchie Leggende")  # Opzione per scegliere la squadra Vecchie Leggende
    print("2. Scegli Nuove Leggende")  # Opzione per scegliere la squadra Nuove Leggende
    print("3. Esci")  # Opzione per uscire dal gioco

# Funzione per mostrare i giocatori delle due squadre
def mostra_giocatori(squadra_1, squadra_2):
    print("\n Squadre in campo:")
    print(f"\n {squadra_1.nome} (Allenatore: {squadra_1.allenatore.nome})")  # Mostra il nome della squadra e dell'allenatore
    for giocatore in squadra_1.giocatori:  # Itera sui giocatori della prima squadra
        print(f"- {giocatore.nome} (Potenza base: {giocatore.potenza_base})")  # Mostra il nome e la potenza base del giocatore
    
    print(f"\n {squadra_2.nome} (Allenatore: {squadra_2.allenatore.nome})")  # Mostra il nome della seconda squadra e dell'allenatore
    for giocatore in squadra_2.giocatori:  # Itera sui giocatori della seconda squadra
        print(f"- {giocatore.nome} (Potenza base: {giocatore.potenza_base})")  # Mostra il nome e la potenza base del giocatore

# Funzione per gestire un'azione di gioco
def azione_di_gioco(squadra, avversaria):
    print("\nScegli il tuo attaccante:")
    for i, giocatore in enumerate(squadra.giocatori):  # Mostra i giocatori della squadra
        print(f"{i + 1}. {giocatore.nome}")
    scelta = int(input("Numero: ")) - 1  # L'utente sceglie un giocatore

    giocatore = squadra.giocatori[scelta]  # Seleziona il giocatore scelto

    # SCELTE TATTICHE
    zona = input("Da dove vuoi tirare? (dentro/fuori): ").lower()  # Scelta della zona di tiro
    passaggio = input("Vuoi fare un passaggio prima del tiro? (sì/no): ").lower()  # Scelta di fare un passaggio
    smarcamento = input("Vuoi tentare di smarcarti? (sì/no): ").lower()  # Scelta di smarcarsi

    modificatore = 0  # Modificatore iniziale

    # ZONA DI TIRO
    if zona == "dentro":
        modificatore += 10  # Bonus per tiro dentro l'area
    else:
        modificatore -= 25  # Penalità per tiro fuori area

    # PASSAGGIO
    if passaggio == "sì":
        modificatore += 5  # Bonus per passaggio
    else:
        modificatore -= 5  # Penalità per non fare passaggio

    # SMARCAMENTO
    if smarcamento == "sì":
        riuscito = random.choice([True, False])  # Tentativo di smarcamento
        if riuscito:
            print(" Smarcamento riuscito!")
            modificatore += 10  # Bonus per smarcamento riuscito
        else:
            print(" Smarcamento fallito!")
            modificatore -= 10  # Penalità per smarcamento fallito
    else:
        modificatore -= 15  # Penalità per non tentare smarcamento

    # Calcolo della potenza del tiro
    potenza = giocatore.potenza_reale(squadra.allenatore.impatto) + modificatore
    tiro = random.randint(1, 100)  # Genera un numero casuale per il tiro

    print(f"\n {giocatore.nome} tira con potenza modificata: {potenza}...")
    if tiro <= potenza:  # Verifica se il tiro è un gol
        print(" GOOOOOL!!!")
        giocatore.gol += 1  # Incrementa il numero di gol del giocatore
    else:
        print(" Tiro sbagliato o parato!")  # Tiro fallito

    # RISPOSTA AVVERSARIA
    print(f"\n La squadra avversaria contrattacca...")
    avversario = random.choice(avversaria.giocatori)  # Sceglie un giocatore avversario casualmente
    potenza_avv = avversario.potenza_reale(avversaria.allenatore.impatto)  # Calcola la potenza del tiro avversario
    random_bonus = random.randint(-90, 10)  # Bonus casuale per il tiro avversario
    totale_avv = potenza_avv + random_bonus  # Potenza totale del tiro avversario
    tiro_avv = random.randint(1, 100)  # Genera un numero casuale per il tiro avversario

    print(f"{avversario.nome} tenta il tiro con potenza {totale_avv}...")
    if tiro_avv <= totale_avv:  # Verifica se il tiro avversario è un gol
        print(" GOL della squadra avversaria!")
        avversario.gol += 1  # Incrementa il numero di gol dell'avversario
    else:
        print(" La tua difesa regge!")  # Tiro avversario fallito

# Funzione per mostrare le statistiche delle squadre
def mostra_statistiche(squadra, avversaria):
    print(f"\n Statistiche: {squadra.nome}")
    for giocatore in squadra.giocatori:  # Mostra i gol di ogni giocatore della squadra
        print(f"{giocatore.nome}: {giocatore.gol} gol")
    
    print(f"\n Statistiche: {avversaria.nome}")
    for giocatore in avversaria.giocatori:  # Mostra i gol di ogni giocatore della squadra avversaria
        print(f"{giocatore.nome}: {giocatore.gol} gol")

# --- MAIN LOOP ---
while True:
    mostra_menu()  # Mostra il menu principale
    scelta = input("Scelta: ")  # L'utente sceglie un'opzione

    if scelta == "1":
        squadra = SquadraVecchieLeggende()  # Crea la squadra Vecchie Leggende
        avversaria = SquadraNuoveLeggende()  # Crea la squadra Nuove Leggende
    elif scelta == "2":
        squadra = SquadraNuoveLeggende()  # Crea la squadra Nuove Leggende
        avversaria = SquadraVecchieLeggende()  # Crea la squadra Vecchie Leggende
    elif scelta == "3":
        print("Uscita dal gioco. ⚽ Ciao!")  # Esce dal gioco
        break
    else:
        print("Scelta non valida.")  # Messaggio di errore per scelta non valida
        continue

    mostra_giocatori(squadra, avversaria)  # Mostra i giocatori delle squadre

    while True:
        print("\n1. Azione di gioco")  # Opzione per eseguire un'azione di gioco
        print("2. Vedi statistiche")  # Opzione per vedere le statistiche
        print("3. Torna al menu principale")  # Opzione per tornare al menu principale
        azione = input("Scelta: ")  # L'utente sceglie un'opzione
        if azione == "1":
            azione_di_gioco(squadra, avversaria)  # Esegue un'azione di gioco
        elif azione == "2":
            mostra_statistiche(squadra, avversaria)  # Mostra le statistiche
        elif azione == "3":
            break  # Torna al menu principale
        else:
            print("Opzione non valida.")  # Messaggio di errore per opzione non valida
