a=[10,20,[30,40,50],70,80,90]
b=a
b.insert(0,60)
print(b)
print(a)
a.insert(0,5)
print(a)
print(b)
del(a[4][0])
print(a)
print(b)

