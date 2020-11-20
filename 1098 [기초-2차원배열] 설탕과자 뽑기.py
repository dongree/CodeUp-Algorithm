h, w = input().split()

lista = [[0 for i in range(int(w))] for j in range(int(h))]

n = int(input())

for _ in range(n):
    l, d, a, b = input().split()
    x = int(a)-1
    y = int(b)-1
    if int(d) == 0:
        for i in range(int(l)):
            lista[x][y+i] = 1
    else:
        for i in range(int(l)):
            lista[x+i][y] = 1


for i in range(int(h)):
    for j in range(int(w)):
        print(lista[i][j], end=' ')
    print()
