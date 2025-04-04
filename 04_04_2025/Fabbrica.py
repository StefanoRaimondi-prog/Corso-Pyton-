class Prodotto:
    def __init__(self, nome, prezzo, quantita, costo):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        self.prezzo_totale = prezzo * quantita
        self.costo = costo

    def aggiorna_totale(self):
        self.prezzo_totale = self.prezzo * self.quantita


class Fabbrica:
    def __init__(self, nome, indirizzo, telefono):
        self.nome = nome
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)
        print(f"Prodotto '{prodotto.nome}' aggiunto alla fabbrica '{self.nome}'.")

    def vendi_prodotto(self, prodotto):
        if prodotto.quantita > 0:
            prodotto.quantita -= 1
            prodotto.aggiorna_totale()
            print(f"Prodotto '{prodotto.nome}' venduto. Quantità rimanente: {prodotto.quantita}")
        else:
            print(f"Prodotto '{prodotto.nome}' esaurito.")

    def reso_prodotto(self, prodotto):
        prodotto.quantita += 1
        prodotto.aggiorna_totale()
        print(f"Prodotto '{prodotto.nome}' restituito. Quantità attuale: {prodotto.quantita}")


# Creo un oggetto iniziale da usare
accendino = Prodotto("Accendino", 2.5, 3, 2.0)
fabbrica = Fabbrica("Fiamma S.r.l.", "Via del Fuoco 12", "123456789")
fabbrica.aggiungi_prodotto(accendino)
fabbrica.vendi_prodotto(accendino)
fabbrica.reso_prodotto(accendino)


class Menu:
    def __init__(self, fabbrica):
        self.fabbrica = fabbrica
        self.avvia_menu()

    def avvia_menu(self):
        while True:
            print("\n--- Menu ---")
            print("1. Aggiungi Prodotto")
            print("2. Vendi Prodotto")
            print("3. Restituisci Prodotto")
            print("4. Esci")

            scelta = input("Inserisci la tua scelta: ")

            if scelta == "1":
                nome = input("Nome prodotto: ")
                prezzo = float(input("Prezzo unitario: "))
                quantita = int(input("Quantità: "))
                costo = float(input("Costo unitario: "))
                prodotto = Prodotto(nome, prezzo, quantita, costo)
                self.fabbrica.aggiungi_prodotto(prodotto)

            elif scelta == "2":
                nome = input("Nome del prodotto da vendere: ")
                prodotto = self.trova_prodotto(nome)
                if prodotto:
                    self.fabbrica.vendi_prodotto(prodotto)
                else:
                    print("Prodotto non trovato.")

            elif scelta == "3":
                nome = input("Nome del prodotto da restituire: ")
                prodotto = self.trova_prodotto(nome)
                if prodotto:
                    self.fabbrica.reso_prodotto(prodotto)
                else:
                    print("Prodotto non trovato.")

            elif scelta == "4":
                print("Arrivederci!")
                break

            else:
                print("Scelta non valida. Riprova.")

    def trova_prodotto(self, nome):
        for prodotto in self.fabbrica.prodotti:
            if prodotto.nome.lower() == nome.lower():
                return prodotto
        return None


# Avvio il menu
menu = Menu(fabbrica)
