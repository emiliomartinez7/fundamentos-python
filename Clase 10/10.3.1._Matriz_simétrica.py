'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    10.3.1
Descripción:  Matriz simetrica.
Autor:        Emilio Josue Martínez Aguilera
Fecha:        2025-6-11
Estado:       [ TERMINADO ]
'''
N = int(input())
m = []
for i in range(N):
    entrada = input()
    ya_casi = list(map(int, entrada.split(",")))
    m.append(ya_casi)
    
simetrica = True
for i in range(N):
    for j in range(N):
        if m[i][j] != m[j][i]:
            simetrica = False
            break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")

