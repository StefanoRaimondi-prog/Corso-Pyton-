class MetodoPagamento:
    # Classe base per i metodi di pagamento
    def __init__(self):
        pass

    def effettua_pagamento(self, importo):
        # Metodo astratto da implementare nelle sottoclassi
        raise NotImplementedError("Devi implementare effettua_pagamento nelle sottoclassi.")

class Bancomat(MetodoPagamento):
    # Classe per il metodo di pagamento Bancomat
    def __init__(self, numero_carta, nome_intestatario, data_scadenza, cvv):
        super().__init__()
        self.numero_carta = numero_carta
        self.nome_intestatario = nome_intestatario
        self.data_scadenza = data_scadenza
        self.cvv = cvv

    def effettua_pagamento(self, importo):
        # Implementazione del pagamento tramite Bancomat
        print(f"[Bancomat] Pagamento di €{importo} effettuato con la carta {self.numero_carta}.")

    def __str__(self):
        # Rappresentazione testuale del metodo Bancomat
        return f"Bancomat - Intestatario: {self.nome_intestatario}, Carta: {self.numero_carta}"

class PayPal(MetodoPagamento):
    # Classe per il metodo di pagamento PayPal
    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password

    def effettua_pagamento(self, importo):
        # Implementazione del pagamento tramite PayPal
        print(f"[PayPal] Pagamento di €{importo} effettuato tramite l'account {self.email}.")

    def __str__(self):
        # Rappresentazione testuale del metodo PayPal
        return f"PayPal - Email: {self.email}"

class Bonifico(MetodoPagamento):
    # Classe per il metodo di pagamento Bonifico
    def __init__(self, iban, intestatario, importo_disponibile):
        super().__init__()
        self.iban = iban
        self.intestatario = intestatario
        self.importo_disponibile = importo_disponibile

    def effettua_pagamento(self, importo):
        # Implementazione del pagamento tramite Bonifico
        if importo <= self.importo_disponibile:
            print(f"[Bonifico] Pagamento di €{importo} effettuato da {self.intestatario} all'IBAN {self.iban}.")
            self.importo_disponibile -= importo
        else:
            print(f"[Bonifico] Fondi insufficienti: disponibili €{self.importo_disponibile}, richiesti €{importo}.")

    def __str__(self):
        # Rappresentazione testuale del metodo Bonifico
        return f"Bonifico - Intestatario: {self.intestatario}, IBAN: {self.iban}, Disponibili: €{self.importo_disponibile}"

class GestorePagamento:
    # Classe per gestire i metodi di pagamento
    def __init__(self):
        self.metodi = []

    def aggiungi_metodo(self, metodo):
        # Aggiunge un metodo di pagamento alla lista
        self.metodi.append(metodo)

    def mostra_metodi(self):
        # Mostra tutti i metodi di pagamento salvati
        for idx, metodo in enumerate(self.metodi):
            print(f"{idx + 1}. {metodo}")

    def esegui_pagamento(self, indice, importo):
        # Esegue il pagamento utilizzando il metodo selezionato
        if 0 <= indice < len(self.metodi):
            self.metodi[indice].effettua_pagamento(importo)
        else:
            print("Metodo non valido.")


# =======================
#          MENU
# =======================
def menu():
    # Funzione principale per gestire il menu
    gestore = GestorePagamento()
    while True:
        print("\n--- MENU GESTORE PAGAMENTI ---")
        print("1. Aggiungi metodo di pagamento")
        print("2. Visualizza metodi di pagamento")
        print("3. Effettua un pagamento")
        print("4. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            # Aggiungi un nuovo metodo di pagamento
            print("\n--- Aggiungi Metodo ---")
            print("a. Bancomat")
            print("b. PayPal")
            print("c. Bonifico")
            tipo = input("Scegli il tipo (a/b/c): ")

            if tipo == "a":
                # Aggiungi un metodo Bancomat
                num = input("Numero carta: ")
                nome = input("Intestatario: ")
                data = input("Data scadenza: ")
                cvv = input("CVV: ")
                gestore.aggiungi_metodo(Bancomat(num, nome, data, cvv))
                print("Bancomat aggiunto.")
            elif tipo == "b":
                # Aggiungi un metodo PayPal
                email = input("Email: ")
                pw = input("Password: ")
                gestore.aggiungi_metodo(PayPal(email, pw))
                print("PayPal aggiunto.")
            elif tipo == "c":
                # Aggiungi un metodo Bonifico
                iban = input("IBAN: ")
                intestatario = input("Intestatario: ")
                disponibile = float(input("Importo disponibile: "))
                gestore.aggiungi_metodo(Bonifico(iban, intestatario, disponibile))
                print("Bonifico aggiunto.")
            else:
                print("Tipo non valido.")

        elif scelta == "2":
            # Visualizza i metodi di pagamento salvati
            print("\n--- Metodi Salvati ---")
            if gestore.metodi:
                gestore.mostra_metodi()
            else:
                print("Nessun metodo disponibile.")

        elif scelta == "3":
            # Effettua un pagamento
            if not gestore.metodi:
                print("Non ci sono metodi disponibili.")
                continue
            print("\n--- Scegli metodo per pagare ---")
            gestore.mostra_metodi()
            try:
                idx = int(input("Numero metodo: ")) - 1
                importo = float(input("Importo da pagare: "))
                gestore.esegui_pagamento(idx, importo)
            except ValueError:
                print("Input non valido.")

        elif scelta == "4":
            # Esci dal programma
            print("Uscita in corso...")
            break
        else:
            print("Scelta non valida.")


# Avvia il menu
menu()
