r, g, b = input().split()

capacity = int(r)*int(g)*int(b)/8/1024/1024

print("%.2f MB" % capacity)
