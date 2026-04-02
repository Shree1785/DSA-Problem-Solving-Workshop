# math=50
# name="prashant"
# pi=3.14
# result=True
# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))

# math=50 #new memory
# chem=50
# phy=50
# hindi=40
# print(id(math))
# print(id(chem))
# print(id(phy))
# print(id(hindi))

# list=[[1,2,3],
#       [4,5,6],
#       [7,8,9]]

#---------

#list[row][col]
#list[0][0]=1
#list[1][1]=5
#list[2][2]=9
# if i== j:
#     sum += i

# print(2+2)
# print("2"+"2")
# val1=int(input("Enter value of val1 :"))#2
# val2=int(input("Enter value of val2 :"))#4
# print(val1+val2)

# input function by default only accept string value

# print(int(3.14))
# #print((int(10+5j)))
# print(int(True))#1
# print(int(False))#0
# #print(int("4.22"))
# print(int("4"))
# #print(int("prashant"))
# #we can not convert complex value to int
# #we can not convert floating point value string to int
# #can't convert string name to int'''

# #float() used to convert
# print(float(3))#3.0
# #print(float(50+2j))
# print(float(True))#1.0
# print(float(False))#0.0
# print(float(4.22))
# print(float("4"))
# #print(float("name")) 
# #we cannot convert complex value to float
#cant convert string name to float

## complex() used to convert
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# #print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))


## bool() is used to convert
# print(bool())
# print(bool(0))#False
# print(bool(15))#True
# print(bool(3.14))#True
# print(bool(0.0))#False
# print(bool(1.2j))#True
# print(bool(0.0j))#False
# print(bool(-1))#True
# print(bool(False))#False
# print(bool(True))#True
# #print(bool("Prashant"))#True

##33 reserved keywords in python
##All are alphabets and True/False/None are keywords first letters are capital

##Swapping of Two Number Using Third Variable

# val1 = int(input("Enter the value of val1:"))
# val2 = int(input("Enter the value of val2:"))
# print("Before swapping val1=",val1, "val2=",val2)
# temp=val1 #temp=100
# val1=val2 #val1=200
# val2=temp #val2=100
# print("Before swapping val1=",val1,"val2=",val2)


##Swapping of Two Number Without Using Third Variable  a=100 b=200

# val1 = int(input("Enter the value of val1: "))
# val2 = int(input("Enter the value of val2: "))
# print("Before swapping val1=", val1, "val2=", val2)
# val1 = val1 + val2   #100+200=300 a=300
# val2 = val1 - val2   #300-200=100 b=100
# val1 = val1 - val2   #300-100=200 a=200
# print("After swapping val1=", val1, "val2=", val2)



# p1 = int(input("Enter the marks of p1:"))
# p2 = int(input("Enter the marks of p2:"))
# p3 = int(input("Enter the marks of p3:"))
# total=p1+p2+p3
# percentage=total/3.0
# print("Total=" , total)
# print("Percentage=", percentage)

##WAP to calculate Simple Interest 

# p_amount=int(input("Enter principle amount:"))#100000
# roi=int(input("Enter Rate of interest:"))#10
# time=int(input("Enter the duration of loan amount:"))#1
# si=p_amount*roi*time/100
# print("Simple interest=",si)

##WAP To Enter Height of User in Feet And Convert it Into Inch And Centimeter inch=h*12 and cm=inch*2.54

# height= float(input("Enter height of user in feet: "))
# inch = height * 12
# cm = inch * 2.54
# print("Height in inches =", inch)
# print("Height in centimeters =", cm)

                                                    ###reverse  1 to 6 123456 to 654321
# num=123 #num=321
# a= num%10 #a=3
# num = num // 10 #num=12
# b=num%10 #b=2
# c= num//10 # c=1
# rev=a*100+b*10+c*1 #300+20+1=321
# print(num)



# num = 123
# a = num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# rev = a * 100 + b * 10 + c
# print("Reversed number =", rev)


###                            ###reverse  1 to 6 123456 to 654321

# num = 123456
# a = num % 10        # 6
# num = num // 10     # 12345
# b = num % 10        # 5
# num = num // 10     # 1234
# c = num % 10        # 4
# num = num // 10     # 123
# d = num % 10        # 3
# num = num // 10     # 12
# e = num % 10        # 2
# f = num // 10       # 1
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
# print("Reversed number =", rev)


    
##When we want to do the address comparison we use the identity operator

##When we want to do address comparison then we should go for identity operator


# a=10
# b=10
# print(a is b) #True
# print(a is not b) #False

# a=10
# b=15
# print(a is b) #False
# print(a is not b) #True

