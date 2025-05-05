class Animale():
    def emetti_suono(self):
        print("L'animale emette un suono")

class Cane(Animale):
    def emetti_suono(self):
        print("Il cane abbaia")

class Gatto(Animale):
    def emetti_suono(self):
        print("Il gatto miagola")

class Pippo():
    def emetti_suono(self):
        print("Il pippo fa un suono strano")

def fai_emettere_suono(animale):
    animale.emetti_suono()

# Creazione delle istanze
cane = Cane()
gatto = Gatto()
pippo = Pippo()

# Uso diretto
cane.emetti_suono()   # Output: Il cane abbaia
gatto.emetti_suono()  # Output: Il gatto miagola
pippo.emetti_suono()  # Output: Il pippo fa un suono strano

# Uso della funzione polimorfica
fai_emettere_suono(cane)
fai_emettere_suono(gatto)
fai_emettere_suono(pippo)
