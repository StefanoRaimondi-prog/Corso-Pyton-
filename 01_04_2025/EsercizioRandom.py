import random
def gioco(): 
    range = 1, 100
    numero_utente = int(input("Scegli un numero da 1 a 100: "))
    numero_segretissimo = random.randint(*range)
    if numero_utente == numero_segretissimo:
        print("Il numero è corretto")
    else:
        print("Il numero non è corretto")
        print("Riprova")
        print("Il numero segretissimo era:", numero_segretissimo)
        def suggerimento(numero_utente, numero_segretissimo):
            if numero_utente < numero_segretissimo:
                print("Il prossimo numero dovrebbe essere maggiore.")
            else:
                print("Il prossimo numero dovrebbe essere minore.")

        suggerimento(numero_utente, numero_segretissimo)

while True:
    
    
   gioco()
   break

