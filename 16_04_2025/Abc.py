from abc import ABC, abstractmethod

class Animale (ABC):
    @abstractmethod
    def muovi(self):
        pass

class Cane(Animale):
    def muovi(self):
        print("Il cane corre")
        
class Pesce(Animale):
    def muovi(self):
        print("Il pesce nuota")

def fai_muovere(animale: Animale):
    animale.muovi()

fai_muovere(Cane())   # Output: Il cane corre
fai_muovere(Pesce())  # Output: Il pesce nuota