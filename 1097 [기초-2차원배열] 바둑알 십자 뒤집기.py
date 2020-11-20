lista = []

for i in range(19):
    a = input().split()
    lista.append(a)

n = int(input())

for _ in range(n):
    a, b = input().split()
    x = int(a)-1
    y = int(b)-1
    for i in range(19):
        if y != i:
            if int(lista[x][i]) == 0:
                lista[x][i] = 1
            else:
                lista[x][i] = 0
        if x != i:
            if int(lista[i][y]) == 0:
                lista[i][y] = 1
            else:
                lista[i][y] = 0


for i in range(19):
    for j in range(19):
        print(lista[i][j], end=" ")
    print()
