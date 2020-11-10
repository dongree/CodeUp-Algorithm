h, b, c, s = input().split()

x = int(h)
y = int(b)
z = int(c)
k = int(s)

print("%.1f MB" % (x*y*z*k/8/1024/1024))
