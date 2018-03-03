a=int(input("enter any number"))
i=2
found=True
while(i<a):
  if(a%i==0):
    found=False
    system.exit()
  i+=1
if(found):
  print("prime number")
else:
  print("not prime")
