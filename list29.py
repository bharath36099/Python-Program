a=[]
n=int(input("enter a number of element"))
i=1
while (i<n):
   b=int(input("enter a number"))
   a.append(b)
   i=i+1
print(a)
print(a[0:3])
print(a[-1])
print(a[-1:-4])
print(a[:-3])
print(a[::-1])
