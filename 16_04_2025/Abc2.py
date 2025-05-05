# from abc import ABC, abstractmethod

# class Forma(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimetro(self):
#         pass

# class Rettangolo(Forma):
#     def __init__(self, base, altezza):
#         self.base = base
#         self.altezza = altezza

#     def area(self):
#         return self.base * self.altezza

#     def perimetro(self):
#         return 2 * (self.base + self.altezza)
    
# f = Forma()  # TypeError: Can't instantiate abstract class Forma with abstract methods area, perimetro
# r = Rettangolo(5, 10)

# print(r.area())      # Output: 50
# print(r.perimetro()) # Output: 30   

# FORMA CON OUTPUT SENZA ERRORI

from abc import ABC, abstractmethod

# Classe astratta
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Classe concreta
class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

# Creazione dell'oggetto Rettangolo e stampa dei risultati
r = Rettangolo(5, 10)

print("Area del rettangolo:", r.area())         # Output: 50
print("Perimetro del rettangolo:", r.perimetro())  # Output: 30
