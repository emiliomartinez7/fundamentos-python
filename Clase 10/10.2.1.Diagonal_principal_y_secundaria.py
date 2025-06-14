'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    10.2.1
Descripción:  Imprimir la diagonal principal y secundaria de una matriz cuadrada.
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
diagonal_1 = []
diagonal_2 = []

for j in range(N):
    diagonal_1.append(m[j][j])
print(diagonal_1)
for i in range(N):
    j = N - 1 - i
    diagonal_2.append(m[i][j])
print(diagonal_2)
