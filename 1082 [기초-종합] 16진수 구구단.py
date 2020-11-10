a = input()

for i in range(1, 16):
    print("%s*%X=%X" % (a, i, int(a, 16)*i))
