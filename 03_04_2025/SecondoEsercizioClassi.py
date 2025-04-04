class Libro():
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def descrizione(self):
        print(f"'{self.titolo}' di {self.autore}, pubblicato nel {self.anno_pubblicazione}.")
        
libro1 = Libro("Il Nome della Rosa", "Umberto Eco", 1980)
libro1.descrizione()

libro2 = Libro("1984", "George Orwell", 1949)
libro2.descrizione()

libro3 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954)
libro3.descrizione()

