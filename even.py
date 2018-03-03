n=int(input("enter how many values you want"))
a=[]
for i in range(0,n):
  x=int(input("enter numbers"))
  a.append(x)
b=[]
c=[]
for i in a:
  if(i%2==0):
    b.append(i)
  else:
    c.append(i)
b.sort()
c.sort()
"""count1=0
count2=0
for k in b:
    count1=count1+1
for j in c:
    count2=count2+1
print("Largest even number:",b[count1-1])
print("Largest odd number",c[count2-1])"""
print(max(b))
print(max(c))