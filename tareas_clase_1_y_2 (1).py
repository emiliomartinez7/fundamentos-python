# -*- coding: utf-8 -*-
"""
Clase:        1 Y 2
Tema:         Tipo de variables y Bloques comparativos
Ejercicio:    1.3.1 -- 1.3.2 -- 1.4.1 --1.4.3 -- 2.3.1 -- 2.3.2 -- 2.4.1 -- 2.4.2 -- 2.5.1 --2.5.1
Descripción:  Calculo de la propina, generador de correos key, Contraseña segura, calculo de impuestos, El numero magico, Año bisiesto, Elevaor logico

Autor:        Emilo Josue Martinez Aguiera
Fecha:        2025-05-22
Estado:       [Terminado]
"""
#1.3.1. Automatizando el cálculo de la propina
total = float(input("Ingrese el balor de su cuneta"))
p = float(input("que porcentaje de propina quiere?"))
porcentaje = (total*p)/100
print(f"La propina es {porcentaje}")
total_a_pagar = total + porcentaje
print(f"El total a pagar es {total_a_pagar}")

#1.3.2. Generador del correo de Key
nombre = input("Ingrese su nombre completo")
nombre = nombre.lower()
nombre = nombre.split()

print(f"Su nombre es {nombre[0]}.{nombre[2]}@keyinstitute.edu.sv")

#1.4.1. División con Precisión
a,b,k = (1,3,1000)
div = str(a/b)
punto = div.find(".")
entero =(div[:punto])
decimal =(div[punto:punto+1+k])
print(f"{entero}{decimal}")

#1.4.2. Suma de cadenas de texto
A = "12345678901234567890"
B = "98765432109876543210"

a = list(A)
b = list(B)

if len(a) > len(b):
    while len(a) > len(b):
        b.insert(0, "0")

if len(b) > len(a):
    while len(b) > len(a):
        a.insert(0, "0")

digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def convercion_int(string):
    for i in range(10):
        if string == digitos[i]:
            return i

def conversion_of_mayus(cadena):
    chain = []
    for i in cadena:
        chain.append(convercion_int(i))
    return chain

num_a = conversion_of_mayus(a)
num_b = conversion_of_mayus(b)

sum_ultima = []

sobras = 0
for i in range(len(a) - 1, -1, -1):
    sum = num_a[i] + num_b[i] + sobras
    if sum >=10:
      sobras = 1
      sum -=10
    else:
      sobras = 0
    sum_ultima.insert(0, sum)
if sobras > 0:
    sum_ultima.insert(0, sobras)


sum_final_str = "".join(str(numero) for numero in sum_ultima)

print(sum_final_str)

#1.4.3. Suma de fracciones
from fractions import Fraction
n = int(input("Cuantas divisones va a meter?"))
fracciones = []
for i in range(n):
 div = input("Ingrese la fraccion: ")
 fracciones.append(div)

sumando = sum(Fraction(x) for x in fracciones )
print(sumando)

#2.3.1. Contraseña segura

contrasena =str(input("Ingrese su contraseña "))
#print(contrasena.isdigit())
#print(contrasena.isupper() for  contrasena in contrasena)
if len(contrasena) >= 8 and any(contrasena.isalpha() for contrasena in contrasena) and any(contrasena.isupper() for contrasena in contrasena) and any(contrasena.islower() for contrasena in contrasena):

  print("Contraseña segura")
else:
 print("Contraseña no segura")

#2.3.2. Cálculo de impuesto
consumo = int(input("Ingrese cuantas unidades consumio "))

if consumo >= 101 and consumo <= 200:
 precio = 0.5 + (consumo-101)*0.5
 print(f"El impuesto aplicado: ${precio}")
elif consumo >= 201:
  precio = 0.7 + (consumo-201)*0.7
  print(f"El impuesto aplicado: ${precio}")
else:
  print(f"El impuesto aplicado fue de $0 :o")

#2.4.1. El número mágico
n = float(input("A ver si es magico o nel, ponga aqui su num. a comprobar: "))
if n % 7== 0 and n%5 != 0:
  print("magico")
else:
  print("Normal")

#2.4.2. Año bisiesto
n = float(input("A ver si es año biciesto o nel, ponga aqui su año par comprobar: "))
if n % 4== 0 or (n% 100 == 0 and n% 400) == 0:
  print("biciesto")
else:
  print("biciesto")

#2.5.1. Elevador lógico
ubi_a, ubi_b, piso = (5,5,9)
dis_a = ubi_a-piso
#print(dis_a)
des_b = ubi_b-piso
#print(des_b)

if ubi_a == piso:
  print("Asenor A")
elif dis_a < des_b:
  print("Asensor B")
else:
  print("Asensor A")

#2.5.2. Punto en zona de peligro
sensor_x,sensor_y = (-3, -4)
ciruclo = (sensor_x*sensor_x)+ (sensor_y*sensor_y)
if ciruclo <= 25 or sensor_x >0 and sensor_y >0:
  print("Peligro")
else:
  print("Seguro")