a=['1','2','3','2','3','4','1','3','4']
b=[]
sum=0
for i in a:
  if(i not in b):
    b.append(i)
for i in b:
  sum+=int(i)
avg=sum/4
print(sum)
print(avg)