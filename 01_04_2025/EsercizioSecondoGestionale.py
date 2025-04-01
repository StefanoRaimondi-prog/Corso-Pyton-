import random

def chiedi_numero():
    while True:
        try:
            n = int(input("Inserisci un numero intero positivo: "))
            if n > 0:
                return n
            else:
                print("Errore: il numero deve essere positivo.")
        except ValueError:
            print("Errore: inserisci un numero valido.")

# Funzione per determinare se un numero è primo
def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 1. Chiedere all'utente un numero positivo
n = chiedi_numero()

# 2. Generare una lista di n numeri casuali tra 1 e n
lista_numeri = [random.randint(1, n) for _ in range(n)]
print(f"Lista generata: {lista_numeri}")

# 3. Calcolare la somma dei numeri pari
somma_pari = sum(num for num in lista_numeri if num % 2 == 0)
print(f"Somma dei numeri pari: {somma_pari}")

# 4. Stampare i numeri dispari
numeri_dispari = [num for num in lista_numeri if num % 2 != 0]
print(f"Numeri dispari nella lista: {numeri_dispari}")

# 5. Stampare i numeri primi nella lista
numeri_primi = [num for num in lista_numeri if is_primo(num)]
print(f"Numeri primi nella lista: {numeri_primi}")

# 6. Verificare se la somma di tutti i numeri nella lista è un numero primo
somma_totale = sum(lista_numeri)
print(f"Somma totale della lista: {somma_totale}")
if is_primo(somma_totale):
    print("La somma di tutti i numeri nella lista è un numero primo.")
else:
    print("La somma di tutti i numeri nella lista NON è un numero primo.")
