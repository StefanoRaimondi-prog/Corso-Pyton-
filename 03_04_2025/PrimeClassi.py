class Automobile:
    numero_di_ruote = 4
# init è il costruttore della classe
    def __init__(self, marca, modello, anno):
        """
        Costruttore della classe Automobile.
        
        """
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def stamp_info(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")



Auto1 = Automobile("Fiat", "Panda", 2020)
Auto2 = Automobile("Ford", "Fiesta", 2019)


class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b

# Ora siamo fuori dalla classe: tutto funziona
risultato = Calcolatrice.somma(2, 3)
print(risultato)



class Contatore:
    numero_di_istanze = 0

    def __init__(self):
        Contatore.numero_di_istanze += 1

    @classmethod
    def mostra_numero_istanze(cls):
        return cls.numero_di_istanze

# Fuori dalla classe
C1 = Contatore()
C2 = Contatore()

print(Contatore.mostra_numero_istanze())  # Output: 2
