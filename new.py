l=[3,2,6,5,1,4,8,9]
n =len(l)
sum=0
b=""

for i in range (0,n):
    if(l[i]!=5):
        sum=sum+l[i]
    elif(l[i]==5):
        while(l[i]!=8):
            b=b+str(l[i])
a=int(b)
print(sum+a)


