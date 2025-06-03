'''
Clase:        Clase 6
Tema:         Fase de fortalecimiento lógico
Ejercicio:    6.3.1
Descripción:  Obtner el numero líder de una lista de números enteros.
Autor:        Emilio Josue Martínez Aguolera
Fecha:        2025-6-2
Estado:       [ TERMINADO ]
'''
lst = input()
n = [int(x) for x in lst.split()]
mayores = []

for i in range(len(n) - 1): 
    actual = n[i]
    derecha = n[i+1:]
    if all(actual > x for x in derecha):
        mayores.append(actual)
print(*mayores)
