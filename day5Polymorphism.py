# Polymorphism

# Polymorphism means having many forms.
# We can define polymorphism as the ability of a message to be displayed in more than one form.
# Eg: A person in real world can perform many task at a time like at the same time can watch TV, can eat food, can receive a call.

# In C++ there are two types of polymorphism:

# □ Compile time polymorphism:
# eg: function overloading

# □ Runtime polymorphism:
# eg: function overriding

# polymorphism Example


# class Principal:  
#     def role(self):  
#         print("I am managing all activity of college")  
  
# class Dean:  
#     def role(self):  
#         print('Dean= I am decision taking person')  
          
# class Hod:  
#     def role(self):  
#         print('Hod= I have responsibility of Teachers and Students')         
# class Faculty:  
#     def role(self):  
#         print('Faculty= I have to complete syllabus successfully')  
        
# # ========== class declaration completed=====================================  

# def  func(obj): # called func obj =1:Dean  
#     obj.role()# calling func  
# campus=[Principal(),Dean(),Hod(),Faculty()]   
# for obj in campus: #obj =[0:Principal(),1:Dean(),2:Hod()]  
#     func(obj)   # calling fun
    
    
    
    
##Python does not support constructor overloading

# How the polymorphism implemented here

# Overloading in python

# 1.Operator overloading
# 2.Method overloading
# 3.Constructor overloading

# Overriding in python

# 1.Method overriding
# 2.Constructor overriding


# In Python method overloading is not possible.
# If we are trying to declare multiple methods with same name and
# different number of arguments then Python will always consider only 1

#directly method overloading

# class Arithmatic:  
#     def add(self,a):  
#         print(a)       ######Code has error
#     def add(self,a,b):  
#         print(a+b)  
#     def add(self,a,b,c):  
#         print(a+b+c)  
# obj = Arithmatic()  
# obj.add(10)  
# obj.add(10,20)  
# obj.add(1,2,3)


# To handle overloaded method in python
# If method with variable number of arguments required then we can
# handle with default arguments

# class Arithmetic:
#     def add(self, a=None, b=None, c=None):
#         if a != None and b != None:      #####Correct code
#             print(a + b)
#         elif a != None and b != None and c != None:      
#             print(a + b + c)
#         else:
#             print("enter atleast two argument")


# obj = Arithmetic()

# obj.add(10)
# obj.add(10, 20)
# obj.add(1, 2, 3)


##Constructor Overloading


# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be used

# class Arithmetic:

#     def __init__(self):
#         print("There is no argument")         ######Code has error

#     def __init__(self, a):
#         print("passing one argument")

#     def __init__(self, a, b):
#         print("passing two arguments")


# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(1, 2)



# class Arithmetic:
#     def __init__(self, a=None, b=None):
#         if a is None and b is None:
#             print("There is no argument")     #####Correct code
#         elif b is None:
#             print("passing one argument")
#         else:
#             print("passing two arguments")


# obj1 = Arithmetic()
# obj2 = Arithmetic(10)
# obj3 = Arithmetic(10, 20)


##Python supports both constructor overriding and method overriding


# Method Overriding(parent and child relationship must be there)


# class RBI:
#     def home_loan(self):
#         print("Home Loan = 7.5%")

#     def car_loan(self):
#         print("Car Loan = 8%")


# class SBI(RBI):
#     def home_loan(self):
#         print("SBI Provide home loan = 6.5%")
#         # super().homeloan()
 
# obj = SBI()
# obj.home_loan()   # child method overrides the parent class method



# Using super method we can access parent class method in child class


##Constructor Overriding

# class Father:
#     def __init__(self):
#         print("Father: I am already at breakfast table")


# class Child(Father):
#     def __init__(self):
#         print("Child: I will be late for breakfast")
#         super().__init__()

# obj = Child()