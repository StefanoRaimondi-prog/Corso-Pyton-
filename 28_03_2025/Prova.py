def somma(a, b):
    return a + b

if __name__ == "__main__":
    print("Benvenuto nel mio programma Python!")
    numero1 = int(input("Inserisci il primo numero: "))
    numero2 = int(input("Inserisci il secondo numero: "))
    risultato = somma(numero1, numero2)
    print(f"La somma di {numero1} e {numero2} è: {risultato}")