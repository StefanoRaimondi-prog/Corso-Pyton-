# ✅ Dizionario che contiene tutti i concetti da spiegare, suddivisi per macro-categoria
# Ogni voce è una categoria (es. "Operatori"), e contiene una lista di concetti + esempi di codice
concetti = {
    "1. Sintassi base": [
        ("Print", 'print("Ciao, mondo!")'),
        ("Commenti", '# Questo è un commento'),
        ("Indentazione", 'if True:\n    print("Indentato correttamente")')
    ],
    "2. Variabili e tipi di dato": [
        ("Assegnazione", 'x = 10'),
        ("Tipi", 'a = 5       # int\nb = 3.14    # float\nc = "ciao"  # str'),
        ("Conversione", 'x = int("42")\ny = str(100)')
    ],
    "3. Operatori": [
        ("Aritmetici", 'a = 5\nb = 2\nprint(a + b)  # 7'),
        ("Confronto", 'print(5 > 3)  # True'),
        ("Logici", 'print(True and False)  # False')
    ],
    "4. Controllo del flusso": [
        ("if/else", 'x = 10\nif x > 5:\n    print("Maggiore di 5")'),
        ("while", 'i = 0\nwhile i < 3:\n    print(i)\n    i += 1'),
        ("for", 'for i in range(3):\n    print(i)')
    ],
    "5. Funzioni": [
        ("Definizione", 'def saluta():\n    print("Ciao!")'),
        ("Parametri", 'def somma(a, b):\n    return a + b'),
        ("Valori di default", 'def saluta(nome="utente"):\n    print("Ciao", nome)')
    ],
    "6. Stringhe e metodi": [
        ("Upper", 'print("ciao".upper())  # CIAO'),
        ("Slicing", 's = "Python"\nprint(s[0:3])  # Pyt'),
        ("f-string", 'nome = "Luca"\nprint(f"Ciao {nome}")')
    ],
    "7. Collezioni": [
        ("Liste", 'numeri = [1, 2, 3]\nnumeri.append(4)'),
        ("Tuple", 'coordinate = (10, 20)'),
        ("Dizionari", 'persona = {"nome": "Luca", "eta": 30}'),
        ("Set", 'frutti = {"mela", "banana", "pera"}')
    ],
    "8. Iterazioni su collezioni": [
        ("for su lista", 'for x in [1,2,3]:\n    print(x)'),
        ("enumerate", 'for i, valore in enumerate(["a", "b"]):\n    print(i, valore)'),
        ("in", 'if "a" in ["a", "b"]:\n    print("presente")')
    ],
    "9. Decoratori": [
        ("Decoratore base", '''def mio_decoratore(f):
    def wrapper():
        print("Prima della funzione")
        f()
        print("Dopo la funzione")
    return wrapper

@mio_decoratore
def saluta():
    print("Ciao!")

saluta()''')
    ]
}

# ✅ Decoratore reale utilizzato nel programma
# Serve per loggare l'inizio e la fine di una funzione
# Lo usiamo per dimostrare il funzionamento dei decoratori in pratica
def logger(f):
    def wrapper(*args, **kwargs):  # wrapper accetta qualsiasi argomento
        print(f"\n[LOG] Sto per eseguire: {f.__name__}")  # f.__name__ mostra il nome della funzione originale
        risultato = f(*args, **kwargs)  # esegue la funzione originale con i suoi argomenti
        print(f"[LOG] Fine esecuzione: {f.__name__}")
        return risultato  # restituisce ciò che la funzione originale avrebbe restituito
    return wrapper

# ✅ Funzione che mostra il menu delle categorie all'utente
# Usa la funzione print, il ciclo for e il dizionario "concetti"
def mostra_menu():
    print("\n--- MENU CATEGORIE ---")
    for chiave in concetti:
        print(chiave)

# ✅ Funzione decorata con @logger
# Quando viene eseguita, il decoratore logger stampa un log prima e dopo
# Questa funzione stampa tutti i concetti e gli esempi relativi a una categoria
@logger
def mostra_concetti(categoria):
    print(f"\n▶ Concetti in {categoria}:")
    for nome, esempio in concetti[categoria]:  # unpacking di tuple
        print(f"\n🔹 {nome}:\n{esempio}")

# ✅ Funzione principale del programma
# Mostra il menu, prende input dall'utente, gestisce il ciclo principale
def main():
    while True:  # ciclo infinito finché l'utente non scrive "esci"
        mostra_menu()
        scelta = input("\nScegli una categoria (1-9) o 'esci': ")

        if scelta.lower() == 'esci':  # controllo su stringa
            print("Alla prossima!")
            break

        # Cerca una categoria che comincia col numero scelto, es: "3" -> "3. Operatori"
        categoria = next((k for k in concetti if k.startswith(scelta)), None)

        if categoria:
            mostra_concetti(categoria)  # chiama la funzione decorata
        else:
            print("Scelta non valida. Riprova.")

# ✅ Avvio del programma
main()
