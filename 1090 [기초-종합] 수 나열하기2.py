a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

# 풀이 1
print(a*r**(n-1))

# 풀이 2
for i in range(n-1):
    a *= 3

print(a)
