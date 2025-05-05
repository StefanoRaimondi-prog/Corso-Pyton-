import sqlite3
import numpy as np

# Funzione per creare e popolare il database
def crea_db():
    # Connessione al database SQLite (crea il file se non esiste)
    conn = sqlite3.connect("analisi.db")
    cur = conn.cursor()

    # Rimuove le tabelle esistenti (se presenti) per evitare conflitti
    cur.execute("DROP TABLE IF EXISTS Ordini")
    cur.execute("DROP TABLE IF EXISTS Clienti")
    cur.execute("DROP TABLE IF EXISTS Prodotti")

    # Creazione della tabella "Clienti" con id, nome e età
    cur.execute("""
        CREATE TABLE Clienti (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            eta INTEGER
        )
    """)

    # Creazione della tabella "Prodotti" con id, nome e prezzo
    cur.execute("""
        CREATE TABLE Prodotti (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            prezzo REAL
        )
    """)

    # Creazione della tabella "Ordini" con id, id_cliente, id_prodotto e quantità
    # Include chiavi esterne per collegare clienti e prodotti
    cur.execute("""
        CREATE TABLE Ordini (
            id INTEGER PRIMARY KEY,
            id_cliente INTEGER,
            id_prodotto INTEGER,
            quantita INTEGER,
            FOREIGN KEY (id_cliente) REFERENCES Clienti(id),
            FOREIGN KEY (id_prodotto) REFERENCES Prodotti(id)
        )
    """)

    # Dati iniziali per la tabella "Clienti"
    clienti = [(1, 'Marco', 30), (2, 'Luca', 25), (3, 'Anna', 28)]
    # Dati iniziali per la tabella "Prodotti"
    prodotti = [(1, 'Libro', 15.50), (2, 'Penna', 1.20), (3, 'Zaino', 35.00)]
    # Dati iniziali per la tabella "Ordini"
    ordini = [
        (1, 1, 1, 2),  # Marco ordina 2 Libri
        (2, 1, 2, 5),  # Marco ordina 5 Penne
        (3, 2, 1, 1),  # Luca ordina 1 Libro
        (4, 2, 3, 1),  # Luca ordina 1 Zaino
        (5, 3, 2, 10)  # Anna ordina 10 Penne
    ]

    # Inserimento dei dati nelle rispettive tabelle
    cur.executemany("INSERT INTO Clienti VALUES (?, ?, ?)", clienti)
    cur.executemany("INSERT INTO Prodotti VALUES (?, ?, ?)", prodotti)
    cur.executemany("INSERT INTO Ordini VALUES (?, ?, ?, ?)", ordini)

    # Salvataggio delle modifiche e chiusura della connessione
    conn.commit()
    conn.close()

# Funzione per visualizzare il menu e gestire le scelte dell'utente
def menu():
    while True:
        # Stampa del menu
        print("\n--- MENU ANALISI ---")
        print("1. Prezzo medio dei prodotti")
        print("2. Quantità media ordinata")
        print("3. Totale speso da ciascun cliente")
        print("4. Prodotto più costoso")
        print("5. Statistiche quantità ordinate")
        print("0. Esci")

        # Lettura della scelta dell'utente
        scelta = input("Scegli un'opzione: ")

        # Esecuzione della funzione corrispondente alla scelta
        if scelta == "1":
            prezzo_medio_prodotti()
        elif scelta == "2":
            quantita_media()
        elif scelta == "3":
            totale_speso_clienti()
        elif scelta == "4":
            prodotto_piu_costoso()
        elif scelta == "5":
            statistiche_quantita()
        elif scelta == "0":
            break  # Esce dal menu
        else:
            print("Scelta non valida")  # Messaggio di errore per input non valido

# Funzione per calcolare e stampare il prezzo medio dei prodotti
def prezzo_medio_prodotti():
    conn = sqlite3.connect("analisi.db")
    cur = conn.cursor()
    # Recupera i prezzi di tutti i prodotti
    cur.execute("SELECT prezzo FROM Prodotti")
    prezzi = [row[0] for row in cur.fetchall()]
    # Calcola e stampa il prezzo medio
    print("Prezzo medio:", np.mean(prezzi))
    conn.close()

# Funzione per calcolare e stampare la quantità media ordinata
def quantita_media():
    conn = sqlite3.connect("analisi.db")
    cur = conn.cursor()
    # Recupera le quantità di tutti gli ordini
    cur.execute("SELECT quantita FROM Ordini")
    quantita = [row[0] for row in cur.fetchall()]
    # Calcola e stampa la quantità media
    print("Quantità media ordinata:", np.mean(quantita))
    conn.close()

# Funzione per calcolare e stampare il totale speso da ciascun cliente
def totale_speso_clienti():
    conn = sqlite3.connect("analisi.db")
    cur = conn.cursor()
    # Calcola il totale speso da ogni cliente unendo le tabelle
    cur.execute("""
        SELECT Clienti.nome, SUM(Prodotti.prezzo * Ordini.quantita)
        FROM Ordini
        JOIN Clienti ON Ordini.id_cliente = Clienti.id
        JOIN Prodotti ON Ordini.id_prodotto = Prodotti.id
        GROUP BY Clienti.id
    """)
    # Stampa il totale speso per ogni cliente
    for nome, totale in cur.fetchall():
        print(f"{nome} ha speso: {totale:.2f}€")
    conn.close()

# Funzione per trovare e stampare il prodotto più costoso
def prodotto_piu_costoso():
    conn = sqlite3.connect("analisi.db")
    cur = conn.cursor()
    # Recupera il prodotto con il prezzo più alto
    cur.execute("SELECT nome, prezzo FROM Prodotti ORDER BY prezzo DESC LIMIT 1")
    nome, prezzo = cur.fetchone()
    # Stampa il nome e il prezzo del prodotto più costoso
    print(f"Il prodotto più costoso è {nome} a {prezzo:.2f}€")
    conn.close()

# Funzione per calcolare e stampare statistiche sulle quantità ordinate
def statistiche_quantita():
    conn = sqlite3.connect("analisi.db")
    cur = conn.cursor()
    # Recupera tutte le quantità ordinate
    cur.execute("SELECT quantita FROM Ordini")
    quantita = np.array([row[0] for row in cur.fetchall()])
    # Calcola e stampa statistiche: media, deviazione standard, massimo e minimo
    print("Media:", np.mean(quantita))
    print("Deviazione standard:", np.std(quantita))
    print("Quantità max:", np.max(quantita))
    print("Quantità min:", np.min(quantita))
    conn.close()

# Punto di ingresso del programma
if __name__ == "__main__":
    crea_db()  # Crea e popola il database
    menu()  # Mostra il menu all'utente
