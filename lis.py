#for x in range(1,101):
#	if(x%3!=0):
print([x**3 if x%2 else x**2 for x in range(1,101) if x%3!=0])
