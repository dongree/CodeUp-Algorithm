a, b, c = input().split()
x = int(a)
y = int(b)
z = int(c)
num = 0

for i in range(x):
    for j in range(y):
        for k in range(z):
            print(i, j, k)
            num += 1
print(num)
