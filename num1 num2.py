
num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
num=[]
for i in range (num1,num2+1):
    if i in range(10,100):
        a=i/10
        b=i%10
   
        if ((a+b)%3==0 and i%3==0):
            num.append(i)
print('the Max number is:',max(num))

