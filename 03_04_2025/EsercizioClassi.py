class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Il punto è stato spostato a: ({self.x}, {self.y})")

    def distanza_da_origine(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# --- Programma principale interattivo ---
# Coordinate iniziali del punto
p = Punto(0, 0)
print(f"Punto iniziale: ({p.x}, {p.y})")

# Richiesta all'utente dei valori di spostamento
dx = int(input("Inserisci quanto vuoi spostare in x (dx): "))
dy = int(input("Inserisci quanto vuoi spostare in y (dy): "))

# Spostamento del punto
p.muovi(dx, dy)

# Distanza dall'origine dopo lo spostamento
print("Distanza dall'origine:", p.distanza_da_origine())
