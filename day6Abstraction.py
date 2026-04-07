
##Abstraction

# from abc import ABC, abstractmethod  
# class Help4code(ABC): # abstract class  
#     @abstractmethod # decorator  
#     def training(self):# abstract method  
#         pass  
       
#     @abstractmethod # abstract method  
#     def placement(self):  
#         pass  
  
# class Ashish(Help4code):  
#     def training(self):  
#         print('C , C++ , Java')  
#     def placement(self):  
#         print("Java placement")  
  
# class Ankush(Help4code):  
#     def training(self):  
#         print("Python | Django")  
#     def placement(self):  
#         print("Python placement students")  
  
# class Prashant(Help4code):  
#     def training(self):  
#         print("Machine learning")  
#     def placement(self):  
#         print("Data science placement")  
  
# obj1 = Ashish()  
# obj1.training()  
# obj1.placement()  
  
# obj2 = Ankush()  
# obj2.training()  
# obj2.placement()  
  
# obj3 = Prashant()  
# obj3.training()  
# obj3.placement()


# from abc import ABC, abstractmethod   
# class Irctc(ABC):#abstract class  
  
#     @abstractmethod  
#     def bookTicket(self): # abstract method  
#         pass  
  
# class MakeMyTrip(Irctc):  
  
#     def bookTicket(self):  
#         print( " ==========================================")  
#         print(" Welcome To makemytrip ")  
#         source = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date = input("Enter date")  
#         print( " ==========================================")  
          
# class GoIbibo(Irctc):  
      
#     def bookTicket(self):  
#         print(" Welcome To GOIBIBO")  
#         source = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date = input("Enter date")  
  
# class Yatra(Irctc):  
      
#     def bookTicket(self):  
#         print(" Welcome To Yatra ")  
#         source = input("Enter a source station name")  
#         destination = input("Enter destination name")  
#         date = input("Enter date")  
  
# m = MakeMyTrip()  
# m.bookTicket()  
# g = GoIbibo()  
# g.bookTicket()  
# y = Yatra()  
# y.bookTicket()


##Encapsulation


# class Base: #parent class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "Prashant"  #public data member
#         self.c = "Ashish" #private member

#         #creating a derived class/child class
# class Derived(Base): #child class
#     def __init__(self):
#                 #calling constructor of base class
#                 Base.__init__(self)
#                 # print ("calling private member of base class")
#                 # print(self.a)
#                 # print(self.__c)
# # Obj1 = Derived()
# # print(Obj1.a)
# # print(Obj1.__c)
# Obj2 = Base()
# print(Obj2.a) #accessible
# print(Obj2.__c) #not accessible



# class Rbi:
#     #declaring public method
#     def publicPolicy(self):
#         print("Check the public policy of RBI")

#         # Declaring private method
#     def __privatePolicy(self):
#         print("There is some private policy which is not accessible for public")
            


# class Sbi(Rbi):
#     def __init__(self):#first sbi class const called
#         Rbi.__init__(self)#second parent class constr called

#     def callingPublicMethod(self):#child class public method
#         print("\inside child class")
#         self.publicPolicy()#calling parent class public method

#     def callingPrivateMethod(self):#child class public method
#          self.__privatePolicy()#calling parent class private method
         
# # Obj1=Sbi()
# # Obj1.callingPublicMethod()
# # Obj1.callingPrivateMethod()
# # Obj1.publicPolicy()
# # Obj1.__privatePolicy()
# # Obj2 = Rbi()
# # Obj2.publicpolicy()
# # Obj2.__privatePolicy()
# ##Obj2 = Rbi()
# ##Obj2.publicPolicy()
# ##Obj2._Rbi_privatePolicy()


# Arrange list such that even numbers come first, then odd numbers

# n = int(input("Enter number of elements: "))
# arr = list(map(int, input("Enter elements: ").split()))

# even = []
# odd = []

# for num in arr:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# result = even + odd

# print("Output:", *result)