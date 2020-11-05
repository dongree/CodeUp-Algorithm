a = input()

for i in range(len(a)):
    print("[%d]" % (int(a[i])*10**(4-i)))
