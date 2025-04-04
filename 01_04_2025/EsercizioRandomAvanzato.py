print("scegli un numero da 1 a 100")
n = int(input())
if n <= 0:
    print("Per favore inserisci un numero positivo.")
else:
    a, b = 0, 1
    print("Sequenza di Fibonacci:")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
