x=int(input())
y=int(input())
z=y-x
for i in range(z):
    a=x+1
    x=x+1
    b=a
    num=0
    while(b!=0):
        c=b%10
        d=c**3
        num+=d
        b=int(b/10)
    if(a==num):
        print(a)
