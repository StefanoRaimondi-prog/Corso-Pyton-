class Biblioteca:
    def __init__(self):
        self.libri = []  # Lista che contiene i titoli dei libri

    def aggiungi_libro(self):
        libro = input("Inserisci il titolo del libro da aggiungere: ").strip()
        if libro:
            self.libri.append(libro)
            print(f"Il libro '{libro}' è stato aggiunto alla biblioteca.")
        else:
            print("Titolo non valido. Riprova.")

    def mostra_libri(self):
        if self.libri:
            print("\Numero libri nella biblioteca:")
            for i, libro in enumerate(self.libri, 1):
                print(f"{i}. {libro}")
        else:
            print("\nLa biblioteca è vuota.")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- MENU ---")
        print("1. Aggiungi libro")
        print("2. Mostra libri")
        print("3. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            biblioteca.aggiungi_libro()
        elif scelta == "2":
            biblioteca.mostra_libri()
        elif scelta == "3":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvia il menu
menu()
