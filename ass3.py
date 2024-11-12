
''' 1 sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha(): 
        letter_count += 1
    elif char.isdigit():  
        digit_count += 1
print("Number of letters:", letter_count)
print("Number of digits:", digit_count)'''



''' 2 input_string = input("Enter a string: ")
if len(input_string) < 3:
    result = input_string 
else:
    if input_string.endswith("ing"):
        result = input_string + "ly"
    
    else:
        result = input_string + "ing" 


print("Result:", result)'''

''' 3 def find_longest_word_length(word_list):
    if not word_list:  
        return 0

    
    longest_word = max(word_list, key=len)

    return len(longest_word)


word_list = ["apple", "banana", "cherry", "date", "elderberry"]
result = find_longest_word_length(word_list)
print("Length of the longest word:", result)'''



''' 3.2 a=[]
for i in range(5):
 x=input("enter the string :")
 a.append(x)
print(a)
b=max(a)
print("the maximum list is",b)'''


#diplay the resultant string rev order
'''a=[]
a=input("Enter the string:")
b=a[0::2]
c=b[-1::-1]
print(b)
print(c)'''


#remove punctuation from string

'''a=input("Enter the string")
b=["*","@","!","?"]
a=''.join(i for i  in a if not i in b)
print(a)'''


#string merging
'''a=input("Enter the String")
b=input("Enter the String")
for i in range(0,len(a)):
    print(a[i])
    for j in range(0,len(b)):
        print(b[j])'''
#pattern
''''i=1
while i<=5:
    j=1
    while j<=i:
        print('*', end='')
        j=j+1
    print()
    i=i+1'''
 #rev pattern
'''i=1
while i<=5:
    b=1
    while b<=5-i:
        print(' ',end='')
        b=b+1
    j=1
    while j<=i:
        print('*', end='')
        j=j+1
    print()
    i=i+1'''
#mul pattern
'''i=1
k=1
while i<=5:
    b=1
    while b<=5-i:
        print(' ',end='')
        b=b+1
    j=1
    while j<=k:
        print('*', end='')
        j=j+1
    k=k+2
    print()
    i=i+1'''
#pattern uusing number
'''i=1
k=1
while i<=5:
    b=1
    while b<=5-i:
        print(' ',end='')
        b=b+1
    j=1
    while j<=k:
        print(i, end='')
        j=j+1
    k=k+2
    print()
    i=i+1'''
#down pattern
'''n=int(input('Enter the Number:'))
i=1

while n>0:
    b=1
    while b<i:
        print(' ',end='')
        b=b+1
    j=1
    while (j<=(n*2)-1) :
         print('*', end = '')
         j=j+1
    print()
    n=n-1
    i=i+1'''
#table
'''x=int(input("Enter the number:"))
for y in range(1,11):
    print(x*y)'''

d={'ram':30,'jai':40,'hari':25,'shyam':30}
'''x=d['ram']
print(x)
print(d.get('ram'))
print(d.setdefault('ram'))
s=d.items()
print(s)'''

# function
'''def add(a,b):
    c=a+b
    print(c)

a=int(input("Enter the 1st Number :"))
b=int(input("Enter the 2nd Number :"))
add(a,b)'''
#string palindraome
'''a=input('Enter the string :')
b=a[-1::-1]
if(a==b):
    print('Palindrome String')
else:
    print('Not Palindrome String')'''
#append use
'''a=[]
for i in range(5):
    x=input('Enter the item in List:')
    a.append(x)
print(a)'''
#list input and count
'''a=[]
for i in range(5):
    x=input('Enter the Number')
    a.append(x)
x=input('Enter  Value whose frequency you hane to count:')
f=a.count(x)
print('Frequency of' ,x,' is=',f)'''
#index return
'''a=[]
for i in range(5):
    x=input('Enter the values')
    a.append(x)
x=input('Enter the value to find index:')
z=a.index(x)
print('Index:',z)'''
#input And find key in dict
'''d={}
n=int(input('Enter the range of Key:'))
for i in range(n):
    key=input('Enter the key:')
    value=input('Enter the value:')
    d[key]=value
key=input('Enter the key to find')
if key in d.keys():
    print("Value",d[key])'''
#sort dictt
'''d={}
n=int(input('Enter the range of Key:'))
for i in range(0,n):
    key=int(input('Enter the key:'))
    value=input('Enter the value:')
    d[key]=value
l=sorted(d.items())
print(l)'''
'''dict2={}
n=int(input('Enter the range of Key:'))
for i in range(0,n):
    key= int(input('Enter the key:'))
    value=input('Enter the value:')
    dict2[key]=value
l=sorted(dict2.items())
print(l)'''

#list.index
'''a=[1,'ram',10]
print(a)'''
'''a.insert(2,'shyam')
print(a)'''
#remove
'''a.remove(10)
print(a)'''
#reverse
'''a.reverse()
print(a)''' 
# pop -remove last element

