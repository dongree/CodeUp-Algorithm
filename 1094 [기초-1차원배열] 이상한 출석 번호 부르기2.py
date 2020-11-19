n = int(input())
a = input().split()

for i in range(n, 0, -1):
    print(a[i-1], end=' ')
