# class Myclass:
#     '''this is first class'''

# print (Myclass.__doc__)
# help(Myclass)

# class Student:
#     '''xyz'''
#     def __init__ (self):
#         self.name="Mayank"
#         self.age=19
#         self.marks=99
#     def talk(self):
#         print("Hello, my name is", self.name, "and  My age is : ", self.age, "and My marks are",self.marks)
# s1=Student()   
# print(s1.name)
# print(s1.age)
# print(s1.marks)    
# s1.talk()
# s2=Student()
# print(id(s1))
# print(id(s2))
# class Student:
#     '''xyz'''
#     def __init__ (self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def talk(self):
#         print("Hello, my name is", self.name, "and  My age is : ", self.age, "and My marks are",self.marks)
# s3=Student("Adarsh",56,79)
# s3.talk()



# class Test:
#     x=10
#     y=20
#     z=30
#     def m1(self):
#         print(Test.x)
#         print(Test.y)
#         print(Test.z)
# t=Test()
# t.m1()
# print(Test.x)
# print(Test.y)

# class Test:
#     def __init__(self):
#         self.__x=10
# t=Test()
# print(t._Test__x)


# class Employ:
#     def __init__(self):
#         self.eno=100
#         self.ename='Mayank'
#         self.esal=10000
# a=Employ()
# print(a.__dict__)

# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def m1(self):
#         self.c=30
# t=Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20
#     def m1(self):
#         Test.c=30
#     @classmethod
#     def m2(cls):
#         cls.d1=40
#         Test.d2=400
#     @staticmethod   
#     def m3():
#         Test.e=50
# t=Test()
# print(Test.__dict__)
# t.m1()
# # class through c21
# Test.m2()
# Test.m3()
# Test.f=60
# t1=Test()
# class Test:
#     a=10
#     def __init__(self):
#        self.b=20
#     @classmethod
#     def m1(cls):
#         cls.a=888
#         cls.b=999
# t1=Test()
# t2=Test()
# t1.m1()

# class Animal:
#     legs=4
#     @classmethod
#     def walk(cls,name):
#         print('{} walks with {} legs..'.format(name,cls.legs))
# Animal.walk('Dog')
# Animal.walk('Cat')

# class Test:
#     count=0
#     def __init__(self):
#         Test.count+=1
#     @classmethod
#     def noofObject(cls):
#         print('The number of object created for Test class:',cls.count)
# t1=Test()
# t2=Test()
# Test.noofObject()
# t3=Test()
# t4=Test()
# t5=Test()
# Test.noofObject()

# class Math:
#     @staticmethod
#     def add(x,y):
#         print('The sum:',x+y)
#     @staticmethod
#     def product(x,y):
#         print('The product:',x*y)

#     @staticmethod
#     def average(x,y):
#         print('The average:',(x+y)/2)

# Math.add(10,20)
# Math.product(10,20)
# Math.average(10,20)

class Outer:
    def __init__(self):
        print("outer class object creation")
    class Inner:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")
# o=Outer()
# i=o.Inner()
# i.m1()

# i=Outer().Inner()
# i.m1()

# Outer().Inner().m1()

# class Human:
#     def __init__(self):
#         self.name="Rahul"
#         self.head=self.Head()
#         self.brain=self.Brain()
#     def display(self):
#         print("Hello..",self.name)
#     class Head:
#         def talk(self):
#             print('Talking...')
#     class Brain:
#         def think(self):
#             print('Thinking...')

# h=Human()
# h.display()
# h.head.talk()
# h.brain.think()

class P:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print("Parent class method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent class static method")
class C(P):
    pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()


    