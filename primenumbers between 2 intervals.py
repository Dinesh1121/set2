a=int(input())
b=int(input())
c=b-a
for i in range(c):
    a=a+1
    j=2
    flag=0
    for i in range(a-2):
        if(a%j==0):
            flag=1
            break
        j=j+1
    if(flag==0):
        print(a,end=" ")

    
