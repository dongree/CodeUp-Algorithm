n = int(input())

a = input().split()

list = [0 for i in range(23)]

for i in a:
    list[int(i)-1] += 1


for i in range(23):
    print(list[i], end=' ')
