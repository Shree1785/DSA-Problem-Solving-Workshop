# names=[4,2,5,6,8,2]
# for i in names:
#     print(i)


##moves the zeros to last

# A=[4,0,2,5,0,1] ##input
# B=[4,2,5,1,0,0] ##output

# A=[4,0,2,5,0,1]
# for i in A:
#     if i==0:
#         A.remove(i)
#         A.append(i)
# print(A)

##Remove duplicates
#Sample Input: [1,2,2,3,4,4,5]
#Expected Output: [1,2,3,4,5]

# A= [1,2,2,3,4,4,5]
# newlist=[]
# for i in A:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

##Find out common element from 3 lists

#Sample Input: [1,2,3], [2,3,4], [3,4,5]
#Expected Output: [3]

# A = [1, 2, 3]
# B = [2, 3, 4]
# C = [3, 4, 5]
# for i in A:
#     if i in B and i in C:
#         print(i)


##WAP to calculate and return the sum of distances between two adjacent numbers in an array of positive integers

# n=int(input("Enter the size of array:"))
# arr=[]
# for i in range(n):
#     val=int(input("Enter the value of array:"))
#     arr.append(val)
# sum=0
# print(arr)
# for i in range(n):
#     if i+1 in arr:
#         sum+= abs(arr[i]-arr[i+1])
# print(sum)
          

# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)

###Generate code for this output
        
### 1 5
### 2 4
### 4 2
### 5 1

# for i in range(1, 6):
#     if i != 3:
#         j = 6 - i
#         print(i, j)
        

##zip() inside we take multiple range function

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)


##WAP to move *
#input= prashant*is*a*good*programmer
#output= ****prashantisagoodprogrammer

# s = "prashant*is*a*good*programmer"

# stars = ""
# chars = ""

# for ch, _ in zip(s, s):   # using zip
#     if ch == '*':
#         stars += '*'
#     else:
#         chars += ch

# print(stars + chars)


# name="prashant*is*a*good*programmer"
# newname=""
# val=""
# for i in name:
#     if i!="*":
#        newname +=i
#     else:
#        val+=i
# print(newname)
# print(str(val+newname))


#BODMAS
a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*c/d)
# print(a+(b*c)/d)

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

##Check for Anagrams

##WAP to check if two strings are anagrams of each other

##Logic-Check if the character counts in both strings are the same

##Sample Input: "listen" and "silent"
##Expected Output: Anagrams

# if sorted("listen") == sorted("silent"):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# str1="listen"
# str2="silent"

# if sorted(str1)==sorted(str2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

##WAP to count the number of words in a string
##Logic- Use loops to count spaces and words

# Sample Input- This is a sentence
# Expected Output- 4

##to count space

# a = "this is a my sentece"
# count = 1
# for i in a:
#     if i == ' ':
#         count+=1
# print(count)

##Product of Array Except Self

##Given an array,return an array where each element is the product of all the elements in the array except itself

##Logic-Use two passes, one from left to right, and one from right to left, to calculate products

##Sample Input:[1,2,3,4]
##Expected Output: [24,12,8,6]

# arr = [1, 2, 3, 4]
# n = len(arr)

# result = [1] * n

# left = 1
# for i in range(n):
#     result[i] = left
#     left *= arr[i]

# right = 1
# for i in range(n-1, -1, -1):
#     result[i] *= right
#     right *= arr[i]

# print(result)