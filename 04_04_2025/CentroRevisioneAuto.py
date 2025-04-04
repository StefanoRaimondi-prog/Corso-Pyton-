class Centro_Revisione_Auto:
    # Classe per gestire il centro di revisione auto

    def __init__(self):
        # Inizializza la lista dei clienti
        self.clienti = []

    def inserimento_cliente(self, cliente):
        # Metodo per inserire un nuovo cliente
        for i in self.clienti:
            if i.cf == cliente.cf:
                # Controlla se il cliente esiste già
                print("Impossibile aggiungere utente, già esistente.")
                return
        # Aggiunge il cliente alla lista
        self.clienti.append(cliente)
        print("\nUtente aggiunto con successo.")
        # Avvia il menu di gestione per il cliente
        self.menu_gestione_cliente(cliente)

    def elimina_cliente(self, cf):
        # Metodo per eliminare un cliente tramite codice fiscale
        for i in self.clienti:
            if i.cf == cf:
                # Rimuove il cliente se trovato
                self.clienti.remove(i)
                print("\nUtente eliminato con successo.")
                return
        # Messaggio se il cliente non è trovato
        print("Impossibile eliminare utente, poiché non presente.")

    def modifica_cliente(self, cf):
        # Metodo per modificare i dati di un cliente
        for i in self.clienti:
            if i.cf == cf:
                # Menu per modificare i campi del cliente
                while True:
                    print("\n--- Menu Modifica Cliente ---")
                    scelta = int(input(
                        "Inserisci il campo da modificare:\n"
                        "1. Cognome\n"
                        "2. Codice Fiscale\n"
                        "3. Numero Telefono\n"
                        "4. Data Scadenza\n"
                        "5. Nome\n"
                        "0. Esci\n> "
                    ))

                    # Modifica il campo selezionato
                    if scelta == 1:
                        i.cognome = input("Inserisci nuovo cognome: ")
                    elif scelta == 2:
                        i.cf = input("Inserisci nuovo codice fiscale: ")
                    elif scelta == 3:
                        i.numero = input("Inserisci nuovo numero: ")
                    elif scelta == 4:
                        i.data_scadenza = input("Inserisci nuova data scadenza: ")
                    elif scelta == 5:
                        i.nome = input("Inserisci nuovo nome: ")
                    elif scelta == 0:
                        break
                    else:
                        print("Scelta non valida.")
                    print("Modifica effettuata.\n")
                return
        # Messaggio se il cliente non è trovato
        print("Cliente non trovato.")

    def stampa_dati(self):
        # Metodo per stampare i dati di tutti i clienti
        if not self.clienti:
            print("Nessun cliente registrato.")
            return
        for c in self.clienti:
            # Stampa i dettagli di ogni cliente
            print(f"\nCliente: {c.nome} {c.cognome}")
            print(f"Auto: {c.auto}, Revisione entro: {c.data_scadenza}")
            print(f"Stato: {c.stato}")
            print(f"Contatto: {c.numero}, CF: {c.cf}")

    def menu_gestione_cliente(self, cliente):
        # Menu per gestire la revisione di un cliente
        print(f"\n--- Gestione Revisione per {cliente.nome} {cliente.cognome} ---")
        scelta = input("Vuoi procedere con la revisione? (s/n): ").strip().lower()
        if scelta == 's':
            # Procede con la revisione
            print("Il costo della revisione è di 78.75€.")  # prezzo fisso
            pagamento = input("Metodo di pagamento (bancomat/contanti): ").strip().lower()
            if pagamento in ['bancomat', 'contanti']:
                # Aggiorna lo stato del cliente
                cliente.stato = "Revisione completata"
                print(f"Pagamento effettuato con {pagamento}. Revisione completata con successo.")
            else:
                print("Metodo di pagamento non valido. Revisione non completata.")
        else:
            print("Revisione non eseguita. Cliente in attesa.")


class Cliente:
    # Classe per rappresentare un cliente
    def __init__(self):
        # Inizializza i dati del cliente
        self.nome = input("Inserisci il nome: ")
        self.cognome = input("Inserisci il cognome: ")
        self.numero = input("Inserisci il numero di telefono: ")
        self.cf = input("Inserisci il codice fiscale: ")
        self.data_scadenza = input("Inserisci la data di scadenza della revisione (gg/mm/aaaa): ")
        self.auto = input("Inserisci il modello dell'auto: ")
        self.stato = "In attesa di revisione"


# --- Funzioni utente ---

def inserimento_cliente(revisione):
    # Funzione per inserire nuovi clienti
    continua = True
    while continua:
        nuovo = Cliente()
        revisione.inserimento_cliente(nuovo)
        risp = input("Vuoi inserire ancora clienti? (s/n): ").strip().lower()
        if risp == "n" or risp == "no":
            continua = False

def modifica(revisione):
    # Funzione per modificare un cliente
    cf = input("Inserisci codice fiscale del cliente da modificare: ")
    revisione.modifica_cliente(cf)

def elimina(revisione):
    # Funzione per eliminare un cliente
    cf = input("Inserisci codice fiscale del cliente da eliminare: ")
    revisione.elimina_cliente(cf)

# --- Programma principale ---

def main():
    # Funzione principale del programma
    sistema_attivo = True
    while sistema_attivo:
        try:
            # Menu principale
            scelta = int(input("CIAO, BENVENUTO. SCEGLI UN'OPZIONE:\n1. ADMIN\n2. CLIENTE\nAltro per uscire\n> "))
        except ValueError:
            print("Input non valido.")
            continue

        match scelta:
            case 1:
                # Menu ADMIN
                centro = Centro_Revisione_Auto()
                while True:
                    print("\n--- Menu ADMIN ---")
                    print("1. Inserisci nuovo cliente")
                    print("2. Stampa clienti")
                    print("3. Torna indietro")
                    admin_scelta = input("Scegli un'opzione: ")

                    if admin_scelta == "1":
                        inserimento_cliente(centro)
                    elif admin_scelta == "2":
                        centro.stampa_dati()
                    elif admin_scelta == "3":
                        break
                    else:
                        print("Scelta non valida.")

            case 2:
                # Menu CLIENTE
                centro = Centro_Revisione_Auto()
                attivo = True
                while attivo:
                    try:
                        scelta_cliente = int(input("CIAO, SCEGLI UN'OPZIONE:\n1. Inserimento cliente\n2. Modifica\n3. Elimina\n4. Stampa\nAltro per uscire\n> "))
                    except ValueError:
                        print("Input non valido.")
                        continue

                    match scelta_cliente:
                        case 1:
                            inserimento_cliente(centro)
                        case 2:
                            modifica(centro)
                        case 3:
                            elimina(centro)
                        case 4:
                            centro.stampa_dati()
                        case _:
                            print("Uscita dal menu CLIENTE.")
                            attivo = False

            case _:
                # Uscita dal sistema
                print("Uscita dal sistema.")
                sistema_attivo = False

# Avvio del programma
main()
