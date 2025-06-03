'''
Clase:        Clase 6
Tema:         Fase de fortalecimiento lógico
Ejercicio:    6.2.1
Descripción:  Elimna el número que que se repite en una lista de números enteros.
Autor:        Emilio Josue Martínez Aguolera
Fecha:        2025-5-30
Estado:       [ TERMINADO ]
'''
lst = (input())
lst = [int(x) for x in str(lst).split()]
dups = set(lst)
no_dups = []
for i in lst:
    if i not in no_dups:
        no_dups.append(i)
    
print(*no_dups)
