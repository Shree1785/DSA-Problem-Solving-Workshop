##Function

#user define function
# def msg():
#     print("hello world")

# msg()


# def arithmatic():
#     a = int(input("enter the value of A "))
#     b = int(input("enter the value of B "))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# print(arithmatic())    


# def arithmatic():
#     a = int(input("enter the value of A "))
#     b = int(input("enter the value of B "))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# ##print(arithmatic())   
# result=arithmatic()
# print("Arithmatic=", result) 



#How many types of argument we can pass in function

#1.position argument
#2.keyword argument
#3. default argument
#4. variable number of argument/ variable length argument          


#positional argument
# def login(username, password):
#     if username==password:
#         print("login succesfully")
#     else:
#         print("invalid")    

# username = input("enter username :")
# password = input("enter password :")
# login(username, password)


#keyword argument
# def login(username, password):
#     if username==password:
#         print("login succesfully")
#     else:
#         print("invalid")    

# username = input("enter username :")
# password = input("enter password :")
# login(username="admin", password="admin")#calling function


#default argument
# def cityName(city):
#     print(city)

# cityName("delhi")
# cityName("nagpur")   
# cityName()




# def cityName(city="Goa"):
#     print(city)

# cityName("delhi")
# cityName("nagpur")   
# cityName()



#4. variable number of argument/ variable length argument

# def nameOfCitys(*city):
#     print("City Name's =",city)

# nameOfCitys("Goa", "Nagpur", "Mumbai", "pune","nashik")



#wap for menu driven code
# import sys

# def add():
#     val1=int(input("enter the value of val1: "))
#     val2=int(input("enter the value of val2: "))
#     print("add= ", val1+val2)

# def sub():
#     val1=int(input("enter the value of val1: "))
#     val2=int(input("enter the value of val2: "))
#     print("sub= ", val1-val2)

# def mul():
#     val1=int(input("enter the value of val1: "))
#     val2=int(input("enter the value of val2: "))
#     print("mul= ", val1*val2)



# def div():
#     val1=int(input("enter the value of val1: "))
#     val2=int(input("enter the value of val2: "))
#     print("div= ", val1/val2)            
    

# while True:
#     print("1.Addition")
#     print("2.substraction")
#     print("3.Multiplication")
#     print("4.divsion")
#     print("5.exit")
#     choice = int(input("enter your choice: "))
    
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()    
#     elif choice == 5:
#         sys.exit()



#1. rstrip()------ to remove the spaces at right hand side
#2. lstrip()-------to remove spaces at left hand side
#3. strip()--------to remove spaces both sides

# program = input("enter your programing name: ")
# p_name = program.rstrip()
# if p_name=='python':
#     print(p_name)
# elif p_name=='java':
#     print(p_name)
# elif p_name=='cpp':
#     print(p_name)
# else:
#     print("wrong programing name")