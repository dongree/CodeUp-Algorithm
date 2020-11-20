lista = []

for i in range(10):
    lista.append(input().split())

i = 1
j = 1

while(i < 8 or j < 8):
    if int(lista[i][j]) == 2:
        lista[i][j] = 9
        break
    if int(lista[i][j+1]) == 1:
        if int(lista[i+1][j]) == 1:
            break
        lista[i][j] = 9
        i += 1
    else:
        lista[i][j] = 9
        j += 1

if(i == 8 and j == 8):
    lista[i][j] = 9


for i in range(10):
    for j in range(10):
        print(int(lista[i][j]), end=' ')
    print()
