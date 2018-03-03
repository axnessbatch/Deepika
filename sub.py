#with set
a=set([4,5,6,7,8,9])
b=set([6,7,8])
print(b.issubset(a))
#without set
for i in a:
    if(i in b):
        print("True")