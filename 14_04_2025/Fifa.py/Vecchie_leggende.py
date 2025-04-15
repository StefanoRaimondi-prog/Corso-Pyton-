class Allenatore:
    def __init__(self, nome, impatto):
        self.nome = nome
        self.impatto = impatto  # valore che influenza la potenza dei giocatori

class Giocatore:
    def __init__(self, nome, potenza_base):
        self.nome = nome
        self.potenza_base = potenza_base
        self.gol = 0

    def potenza_reale(self, impatto_allenatore):
        return self.potenza_base + impatto_allenatore

class SquadraVecchieLeggende:
    def __init__(self):
        self.nome = "Vecchie Leggende"
        self.allenatore = Allenatore("Arrigo Sacchi", 5)
        self.giocatori = [
            Giocatore("Pelé", 90),
            Giocatore("Maradona", 92),
            Giocatore("Cruyff", 88),
            Giocatore("Beckenbauer", 87),
            Giocatore("Zidane", 89)
        ]
