class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def __str__(self):
        return f"{self.nome} ({self.specie})"

class Animali:
    def __init__(self):
        self.animali = []

    def aggiungi(self, animale):
        if isinstance(animale, Animale):
            self.animali.append(animale)
        else:
            raise TypeError("Puoi aggiungere solo oggetti di tipo Animale")

    def mostra_tutti(self):
        if not self.animali:
            print("Nessun animale presente.")
        else:
            for animale in self.animali:
                print(animale)

class Giraffa(Animale):
    def __init__(self, nome, altezza):
        super().__init__(nome, "Giraffa")
        self.altezza = altezza

    def __str__(self):
        return f"{super().__str__()} - Altezza: {self.altezza} m"

class Elefante(Animale):
    def __init__(self, nome, peso):
        super().__init__(nome, "Elefante")
        self.peso = peso

    def __str__(self):
        return f"{super().__str__()} - Peso: {self.peso} kg"

# Funzione per mostrare il menu
def mostra_menu():
    print("\n--- Menu Animali ---")
    print("1. Aggiungi Giraffa")
    print("2. Aggiungi Elefante")
    print("3. Mostra tutti gli animali")
    print("4. Esci")

# Avvio programma
zoo = Animali()

while True:
    mostra_menu()
    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input("Inserisci il nome della giraffa: ")
        try:
            altezza = float(input("Inserisci l'altezza (in metri): "))
            zoo.aggiungi(Giraffa(nome, altezza))
            print("Giraffa aggiunta con successo!")
        except ValueError:
            print("Errore: l'altezza deve essere un numero.")

    elif scelta == "2":
        nome = input("Inserisci il nome dell'elefante: ")
        try:
            peso = float(input("Inserisci il peso (in kg): "))
            zoo.aggiungi(Elefante(nome, peso))
            print("Elefante aggiunto con successo!")
        except ValueError:
            print("Errore: il peso deve essere un numero.")

    elif scelta == "3":
        print("\nLista degli animali nello zoo:")
        zoo.mostra_tutti()

    elif scelta == "4":
        print("Uscita dal programma. Arrivederci!")
        break

    else:
        print("Opzione non valida. Riprova.")
