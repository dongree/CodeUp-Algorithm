n = int(input())
a = input().split()

mini = int(a[0])

for i in a:
    if(int(i) < mini):
        mini = int(i)

print(mini)
