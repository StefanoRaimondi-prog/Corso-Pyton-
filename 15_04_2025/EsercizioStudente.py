class Persona:
    # Classe base che rappresenta una persona con nome ed età
    def __init__(self, nome, eta):
        # Inizializza i dati privati nome ed età
        self.__nome = nome
        self.__eta = eta

    def get_nome(self):
        # Restituisce il nome della persona
        return self.__nome

    def set_nome(self, nuovo_nome):
        # Modifica il nome della persona se è una stringa non vuota
        if isinstance(nuovo_nome, str) and nuovo_nome.strip():
            self.__nome = nuovo_nome
        else:
            raise ValueError("Il nome deve essere una stringa non vuota.")

    def get_eta(self):
        # Restituisce l'età della persona
        return self.__eta

    def set_eta(self, nuova_eta):
        # Modifica l'età della persona se è un intero positivo
        if isinstance(nuova_eta, int) and nuova_eta > 0:
            self.__eta = nuova_eta
        else:
            raise ValueError("L'età deve essere un intero positivo.")

    def presentazione(self):
        # Restituisce una stringa di presentazione della persona
        return f"Ciao, sono {self.__nome} e ho {self.__eta} anni."


class Studente(Persona):
    # Classe derivata che rappresenta uno studente, estende Persona
    def __init__(self, nome, eta, voti):
        # Inizializza i dati dello studente, inclusi i voti
        super().__init__(nome, eta)
        self.__voti = voti

    def calcola_media(self):
        # Calcola e restituisce la media dei voti dello studente
        if self.__voti:
            return sum(self.__voti) / len(self.__voti)
        return 0

    def presentazione(self):
        # Restituisce una stringa di presentazione dello studente, includendo la media dei voti
        media = self.calcola_media()
        return f"{super().presentazione()} Sono uno studente con una media di {media:.2f}."


class Professore(Persona):
    # Classe derivata che rappresenta un professore, estende Persona
    def __init__(self, nome, eta, materia):
        # Inizializza i dati del professore, inclusa la materia insegnata
        super().__init__(nome, eta)
        self.__materia = materia

    def presentazione(self):
        # Restituisce una stringa di presentazione del professore, includendo la materia insegnata
        return f"{super().presentazione()} Insegno {self.__materia}."


# =======================
#        MENU
# =======================
def menu():
    # Funzione principale che gestisce il menu del programma
    persone = []  # Lista per memorizzare oggetti Persona, Studente e Professore

    while True:
        # Mostra il menu principale
        print("\n====== MENU ======")
        print("1. Aggiungi Studente")
        print("2. Aggiungi Professore")
        print("3. Visualizza tutte le persone")
        print("4. Calcola media di uno studente")
        print("5. Modifica nome/età di una persona")
        print("6. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            # Aggiungi un nuovo studente
            nome = input("Nome studente: ")
            eta = int(input("Età studente: "))
            voti_str = input("Inserisci i voti separati da virgola (es. 8,7,9): ")
            voti = [int(v) for v in voti_str.split(",") if v.strip().isdigit()]  # Converte i voti in una lista di interi
            studente = Studente(nome, eta, voti)
            persone.append(studente)  # Aggiunge lo studente alla lista
            print("Studente aggiunto con successo!")

        elif scelta == "2":
            # Aggiungi un nuovo professore
            nome = input("Nome professore: ")
            eta = int(input("Età professore: "))
            materia = input("Materia insegnata: ")
            professore = Professore(nome, eta, materia)
            persone.append(professore)  # Aggiunge il professore alla lista
            print("Professore aggiunto con successo!")

        elif scelta == "3":
            # Visualizza tutte le persone nella lista
            print("\n--- Presentazioni ---")
            for persona in persone:
                print(persona.presentazione())  # Chiama il metodo presentazione per ogni persona

        elif scelta == "4":
            # Calcola la media dei voti di uno studente specifico
            nome = input("Inserisci il nome dello studente: ")
            trovato = False
            for persona in persone:
                if isinstance(persona, Studente) and persona.get_nome().lower() == nome.lower():
                    # Se la persona è uno studente e il nome corrisponde
                    print(f"La media voti di {nome} è {persona.calcola_media():.2f}")
                    trovato = True
                    break
            if not trovato:
                print("Studente non trovato.")

        elif scelta == "5":
            # Modifica il nome o l'età di una persona
            nome = input("Nome della persona da modificare: ")
            for persona in persone:
                if persona.get_nome().lower() == nome.lower():
                    # Se il nome corrisponde, consente di modificare i dati
                    nuovo_nome = input("Nuovo nome (premi INVIO per lasciare invariato): ")
                    nuova_eta_str = input("Nuova età (premi INVIO per lasciare invariata): ")
                    if nuovo_nome.strip():
                        persona.set_nome(nuovo_nome)  # Modifica il nome
                    if nuova_eta_str.strip():
                        persona.set_eta(int(nuova_eta_str))  # Modifica l'età
                    print("Dati aggiornati con successo.")
                    break
            else:
                print("Persona non trovata.")

        elif scelta == "6":
            # Esce dal programma
            print("Uscita dal programma. Arrivederci!")
            break

        else:
            # Gestisce input non validi
            print("Scelta non valida. Riprova.")
