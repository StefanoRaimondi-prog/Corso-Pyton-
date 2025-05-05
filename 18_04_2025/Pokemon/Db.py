import mysql.connector

# Funzione per creare e restituire una connessione attiva al DB
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Inserisci la tua password
            database="pokemon_db"  # Sostituisci con il nome corretto del tuo database
        )
        return conn
    except mysql.connector.Error as err:
        print("Errore di connessione al database:", err)
        return None

# Funzione di utilità per eseguire query SELECT (usata da views o analisi dirette)
def esegui_query(query, parametri=None):
    conn = get_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(query, parametri or ())
        risultati = cursor.fetchall()
        return risultati
    except mysql.connector.Error as err:
        print("Errore durante l'esecuzione della query:", err)
        return []
    finally:
        conn.close()

# Funzione per chiamare una stored procedure
def chiama_procedura(nome_proc, parametri):
    conn = get_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.callproc(nome_proc, parametri)
        risultati = []
        for result in cursor.stored_results():
            risultati.extend(result.fetchall())
        return risultati
    except mysql.connector.Error as err:
        print(f"Errore durante la procedura {nome_proc}:", err)
        return []
    finally:
        conn.close()
