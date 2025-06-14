'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    10.3.2
Descripción:  Matriz binaria.
Autor:        Emilio Josue Martínez Aguilera
Fecha:        2025-6-11
Estado:       [ TERMINADO ]
'''

N = int(input())
M = int(input())
m = []
for i in range(N):
    entrada = input()
    ya_casi = list(map(int, entrada.split(",")))
    m.append(ya_casi)
ver = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
result = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        unos = 0
        for x, y in ver:
            vi,vj = i + x, j + y
            if 0 <= vi < N and 0 <= vj < M and m[vi][vj] == 1:
                if m[vi][vj] == 1:
                    unos += 1
            result[i][j] = unos

for N in result:
    print(N)
        
