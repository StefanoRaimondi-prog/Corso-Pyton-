class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        self.__titolare = None
        self.__saldo = 0.0
        self.set_titolare(titolare)
        self.__saldo = saldo_iniziale if saldo_iniziale >= 0 else 0.0

    # Getter per il titolare
    def get_titolare(self):
        return self.__titolare

    # Setter per il titolare con validazione
    def set_titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
        else:
            raise ValueError("Il titolare deve essere una stringa non vuota.")

    # Metodo per visualizzare il saldo
    def visualizza_saldo(self):
        return self.__saldo

    # Metodo per depositare
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
        else:
            raise ValueError("L'importo del deposito deve essere positivo.")

    # Metodo per prelevare
    def preleva(self, importo):
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
            else:
                raise ValueError("Fondi insufficienti per il prelievo.")
        else:
            raise ValueError("L'importo del prelievo deve essere positivo.")

conto = ContoBancario("Mirko Ruffy", 100.0)

print("Titolare:", conto.get_titolare())
print("Saldo iniziale:", conto.visualizza_saldo())

conto.deposita(50)
print("Saldo dopo deposito:", conto.visualizza_saldo())

conto.preleva(30)
print("Saldo dopo prelievo:", conto.visualizza_saldo())

# conto.set_titolare("")  # Questo solleverebbe un ValueError
