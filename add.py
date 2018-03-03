a=[4,5,6,7,8]
b=[1,2,3]
while(len(a)!=len(b)):
	b.append(0)
print([a[x]+b[x] for x in range(len(a))])