from Libro import Libro

class Libreria:
    def __init__(self):
        self.libri_disponibili = []

    def aggiungi_libro(self, titolo, autore, isbn):
        libro = Libro(titolo, autore, isbn)
        self.libri_disponibili.append(libro)
        print(f"\nLibro aggiunto: {libro}")
        return libro

    def cerca_per_titolo(self, titolo):
        for libro in self.libri_disponibili:
            if libro.titolo.lower() == titolo.lower():
                return libro
        return None

def menu():
    libreria = Libreria()

    while True:
        print("\n=== MENU LIBRERIA ===")
        print("1. Aggiungi libro")
        print("2. Cerca libro per titolo")
        print("3. Esci")

        scelta = input("Scegli un'opzione (1-3): ")

        if scelta == "1":
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            isbn = input("Inserisci l'ISBN del libro: ")
            libreria.aggiungi_libro(titolo, autore, isbn)

        elif scelta == "2":
            titolo = input("Inserisci il titolo del libro da cercare: ")
            libro_trovato = libreria.cerca_per_titolo(titolo)
            if libro_trovato:
                print(f"\nLibro trovato: {libro_trovato}")
            else:
                print("\nLibro non trovato.")

        elif scelta == "3":
            print("\nUscita dal programma.")
            break

        else:
            print("\nScelta non valida. Riprova.")

# Avvia il menu solo se esegui questo file direttamente
if __name__ == "__main__":
    menu()
