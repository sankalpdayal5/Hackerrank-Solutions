a=[]
a=input()
z=input()
b=a.index(" ")
d1=int(a[0:b])
c=a[b+1:].index(" ")
m1=int(a[b+1:b+c+1])
y1=int(a[b+c+2:])
y=z.index(" ")
d2=int(z[0:y])
x=z[y+1:].index(" ")
m2=int(z[y+1:x+y+1])
y2=int(z[x+y+2:])
if(d1>=1 and d2>=1 and d1<=31 and d2<=31 and m1>=1 and m2>=1 and m1<=12 and m2<=12 and y1>=1 and y2>=1 and y1<=3000 and y2<=3000):
    f=0
    if(y2!=y1 and y2<=y1):
        f=10000
    elif(y2==y1 and m2!=m1 and m2<=m1):
        f=500*(m1-m2)
    elif(y2==y1 and m2==m1):
        f=15*(d1-d2)
    print(f)
else:
    print("Invalid input")
