###day8###


'''
#! function with parameter
def greeting(name):# name is parameter
    print("welcome",name)
for val in range(3):
    username = input("enter the name:")
    greeting(username)#username is argument
'''
'''

#! eg:3
def profile(name,age,place):
    print(name,age,place)
profile("sid",29,"cbe") 
'''
'''

s1="Hello how are you"
s2="hello how is"
def uncombined words(s1,s2)
    s1=s1.split()
    s2=s2.splict()
    x=[]
    for i in s1:
        if i not in s2:
            x.appened(i)
     for i in s2:
         if i not in s1:
             x.appened(i)
'''
'''
# eg:4
#? function with return statement
def f1():
    z = 8
f1()
print(z) # error---> cannot use outside the function

# return
!!! a variable declared inside the function can be outside function using retuurn
!!! return does not prnt anything
!!! we cannot write any code below return statement
def f1(a,b):
    c = a*b
    return c
print(f1(6,8))
obj = f1(6,8)
obj1` = f1(6,8)
print(obj)
def gracemaek(obj):
     print(obj+4)
gracemark(obj)    
'''
'''
# 123

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value:"))
palindrome(a)
'''

#positional args
#keyword args
#default args
#variable length args
#keyword vaiable length args


#positional args


# eg:1
def profile(name,phone,mark):
    txt =" my name is{}. my phone number is{}.i got{} marks."
    print(txt.format(name,phone,mark))
profile(9878776767,"sidhu",97)# unexpected output



# !eg:1
# to overcome the disadvantage of position args,we use keyword args
# it is the process of intialising the paremeter with the args calling the
# function

'''

def profile(name,phone,mark):
    txt =" my name is{}. my phone number is{}.i got{} marks."
    print(txt.format(name,phone,mark))
profile(name="sid",phone=123456789,mark=98) 

'''
'''
# todo----> expection of keyword args function


def profile(name,phone,mark):
    txt =" my name is{}. my phone number is{}.i got{} marks."
    print(txt.format(name,phone,mark))
profile(name="sid",phone=123456789,mark=98)  # error ---> positional args follow  keyword
profile(name="sid",phone=123456789,mark=98)  # error ---> name has multiple values 
profile("sid",mark=98,phone=12345678)

'''
'''
#* default args
# ! eg:2
def profile(name,phone,place="kadapa"):
    txt = "my name is{}. my phone number is{}. iam from {}."
    print(txt.format(name,phone,place))

profile("sid",8767676767,"guntur")    

'''
'''

def profile(name,phone,place="kadapa"):
    if place =="kadapa" or place=="kadapa" or place=="kadapa"
    txt = "my name is{}. my phone number is{}. iam from {}."
    print(txt.format(name,phone,place))

profile("sid",8767676767,"guntur")    

'''
'''
#* variable length params
# eg:1
def profile(*name,age):
    for val in name:
    print("my name is ,"val,"may age is",age)
profile("sid",'name2','name3')    
'''
'''
#* keyword variable length args
# ! eg:1
def price(price_list):
    print(price_list)
print(shirt=1000,iphone=80000)
d1={"a":100,"b":200,c=300}
d1=dict{a=100,b=200,c=300}
print(d1)    
'''
'''
n=int(input("enter the number"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)    

'''
def dict1():
    d1 ={}
    for val in range(1,n+1):
        d1[val1] = val**2
        print(d1)
   dict1(5)
#! ----> object oriented programming
# the paradigms of objects oriented programming are
   
# class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation



#! class is a blue print of a object
l1=[1,2,3,4,5,6]
# eg:1
class c1:
    name1 = "sidhu"
    print(name1)

# eg:2
class [person:
       name = "sidhu"
c = person()
print(c.name)       



# ? eg:3
#  create of a method
# when the function is created with a class is called as method


class person:
    def display():
        print("hello welcome to the classes")
p = person()
p.display()



#? eg:4
#! method with parameter
class person:
    def display(person,name,age):
p = person()
p.display("sidhu",28)


#! eg:5
class person:
    name = "sidhu" # attribute of static variable
    lname ="M"
    def first_name(self):
        print (self.fname)
        
p = print()
p.first_name()
p.full_naame

 constructors  -->__init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation
'''
class profile:
    def __init__(self): # constructor method
        print("hey")
p = profile() # throught this process
p.__init__()
'''

























































































