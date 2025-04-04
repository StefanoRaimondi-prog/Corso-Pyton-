def saluta_decoratore(funzione_originale):
    def nuova_funzione():
        print("Ciao! Sto per eseguire la funzione...")
        funzione_originale()
        print("Funzione eseguita. Arrivederci!")
    return nuova_funzione

# Applichiamo il decoratore con la chiocciola
@saluta_decoratore
def di_cose():
    print("Sto facendo qualcosa...")

# Ora eseguiamo la funzione decorata
di_cose()
