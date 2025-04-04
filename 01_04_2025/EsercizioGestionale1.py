# 1. Chiedere un numero positivo all'utente
while True:
    try:
        n = int(input("Inserisci un numero intero positivo: "))
        if n > 0:
            break
        else:
            print("Il numero deve essere maggiore di 0.")
    except ValueError:
        print("Inserisci un numero valido.")

# 2. Calcolare la somma dei numeri pari da 1 a n
somma_pari = sum(i for i in range(2, n+1, 2))
print(f"La somma dei numeri pari da 1 a {n} è: {somma_pari}")

# 3. Stampare tutti i numeri dispari da 1 a n
numeri_dispari = [i for i in range(1, n+1, 2)]
print(f"I numeri dispari da 1 a {n} sono: {numeri_dispari}")

# 4. Verificare se n è un numero primo
def è_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

if è_primo(n):
    print(f"{n} è un numero primo.")
else:
    print(f"{n} non è un numero primo.")