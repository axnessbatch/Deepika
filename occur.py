a=[1,2,3,4,2,3,2,7,8,2,10]
print(len([i for i in a if i == 2]))

x=[]
for i in a:
  if(i==2):
    	x.append(i)
print(len(x))