from Vecchie_leggende import Giocatore, Allenatore

class SquadraNuoveLeggende:
    def __init__(self):
        self.nome = "Nuove Leggende"
        self.allenatore = Allenatore("Pep Guardiola", 4)
        self.giocatori = [
            Giocatore("Messi", 91),
            Giocatore("Cristiano Ronaldo", 90),
            Giocatore("Mbappé", 89),
            Giocatore("Haaland", 88),
            Giocatore("Salah", 87)
        ]
