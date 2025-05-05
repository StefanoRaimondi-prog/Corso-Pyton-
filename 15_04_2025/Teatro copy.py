class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già occupato.")

    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} liberato.")
        else:
            print(f"Posto {self._fila}{self._numero} non era prenotato.")

    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def is_occupato(self):
        return self._occupato

    def __str__(self):
        stato = "Occupato" if self._occupato else "Libero"
        return f"Posto {self._fila}{self._numero} - {stato}"

class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto VIP {self._fila}{self._numero} prenotato con servizi: {', '.join(self.servizi_extra)}")
        else:
            print(f"Posto VIP {self._fila}{self._numero} è già occupato.")

    def __str__(self):
        stato = "Occupato" if self._occupato else "Libero"
        return f"Posto VIP {self._fila}{self._numero} - {stato} - Servizi: {', '.join(self.servizi_extra)}"

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila)
        self.costo = costo

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto Standard {self._fila}{self._numero} prenotato. Costo: €{self.costo}")
        else:
            print(f"Posto Standard {self._fila}{self._numero} è già occupato.")

    def __str__(self):
        stato = "Occupato" if self._occupato else "Libero"
        return f"Posto Standard {self._fila}{self._numero} - {stato} - Costo: €{self.costo}"

class Teatro:
    def __init__(self):
        self._posti = []

    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                return
        print(f"Posto {fila}{numero} non trovato.")

    def libera_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.libera()
                return
        print(f"Posto {fila}{numero} non trovato.")

    def stampa_tutti_posti(self):
        print("\nElenco Completo dei Posti:")
        if not self._posti:
            print("Nessun posto ancora registrato.")
        for posto in self._posti:
            print(posto)

    def stampa_posti_occupati(self):
        print("\nPosti Occupati:")
        trovati = False
        for posto in self._posti:
            if posto.is_occupato():
                print(posto)
                trovati = True
        if not trovati:
            print("Nessun posto risulta occupato.")

# -----------------------------
#       MENU INTERATTIVO
# -----------------------------
def menu_teatro():
    teatro = Teatro()

    while True:
        print("\n======= GESTIONE TEATRO =======")
        print("1. Aggiungi un Posto")
        print("2. Prenota un Posto")
        print("3. Libera un Posto")
        print("4. Visualizza Tutti i Posti")
        print("5. Visualizza Posti Occupati")
        print("6. Esci")
        scelta = input("Seleziona un'opzione (1-6): ")

        if scelta == "1":
            print("\n--- Aggiunta Posto ---")
            tipo = input("Tipo di posto (standard/vip): ").strip().lower()
            try:
                numero = int(input("Numero posto: "))
                fila = input("Lettera fila: ").strip().upper()
                if tipo == "vip":
                    servizi = input("Inserisci servizi extra separati da virgola: ").split(",")
                    servizi = [s.strip() for s in servizi]
                    posto = PostoVIP(numero, fila, servizi)
                elif tipo == "standard":
                    costo = float(input("Costo prenotazione: €"))
                    posto = PostoStandard(numero, fila, costo)
                else:
                    print("Tipo non valido.")
                    continue
                teatro.aggiungi_posto(posto)
                print("Posto aggiunto con successo.")
            except ValueError:
                print("Inserimento dati non valido.")

        elif scelta == "2":
            print("\n--- Prenotazione ---")
            try:
                numero = int(input("Numero posto da prenotare: "))
                fila = input("Lettera fila: ").strip().upper()
                teatro.prenota_posto(numero, fila)
            except ValueError:
                print("Inserimento dati non valido.")

        elif scelta == "3":
            print("\n--- Liberazione ---")
            try:
                numero = int(input("Numero posto da liberare: "))
                fila = input("Lettera fila: ").strip().upper()
                teatro.libera_posto(numero, fila)
            except ValueError:
                print("Inserimento dati non valido.")

        elif scelta == "4":
            teatro.stampa_tutti_posti()

        elif scelta == "5":
            teatro.stampa_posti_occupati()

        elif scelta == "6":
            print("Uscita in corso...")
            break

        else:
            print("Scelta non valida. Riprova.")

# Avvia il menù
menu_teatro()
