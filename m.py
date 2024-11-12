l=[3,2,6,5,1,4,8,9]
n =len(l)
sum=0
b=""
i=0

while(i<n):
    #if(l[i]!=5):
        #sum=sum+l[i]
    if(l[i]==5):
        while(l[i]!=8):
            b=b+str(l[i])
            i+=1
    elif(l[i]==8):
         b=b+str(l[i])
         i+=1
        
    else:
        sum=sum+l[i]
        i+=1
    
a=int(b)
print(a)

