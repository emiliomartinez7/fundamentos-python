'''
Clase:        6.2.1 Eliminando valores duplicados
Tema:         Manejo de listas
Ejercicio:    Eliminando valores duplicados
Descripción:  Usar una lista para eliminar los valores duplicados de una lista de enteros.

Autor:        Emilio Josue Martinez Aguilera
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lst = (input())
lst = [int(x) for x in str(lst).split()]
dups = set(lst)
no_dups = []
for i in lst:
    if i not in no_dups:
        no_dups.append(i)
    
print(*no_dups)
