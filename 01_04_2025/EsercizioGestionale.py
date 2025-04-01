class Gestionale:
    def __init__(self):
        self.numero = self.chiedi_numero()

    def chiedi_numero(self):
        while True:
            try:
                numero = int(input("Inserisci un numero: "))
                if numero > 0:
                    return numero
                else:
                    print("Il numero deve essere maggiore di 0.")
            except ValueError:
                print("Inserisci un numero valido.")

# Creiamo un'istanza della classe per eseguire il codice
gestione = Gestionale()
print(f"Hai inserito il numero: {gestione.numero}")
