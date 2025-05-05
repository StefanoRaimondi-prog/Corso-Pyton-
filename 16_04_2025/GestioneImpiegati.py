from abc import ABC, abstractmethod

class Impiegato(ABC):
    @abstractmethod
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio

    @abstractmethod
    def Stipendio_base(self):
        pass

    def stampa_informazioni(self):
        print(f"Nome: {self.nome}, Cognome: {self.cognome}, Stipendio: {self.stipendio}")
        print(f"Stipendio base: {self.Stipendio_base()}")
        print(f"Tipo di impiegato: {self.__class__.__name__}")


class Impiegato_fisso(Impiegato):
    def __init__(self, nome, cognome, stipendio):
        super().__init__(nome, cognome, stipendio)

    def Stipendio_base(self):
        return self.stipendio

class Impiegato_provvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio, provvigione):
        super().__init__(nome, cognome, stipendio)
        self.provvigione = provvigione

    def Stipendio_base(self):
        return self.stipendio + self.provvigione

# Lista degli impiegati
impiegati = []

# Menù
def menu():
    while True:
        print("\n--- GESTIONE IMPIEGATI ---")
        print("1. Aggiungi impiegato fisso")
        print("2. Aggiungi impiegato a provvigione")
        print("3. Visualizza tutti gli impiegati")
        print("4. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            stipendio = float(input("Stipendio: "))
            impiegati.append(Impiegato_fisso(nome, cognome, stipendio))
            print(" Impiegato fisso aggiunto.")
        
        elif scelta == "2":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            stipendio = float(input("Stipendio fisso: "))
            provvigione = float(input("Provvigione: "))
            impiegati.append(Impiegato_provvigione(nome, cognome, stipendio, provvigione))
            print(" Impiegato a provvigione aggiunto.")
        
        elif scelta == "3":
            if not impiegati:
                print(" Nessun impiegato registrato.")
            else:
                print("\n--- LISTA IMPIEGATI ---")
                for i, imp in enumerate(impiegati, start=1):
                    print(f"{i})")
                    imp.stampa_informazioni()
        
        elif scelta == "4":
            print(" Uscita dal programma.")
            break
        else:
            print(" Scelta non valida. Riprova.")

# Avvio del menù
menu()