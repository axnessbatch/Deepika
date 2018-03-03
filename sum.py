a=[2,-4,3,6,7,-8,10,15,-18,20]
sum=0
x=0
y=0
for i in a:
  if(i<0):
    sum+=i
  
  elif(i%2==0):
    x+=i
 
  else:
    y+=i
  
print(sum)
print(x)
print(y)