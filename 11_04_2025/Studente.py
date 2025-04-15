import mysql.connector
from mysql.connector import Error

# Funzione per connettersi al database MySQL
def connetti_al_db():
    try:
        # Connessione al server MySQL
        conn = mysql.connector.connect(
            host="localhost",  # Indirizzo del server MySQL
            user="root",       # Nome utente del database
            password="",       # Password del database
            port=8889          # Porta del server MySQL
        )
        return conn  # Restituisce l'oggetto connessione
    except Error as e:
        # Gestione degli errori di connessione
        print("Errore di connessione:", e)
        return None

# Funzione per configurare il database e creare le tabelle necessarie
def setup_database(conn):
    cursor = conn.cursor()
    # Creazione del database "scuola" se non esiste
    cursor.execute("CREATE DATABASE IF NOT EXISTS scuola")
    conn.database = "scuola"  # Seleziona il database "scuola"

    # Creazione della tabella "studenti" per memorizzare i dati degli studenti
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studenti (
        id INT AUTO_INCREMENT PRIMARY KEY,  # ID univoco per ogni studente
        nome VARCHAR(100) NOT NULL,         # Nome dello studente
        cognome VARCHAR(100) NOT NULL,      # Cognome dello studente
        email VARCHAR(100) UNIQUE NOT NULL, # Email univoca dello studente
        matricola VARCHAR(20) UNIQUE NOT NULL # Matricola univoca dello studente
    )
    """)

    # Creazione della tabella "voti" per memorizzare i voti degli studenti
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voti (
        id INT AUTO_INCREMENT PRIMARY KEY,  # ID univoco per ogni voto
        id_studente INT,                    # ID dello studente associato
        voto FLOAT NOT NULL,                # Voto dello studente
        FOREIGN KEY (id_studente) REFERENCES studenti(id) ON DELETE CASCADE
        # Chiave esterna che collega i voti agli studenti
    )
    """)
    conn.commit()  # Conferma le modifiche al database
    cursor.close()

# Funzione per inserire un nuovo studente nel database
def inserisci_studente(conn):
    # Richiede i dati dello studente all'utente
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    email = input("Email: ")
    matricola = input("Matricola: ")

    cursor = conn.cursor()
    try:
        # Inserisce i dati dello studente nella tabella "studenti"
        cursor.execute("""
            INSERT INTO studenti (nome, cognome, email, matricola)
            VALUES (%s, %s, %s, %s)
        """, (nome, cognome, email, matricola))
        conn.commit()  # Conferma l'inserimento
        print("Studente inserito con successo.")
    except Error as e:
        # Gestione degli errori durante l'inserimento
        print("Errore:", e)
    cursor.close()

# Funzione per eliminare uno studente dal database
def elimina_studente(conn):
    # Richiede la matricola dello studente da eliminare
    matricola = input("Matricola dello studente da eliminare: ")
    cursor = conn.cursor()
    # Elimina lo studente con la matricola specificata
    cursor.execute("DELETE FROM studenti WHERE matricola = %s", (matricola,))
    if cursor.rowcount > 0:
        conn.commit()  # Conferma l'eliminazione
        print(f"Studente con matricola '{matricola}' eliminato.")
    else:
        # Messaggio se la matricola non è trovata
        print(f"Nessuno studente trovato con matricola '{matricola}'.")
    cursor.close()

# Funzione per calcolare la media dei voti di uno studente
def calcola_media_studente(conn):
    # Richiede la matricola dello studente
    matricola = input("Inserisci la matricola dello studente: ")
    cursor = conn.cursor(dictionary=True)

    # Recupera i dati dello studente dalla tabella "studenti"
    cursor.execute("SELECT id, nome, cognome FROM studenti WHERE matricola = %s", (matricola,))
    studente = cursor.fetchone()

    if studente:
        # Recupera i voti dello studente dalla tabella "voti"
        cursor.execute("SELECT voto FROM voti WHERE id_studente = %s", (studente['id'],))
        voti = cursor.fetchall()
        if voti:
            # Calcola la media dei voti
            media = sum(v['voto'] for v in voti) / len(voti)
            print(f"La media di {studente['nome']} {studente['cognome']} è: {round(media, 2)}")
        else:
            # Messaggio se non ci sono voti per lo studente
            print("Nessun voto trovato per questo studente.")
    else:
        # Messaggio se la matricola non è trovata
        print("Matricola non trovata.")
    cursor.close()

# Funzione principale del menu
def menu():
    # Connessione al database
    conn = connetti_al_db()
    if conn is None:
        return
    # Configurazione del database
    setup_database(conn)

    while True:
        # Mostra il menu all'utente
        print("\n====== MENU ======")
        print("1. Inserisci studente")
        print("2. Elimina studente")
        print("3. Calcola media voti studente")
        print("4. Esci")

        # Richiede la scelta dell'utente
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == "1":
            inserisci_studente(conn)  # Inserisce un nuovo studente
        elif scelta == "2":
            elimina_studente(conn)  # Elimina uno studente
        elif scelta == "3":
            calcola_media_studente(conn)  # Calcola la media dei voti
        elif scelta == "4":
            # Esce dal programma
            print("Uscita dal programma.")
            break
        else:
            # Messaggio per scelta non valida
            print("Scelta non valida.")

    conn.close()  # Chiude la connessione al database
    print("Connessione chiusa.")

# Punto di ingresso del programma
if __name__ == "__main__":
    menu()
