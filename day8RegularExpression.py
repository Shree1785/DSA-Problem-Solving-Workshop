
##Regular Expression

# import re  # re module for performing all the regular expression based operation  
# count=0    # to count the number of matching found  
# pattern = re.compile("python")# string converts into bytecode  
# # print(pattern)  
# matcher = pattern.finditer("A function in python is defined by a def statement. python The general syntax looks like this: def function name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters. ")  
# #print(matcher)  
# for i in matcher:   
#     count+=1   
#     print(i.start(),"...",i.end(),"...",i.group())  
# print("The number of occurrences: ",count)  



# import re    
# count=0   
# matcher=re.finditer("Hi","HiHiHiHi")  
# # print(matcher)  
# for i in matcher:# loop 4 times execute  
#     count+=1   
#     print(i.start(),"...",i.end(),"...",i.group())  
# print("The number of occurrences: ",count)  



# import re  
# obj = input("enter any character")  
# objmatch=re.finditer(obj,"a7b @k9z")  
# #print(objmatch)  
# for match in objmatch:  
#     print(match.start(),"...",match.end(),"...",match.group())  




##re.match() checks for a match only at the beginning of the string.

#match() function operation

# import re

# a = input("enter string to perform match operation :")

# mtch = re.match(a, "python is very important language")

# print(mtch)

# if mtch != None:
#     print("match found at begining level")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("there is no matching at begining level")




# match() function

# For performing match operation we need string, this match function used to match the given pattern to starting or beginning of the string. If match is done then we will get match object else we will get None.

# fullmatch()

# As a name suggest when we have to match full string with the given pattern then we have to use fullmatch() function. If match is done then we will get match object else we will get None.


#fullmatch()

# import re

# a = input("enter string to perform match operation")

# mtch = re.fullmatch(a, "pythonisvery")

# print(mtch)

# if mtch != None:
#     print("match found")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("there is no matching at begining level")
    
    
    
# Search() function

# If the match found anywhere in the string then it return object else it
# will return None


# findall() function

# This function return a list which containing all matches


# sub() function

# This function perform substitution or replacement

# re.sub(expression,replacement_string) here every match pattern will
# be replaced by provided replacement



# search() function

# import re

# a = input("enter string to perform match operation :")

# mtch = re.search(a, "python sss dynamic lamm")

# print(mtch)

# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("there is no matching anywhere")





# import re
# a = input("enter string to perform match operation")

# f = open("python.txt", "r")

# d = f.read()

# mtch = re.match(a, d)

# print(mtch)

# if mtch != None:
#     print("match found at begining level")
#     print(mtch.start(), " ", mtch.end())
# else:
#     print("there is no matching at begining level")





# findall() function


# Match character classes

# By using this character classes we match the group of characters

# [abc]  ==> Either a or b or c

# [^abc] ==> Except a and b and c

# [a-z]  ==> Any lower case alphabet symbol

# [A-Z]  ==> Any upper case alphabet symbol

# [a-zA-Z] ==> Any alphabet symbol

# [0-9]  ==> Any digit from 0 to 9

# [a-zA-Z0-9] ==> Any alphanumeric character

# [^a-zA-Z0-9] ==> Except alphanumeric characters (Special characters)

# findall() function

# import re
# mtch = re.findall('[0-9]', "abcd3hdh5bk7ZQ9$#")
# print(mtch)



# sub() function

# import re
# obj = re.sub('[a-zA-Z]', 'X', '2345 ABCD Fabc deff')
# print(obj)


# subn() function

# It is as similar as sub() function only one thing is different that it also
# return number of replacement. This return in tuple where first
# element is string and second one is number of replacement.

# split() function

# This function is used to split the given string as per the some pattern
# then we should use split() function



# subn() function

# import re

# obj = re.subn('[0-7]', '@', 'ab3g6dk17')

# print(obj)
# print("the string is:", obj[0])
# print("the number of replacement is:", obj[1])



# Inbuilt character classes

# \s => Space character
# \S => Any character except space character
# \d => Any digit from 0 to 9
# \D => Any character except digit
# \w => Any word character [a-zA-Z0-9]
# \W => Any character except word character (Special Characters)
# .  => Any character including special characters


# WAP to check the valid mobile number


# import re

# no = input("Enter mobile number")

# obj = re.fullmatch("[0-5]\d(9)", no)

# if obj != None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")



# Write a Python Program to check whether the given mail id is
# valid gmail id or not

# import re

# s = input("Enter Mail Id:")

# m = re.fullmatch("[a-zA-Z0-9_.]*@gmail[.]com", s)

# if m != None:
#     print("Valid Mail Id")
# else:
#     print("Invalid Mail Id")

# for gmail id and college mail id

# import re

# s = input("Enter Mail Id: ")

# m = re.fullmatch("[a-zA-Z0-9_.]+@(gmail\.com|ybit\.ac\.in)", s)

# if m != None:
#     print("Valid Mail Id")
# else:
#     print("Invalid Mail Id")



# Q. Write a program to check whether the given file exists or not.
# If it is available then print its content

# import os,sys

# fname = input("Enter File Name: ")

# if os.path.isfile(fname):
#     print("file exists:", fname)
#     f = open(fname, 'r')
# else:
#     print("File does not exist:", fname)
#     sys.exit(0)

# print("The content of file is:")
# data = f.read()
# print(data)