'''a.pop()
print(a)'''
#program to find sum of element in list
'''a=[]
n=int(input("Enter the range:"))
for i in range(n):
    x=int(input('Enter the value:'))
    a.append(x)
print(a)
sum=0
for i in range(n):
    sum=sum+a[i]
print(sum)'''
# odd even in list
'''a=[]
n=int(input("Enter the range:"))
for i in range(n):
    x=int(input('Enter the value:'))
    a.append(x)
print(a)
even=0
odd=0
for i in range(n):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print('Even=',even ,'odd=',odd)'''
# search number in list
'''a=[]
n=int(input("Enter the range:"))
for i in range(n):
    x=int(input('Enter the value:'))
    a.append(x)
print(a)
key=int(input('Enter the number:'))
flag=0
for i in range(n):
    if(a[i]==key):
        flag=1
        pos=i+1
        break
if(flag==1):
    print('Key found at:',pos,'position')
else:
    print('Key Not found')'''


# merge dictionary

'''def Merge(a,b):
    res = {**a, **b}
    return res
a={1:'A',2:'B',3:'C'}
b={9:'z',8:'y'}
c={}
c=Merge(a,b)
print(c)'''


# remove duplicate fron dict
'''a = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks':25} 
print("The original dictionary is : " + str(a))
temp = []
res = dict()
 
for key, val in a.items():
   
    if val not in temp:
        temp.append(val)
        res[key] = val
print("The dictionary after values removal : " + str(res))'''


'''#multiplication table
x=int(input('Enter the number:'))
for i in range(1,11,1):
     print(x,'X',i,'=',x*i)'''
'''
#WAP to print twin prime less than 500.
def twin_prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main():
    twin_primes = []
    for i in range(3,500):
        if twin_prime(i) and twin_prime(i+2):
            twin_primes.append((i,i+2))
    print(twin_primes)
if __name__=="__main__":
    main()   '''

'''
# Python program to print prime factors

import math

def primeFactors(n):
	
	
	while n % 2 == 0:
		print(2)
		n = n // 2
		
	
	for i in range(3,int(math.sqrt(n))+1,2):
		
		
		while n % i== 0:
			print(i)
			n = n // i
			
	
	if n > 2:
		print(n)
		


n = int(input('Enter the number:'))
primeFactors(n)
'''

'''
def position_max_min(nums):
    max_result = max(enumerate(nums),key(lambda x: x[1]))
    min_result= min(enumerate(nums), key(lambda x: x[1]))
    return'''

# write a prog to enter name of employe and there salary as input store them in dictionary and display in tabular 

'''D1={"a":10,"b":20,"c":10}
count ={}
val=D1.values()
for i inm val:
    if I not in count:
        count[i] = 0
        count[i] +=1
a=False
for i in count.values():
    if i>1:
        a= True
        print(i,"keys have same values")
    if not a:
        print("No keys have same values")'''

'''dic1= eval(input("Enter dictionary :"))
dic2 ={}
for i in dic1:
    lst=dic1[i]
    sum_of_num=sum(lst)
    dic2[i]=sum_of_num
print(dic2)'''

'''generate a random password which meets the following condition:
    a) password lenghth must be 10character long
    b)it must contain atleastr 2 upper case letter ,1 digit ,and special symbol'''

'''import random
import string

def randomString(stringLength):
    letters=string.ascii_letters
    return''.join(random.choice(letters) for i in range(stringLength))
print("Random String is",randomString(5))'''


'''class Student:
    def setdata(self):
        self.name="abc"
        self.rollno="2201641540057"
        self.branch="CS"
    def display(self):
        print("Name  :",self.name)
        print("Rollno :",self.rollno)
        print("branch :",self.branch)
a=Student()
a.setdata()
a.display()'''

"""class Test:
    def__init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
        def m1(self):
            del self.d
        def display(self):
            print("helo")
obj1=Test()
print(obj1.__dict__)
obj1.m1()
print(obj1.__dict__)
del obj1.c
print(obj1.__dict__)"""
#wap that has

'''import datetime
class Person:
    def__init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year - self.dob.year
        if age>=18:
            print("you are eligble")
        else:
            print("you are  not eligble")
p1=person("abc",datetime.date(1995,12,11))
p1.check()
p2=person("abc",datetime.date(2012,12,11))
p2.check'''


'''class Parent:
    var1 = None
    _var2 = None
    __var3 = None
    def _init_(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    def displyPublicMemeber(self):
        print("Public Data Member :",self.var1)
    def _displyProtectedMemeber(self):
        print("Public Data Member :",self._var2)
    def __displyPrivateMemeber(self):
        print("Public Data Member :",self.__var3)
    def accessPrivateMemeber(self):
        self.__displayPrivateMembers()'''



