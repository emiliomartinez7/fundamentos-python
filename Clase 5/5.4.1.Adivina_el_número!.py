import random
rng = random.randint(1, 100)

n = int(input("Adivina el número entre 1 y 100: "))
while n != rng:
    if n < rng:
        print("El número secreto es mayor")
    elif n > rng:
        print("El número secreto es menor")
    else:
        print("¡Felicidades! Has adivinado el número secreto")
        break
    n = int(input("Adivina el número entre 1 y 100: "))
