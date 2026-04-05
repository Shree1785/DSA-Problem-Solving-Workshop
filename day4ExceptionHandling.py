
##Exception Handling

# n1=int(input("Enter first value:"))
# n2=int(input("Enter second value:"))
# try:
#     print(n1/n2)
# except:
#     print("can't divide by zero")
# print("to be continue")



# try:
#     n1=int(input("Enter first value:"))
#     n2=int(input("Enter second value:"))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value:")
    
# print("to be continue")


##Handling multiple different kinds of exception with
##single except block

# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)


##The concept of default except block, generally we used

# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# except:
#     print("This is default part of except block")


##We can use else block if no error will generate it is

# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# else:
#     print("Everything is ok")


##Finally block will always executed whether try block
##generate error or not


# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print("Enter correct number:",message)
# finally:
#     print("I will always executed")


##Nested try except block


# try:
#     a=int(input("Enter first number:"))
#     b=int(input("Enter second number:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)
    
    
# try:
#     a=int(input("Enter first integer no:"))
#     b=int(input("Enter second integer no:"))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# else:
#     print("There are no error in try block")
# finally:
#     print("I am finally block i always executed whether")
    
    
# Question:

# A company is transmitting data to another server. The data is in the form of numbers. To secure the data during transmission, they plan to obtain a security key that will be sent along with the data. The security key is identified as the count of the repeating digits in the data.

# Write an algorithm to find the security key for the data.

# Input:

# The input consists of an integer data, representing the data to be transmitted.

# Output:

# Print an integer representing the security key for the given data. If no data is repeated, it should display -1.

# Constraints:

# -1

# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []

# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]

#     j = i + 1
#     while j < len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j + 1

# print(len(newlist))



##Find the second largest element

# list=[7, 3, 9, 2, 8]
# list.sort()
# print(list)
# print(list[-2])


# i=1
# while i<=5:
#     print(i)
#     i=i+1


# username=" " #str
# password=" " #str
# while username !="admin" or password !="admin":
#     username=input("Enter username:")
#     password=input("Enter password:")



# name ='programming'
# vowels =['a','e','i','o','u']
# cons=0
# vowel=0
# for i in name:
#     if i in vowels:
#         vowel +=1
#     else:
#         cons+=1
# print("consonants= ",cons)
# print("vowels= ",vowel)


##Remove all occurrences of an Element in a List:

#Question- Write a function to remove all occurrences of a specific element from a list
#Logic- Use list comprehensions or a loop to filter out the element
#Sample Input- List [1,2,2,3,4,2] and Element 2
#Expected Output- List [1,3,4]


# def remove_element(lst, element):
#     new_list = []
    
#     for item in lst:
#         if item != element:
#             new_list.append(item)
    
#     return new_list

# my_list = [1, 2, 2, 3, 4, 2]
# element = 2

# result = remove_element(my_list, element)

# print(result)



##Calculate the Product of List Elements:

#Question- Write a function to calculate the product of all elements in a list
#Logic- Use a loop to iterate through the list and accumulate the product
#Sample Input- [2,3,4,5]
#Expected Output- 120

# def calculate_product(lst):
#     product = 1
    
#     for item in lst:
#         product = product * item
    
#     return product

# my_list = [2, 3, 4, 5]

# result = calculate_product(my_list)

# print(result)
