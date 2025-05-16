"""
Clase:        1 Y 2
Tema:         Tipo de variables y Bloques comparativos
Ejercicio:    1.3.1 -- 1.3.2 -- 2.3.1 -- 2.3.2 -- 2.4.1 -- 2.4.2 -- 2.5.1 
Descripción:  Calculo de la propina, generador de correos key, Contraseña segura, calculo de impuestos, El numero magico, Año bisiesto, Elevaor logico

Autor:        Emilo Josue Martinez Aguiera
Fecha:        2025-05-15
Estado:       [En progreso]
"""

total = float(input("Ingrese el balor de su cuneta"))
p = float(input("que porcentaje de propina quiere?"))
porcentaje = (total*p)/100
print(f"La propina es {porcentaje}")
total_a_pagar = total + porcentaje
print(f"El total a pagar es {total_a_pagar}")

print("Ingrese su nombre completo")
primero = input()
segundo = input()
tercero = input()
cuarto = input()
print(f"Su nombre es {primero}_{cuarto}@keyinstitute.edu.sv")



contrasena =str(input("Ingrese su contraseña "))
print(contrasena.isdigit())
print(contrasena.isupper() for  contrasena in contrasena)
if len(contrasena) >= 8 and any(contrasena.isalpha() for contrasena in contrasena) and any(contrasena.isupper() for contrasena in contrasena) and any(contrasena.islower() for contrasena in contrasena):

  print("Contraseña valida")
else:
 print("Contraseña invalida")

consumo = int(input("Ingrese cuantas unidades consumio "))

if consumo >= 101 and consumo <= 200:
 precio = 0.5 + (consumo-101)*0.5
 print(f"El impuesto aplicado: ${precio}")
elif consumo >= 201:
  precio = 0.7 + (consumo-201)*0.7
  print(f"El impuesto aplicado: ${precio}")
else:
  print(f"El impuesto aplicado fue de $0 :o")

n = float(input("A ver si es magico o nel, ponga aqui su num. a comprobar: "))
if n % 7== 0 and n%5 != 0:
  print("magico")
else:
  print("Normal")

n = float(input("A ver si es año biciesto o nel, ponga aqui su año par comprobar: "))
if n % 4== 0 and n% 100 == 0 and n% 400 == 0:
  print("biciesto")
else:
  print("biciesto")

ubi_a, ubi_b, piso = (2,10,9)
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