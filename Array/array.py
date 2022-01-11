import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])

#update
a[0] = -1

#delete
del a[2]

for i in range(len(a)):
    print(a[i])
