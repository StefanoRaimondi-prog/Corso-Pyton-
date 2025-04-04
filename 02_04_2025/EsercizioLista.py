import random  # Importa il modulo random per generare numeri casuali

# Funzione che calcola il quadrato di un numero
def quadrato(numero):
    return numero * numero

# Dizionario per memorizzare i numeri inseriti dall'utente e i loro quadrati
Lista = {}

# Chiede all'utente di inserire un numero e calcola il suo quadrato
input_utente1 = int(input("Inserisci un numero: "))
Lista[input_utente1] = quadrato(input_utente1)

# Chiede all'utente di inserire un altro numero e calcola il suo quadrato
input_utente2 = int(input("Inserisci un altro numero: "))
Lista[input_utente2] = quadrato(input_utente2)

# Funzione che calcola la somma dei quadrati dei numeri in un dizionario
def somma(lista):
    somma_quadrati = 0
    # Itera sui numeri e i loro quadrati nel dizionario
    for numero, quadrato in lista.items():
        print(f"Il quadrato di {numero} è {quadrato}")
        somma_quadrati += quadrato  # Somma i quadrati
    print(f"La somma dei quadrati è {somma_quadrati}")

# Chiama la funzione somma per calcolare e stampare la somma dei quadrati
somma(Lista)

# Funzione che genera una lista di n numeri casuali tra 1 e 100
def random_list(n):
    return [random.randint(1, 100) for _ in range(n)]

# Chiede all'utente di inserire un numero per generare una lista casuale
input_utente3 = int(input("Inserisci un numero per generare una lista casuale: "))
lista_casuale = random_list(input_utente3)
print(f"Lista casuale di {input_utente3} numeri: {lista_casuale}")

# Eleva a potenza tutti i numeri della lista casuale usando la funzione quadrato
lista_potenze = [quadrato(numero) for numero in lista_casuale]
print(f"Lista dei quadrati dei numeri casuali: {lista_potenze}")

def probabilita(lista):
    # Calcola la probabilità di ogni numero nella lista
    probabilita = {numero: lista.count(numero) / len(lista) for numero in set(lista)}
    return probabilita
# Calcola e stampa la probabilità di ogni numero nella lista casuale
probabilita_lista = probabilita(lista_casuale)
print("Probabilità di ogni numero nella lista casuale:", probabilita_lista)