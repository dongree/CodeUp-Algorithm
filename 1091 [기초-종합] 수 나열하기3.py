a, b, c, d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

for i in range(d-1):
    a = a*b + c

print(a)
