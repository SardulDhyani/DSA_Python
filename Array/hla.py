import Sys
n = 10
data = []
for i in range(n):
    a = len(data)
    b = Sys.getsizeOf(data)
    print ('Length L {0:3d}; Size in bytes: {1:4d} '.format(a,b))
    data.append(n)