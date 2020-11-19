n = int(input())

lista = [[0 for i in range(19)] for j in range(19)]

for i in range(n):
    a, b = input().split()
    x = int(a)-1
    y = int(b)-1
    lista[x][y] = 1

for i in range(19):
    for j in range(19):
        print(lista[i][j], end=' ')
    print()
