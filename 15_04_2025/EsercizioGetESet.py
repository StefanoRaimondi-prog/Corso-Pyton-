class Computer:
    def __init__(self):
        self.__processore = "Intel i5"
        
    def get_processore(self):
        return self.__processore

    def set_processore(self, processore):
        self.__processore = processore
    
pc = Computer()
print(pc.get_processore())  # Stampa "Intel i5"

pc.set_processore("AMD Ryzen 5")
print(pc.get_processore())  # Stampa "AMD Ryzen 5"