## Membership Operator
## By using membership operator we check that the object is present or not in collection 


# name = "help4code"
# print("z" in name)
# print("p" in name)

# name = "help4code"
# print("z" not in name)
# print("p" not in name)


###Conditional stmts

##simple if

##WAP to accept any one number and check pos, neg and zero
# no=int(input("Enter any one number:"))
# if no>0:
#    print("Positive number")
# if no<0:
#    print("Negative number")
# if no==0:
#    print("Number is zero")
   
##Accept 5 numbers using 5 variables n1,n2,n3,n4,n5 and find out the maximum number ##Logical AND

# n1 = int(input("Enter the value of 1: "))
# n2 = int(input("Enter the value of 2: "))
# n3 = int(input("Enter the value of 3: "))
# n4 = int(input("Enter the value of 4: "))
# n5 = int(input("Enter the value of 5: "))

# if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
#     print("n1 is greater =", n1)

# if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
#     print("n2 is greater =", n2)

# if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
#     print("n3 is greater =", n3)

# if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
#     print("n4 is greater =", n4)

# if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
#     print("n5 is greater =", n5)
    
    
##if else

# username=input("Enter username:")
# password=input("Enter password:")
# if username == password:
#     print("Login successful")
# else:
#     print("Invalid Credentials")


##WAP to accept Phy,Chem, and Maths Subject marks calculate total and percentage and if percentage is greater then equal to 60 and 
##gender is equal to male so he is eligible for placement else eligible for data entry job



# phy = int(input("Enter Physics marks: "))
# chem = int(input("Enter Chemistry marks: "))
# maths = int(input("Enter Maths marks: "))

# gender = input("Enter gender (male/female): ")

# total = phy + chem + maths
# percentage = total / 3

# print("Total marks =", total)
# print("Percentage =", percentage)

# if percentage >=60 and gender == "male":
#     print("Eligible for placement")
# else:
#     print("Eligible for data entry job")


##nested if else:    #WAP to accept value of A,B,C and find max value

# if condition-1:
#     if condition-2:
#         statement
# else:
#     if condition-3:
#         statement
#     else:
#         statement
 
 
# A = int(input("Enter value of A: "))
# B = int(input("Enter value of B: "))
# C = int(input("Enter value of C: "))

# if A > B:
#     if A > C:
#         print("Maximum value =", A)
# else:
#     if B > C:
#         print("Maximum value =", B)
#     else:
#         print("Maximum value =", C)

##Using nested if else show that Monday to Friday Working Day and Saturday,Sunday Off

# day = input("Enter day: ")

# if day == "Monday":
#     print("Working Day")
# else:
#     if day == "Tuesday":
#         print("Working Day")
#     else:
#         if day == "Wednesday":
#             print("Working Day")
#         else:
#             if day == "Thursday":
#                 print("Working Day")
#             else:
#                 if day == "Friday":
#                     print("Working Day")
#                 else:
#                     if day == "Saturday":
#                         print("Off")
#                     else:
#                         if day == "Sunday":
#                             print("Off")
#                         else:
#                             print("Invalid Day")


# day=input("Enter your day name:")

# if day=="saturday" or day=="SATURDAY" or day=="sunday" or "SUNDAY":
#     print("Weekend")
# else:
#     print("Working day")



## Entered character is lowercase or uppercase or special symbol or digit only of 1 entered value

##WAP to accept any one character from keyboard and check it is in upper case, lower case, digit and 
# special symbol so print message wit respect to entered value

# ch = input("Enter any one character: ")

# if len(ch) == 1:
#     if ch.isupper():
#         print("It is an uppercase letter")
#     else:
#         if ch.islower():
#             print("It is a lowercase letter")
#         else:
#             if ch.isdigit():
#                 print("It is a digit")
#             else:
#                 print("It is a special symbol")
# else:
#     print("Please enter only one character")

# ch = ord(input("Enter any character: "))

# #ord function used to convert in ASCII code
# if ch >= 65 and ch <= 91:
#         print("your entered character is in upper case")

# elif ch >= 97 and ch <= 122:
#         print("your entered character is in lower case")

# elif ch >= 48 and ch <= 57:
#         print("your entered character is in digit")

# else:
#         print("your entered character is in special symbol")


# Amount = int(input("Please Enter Amount for withdraw: "))

# print("100 notes:", Amount // 100)
# print("50 notes:", (Amount % 100) // 50)
# print("20 notes:", ((Amount % 100) % 50) // 20)
# print("10 notes:", (((Amount % 100) % 50) % 20) // 10)
# print("5 notes:", ((((Amount % 100) % 50) % 20) % 10) // 5)