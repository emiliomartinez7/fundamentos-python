
n = int(input("Ingresa un número: "))
suma = n
datos = []

print(f"Proceso de reducción para: {n}")
while suma >= 10:
    num = [int(d) for d in str(suma)]
    digit =suma
    suma = sum(num)
    datos.append(suma)
    print(f"{digit} = {suma}")
print("el resultado final es:", suma)