'''class Person:
    def__init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print(":Age:",self.age)
class teacher(Person):
    def__init__(self,name,age,research_area,exp):
        Person.__init__(self,name,age)
        self.research_area=research_area
        self.exp=exp
    def displayData(self):
        Person.display(self)
        print("Research Area:",self.research_area)
        print("Experence :",self.exp)
    def dispaly(self):
        print("DERIVED CLASS")

obj1=Teacher("abc",40,"Blockchain",10)
obj1.displayData()
ob1.display()


write a prog with class fill.user have the option to pay the bill either by cheque or byr the cash use the inheritance to moder this situation 
    
        
 write  a prog that has a class person. inherit the class faculty from person which has also  a class publications
 
'''
'''class Bill:
    def _init_(self, amount):
        self.amount = amount

    def display_bill(self):
        print("Total amount to pay:", self.amount)


class Payment(Bill):
    def _init_(self, amount):
        Bill._init_(self,amount)
        

    def make_payment(self):
        pass


class CashPayment(Payment):
    def make_payment(self):
        print("Payment made by cash. Amount:", self.amount)


class ChequePayment(Payment):
    def _init_(self, amount, cheque_number):
        super()._init_(amount)
        self.cheque_number = cheque_number

    def make_payment(self):
        print("Payment made by cheque. Amount:", self.amount)
        print("Cheque number:", self.cheque_number)


def main():
    amount = float(input("Enter bill amount: "))
    B = Bill(amount)
    bill.display_bill()

    payment_choice = input("Choose payment method (cash/cheque): ").lower()

    if payment_choice == "cash":
        cash_payment = CashPayment(amount)
        cash_payment.make_payment()
    elif payment_choice == "cheque":
        cheque_number = input("Enter cheque number: ")
        cheque_payment = ChequePayment(amount, cheque_number)
        cheque_payment.make_payment()
    else:
        print("Invalid payment method")


if _name_ == "_main_":
    main()'''


'''write a program that overload the + operator to add two objects of class matrix

    write a prrog to overload the -= to substract the two distance of the object and also convert the
.also convert the kilometer in meter'''



'''class Matrix:
        def __init__(self, rows, cols):
            self.rows = rows
            self.cols = cols
            self.data = [[0] * cols for _ in range(rows)]

        def __add__(self, other):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix dimensions do not match for addition!")
                result = Matrix(self.rows, self.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] + other.data[i][j]
                        return result

        def display(self):
            for row in self.data:
                print(" ".join(map(str, row)))'''
'''class Distance:
    def _init_(self, kilometers=0):
        self.kilometers = kilometers

    def to_meters(self):
        return self.kilometers * 1000

    def _isub_(self, other):
        if isinstance(other, Distance):
            self.kilometers -= other.kilometers
        return self

    def _str_(self):
        return f"{self.kilometers} km ({self.to_meters()} m)"


if _name_ == "_main_":
    dist1 = Distance(10)  
    dist2 = Distance(3)   

    print(f"Initial distances: dist1 = {dist1}, dist2 = {dist2}")

    dist1 -= dist2

    print(f"After subtraction: dist1 = {dist1}")'''



'''from abc import ABC,abstractmethod
class Car(ABC):
    def init(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year


    @abstractmethod
    def print_details(self):
        pass
    def breakApplied(self):
        print("Car Stop")
class Matchback(Car):
    def print_details(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)
    def sunroof(self):
        print("Available")
c1=Matchback("Maruti","Alto",2022)
c1.print_details()'''



'''from abc import ABC, abstractmethod
class car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    @abstractmethod
    def printdetails(self):
        pass
    def breakapplied(self):
        print("car will stop")
class hatchback(car):
    def printdetails(self):
        print("brand:", self.brand)
        print("model:", self.model)
        print("year:", self.year)
    def sunroof(self):
        print("not having this feature")

c1=hatchback("maruti","alto",2022)
c1.breakapplied()
c1.printdetails()'''



'''num=[1,2,3,4,5,6]
for i in range (len(num)):
    num[i]+=2
print(num)
num=[i+2 for i in num]
print (num)

odd=[]
for i in  num:
        if( i%2 !=0):
              odd.append(i)
print (odd)
num=[i for i in num if i%2 !=0]
print (num)'''

# num=[1,3,5,8,9,10,12]
# # for i in range(len(num)):
# #     if(num[i]<=3):
# #         num[i]+=2
# #     elif num[i]<=6:
# #         num[i]+=3
# #     else:
# #         num[i]+=4

# print(num)
num = [1, 3, 5, 8, 9, 10, 12]
num = [n + 2 if n <= 3 else n + 3 if n <= 6 else n + 4 for n in num]
print(num)







    


          














        
        





