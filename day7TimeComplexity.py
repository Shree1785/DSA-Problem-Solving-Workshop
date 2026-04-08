
#O(1)- Constant time   //Accessing a specific element in array

#array = [1, 2, 3, 4, 5]
#array[0] //It takes constant time to access first element


#O(N)- Linear time     //Loop through array elements

# array = [1, 2, 3, 4, 5]
# for element in array:
#     print(element)
# //linear time since it is visiting every element of array


# O(LogN)- Logarithmic time   //Find an element in sorted array
  
# array = [1, 2, 3, 4, 5]
# for index in range(0, len(arr), 3):
#     print(array[index])
# //logarithmic time since it is visiting only some elements

# Example- Binary Search       


# O(N²)- Quadratic time      //Looking for a every index in the array twice

# array = [1, 2, 3, 4, 5]

# for x in array:
#     for y in array:
#         print(x,y)


#O(2ⁿ)- Exponential time  //Double recurrsion in fibonacci

# def fibonacci(n):
#     if n <=1:
#         return n
#     return fibonacci(n-10)+ fibonacci(n-2)



# Stack Operations Time and Space Complexity

# Operation 	          Time Complexity	         Space Complexity
# Create Stack	               O(1)	                      O(1)
# Push	                    O(1) / O(n²)	              O(1)
# Pop	                       O(1)	                      O(1)
# Peek	                       O(1)	                      O(1)
# IsEmpty	                   O(1)	                      O(1)
# Delete Entire Stack          O(1)	                      O(1)


# Stack is implemented in 2 ways- list and linked list


##Stack using List

#- Easy to implement
#- Speed problem when it grows


##Stack using Linked List

#- Fast performance
#- Implementation is not easy



#Queue Operations – Time and Space Complexity

# Operation 	          Time Complexity	         Space Complexity
# Create Queue	               O(1)	                      O(1)
# Enqueue	                   O(1)	                      O(1)
# Dequeue	                   O(1)	                      O(1)
# Peek	                       O(1)	                      O(1)
# IsEmpty	                   O(1)	                      O(1)
# Delete Entire Queue	       O(1)	                      O(1)


# Queue is implemented in 2 ways- list and linked list

##Queue using List

#- Easy to implement
#- Speed problem when it grows


##Queue using Linked List

#- Fast performance
#- Implementation is not easy


# def findBiggestNumber(array):  #[2,4,5,6,7,1,9,3,4,5,6]
#     firstValue = array[0] #firstvalue=9
#     for i in range(1,len(array)):#o(N)
#         if array[i] > firstValue:#o(1)
#             firstValue=array[i]#o(1)
#     return firstValue # o(1)        
            
            
# array=[2,4,5,6,7,1,9,3,4,5,6]
# print(findBiggestNumber(array))


# Time Complexity : O(1) + O(n) + O(1) = O(n) 




# Program to count special characters and whitespaces

# message = input("Enter the message: ")

# special_count = 0
# space_count = 0

# for ch in message:
#     if ch == " ":
#         space_count += 1
#     elif not ch.isalnum():   # checks if character is not alphabet or digit
#         special_count += 1

# print("Number of whitespaces:", space_count)
# print("Number of special characters:", special_count)




# import math

# n = 5
# areas = [1,4,10,16,18]

# count = 0

# for a in areas:
#     if int(math.sqrt(a))**2 == a:
#         count += 1

# print(count)



# import math

# n = int(input("Enter number of plots: "))
# areas = list(map(int, input("Enter areas: ").split()))

# count = 0

# for a in areas:
#     if int(math.sqrt(a))**2 == a:
#         count += 1

# print(count)


#Linear Search



# Linear Search Pseudocode

# • Create function with two parameters which are
# a = array and v = value

# • Loop through the array and check if the value
# v matches with a[i]

# • If a[i] = v return the index i at which the element is
# found

# • If value is never found return -1


# def linearSearch(array, target): # array = [1,2,3,4,5,6,7,8,9]
#     for i in range(len(array)): # --> O(n) 
#         if array[i] == target: # --> O(1) 
#             return i # --> O(1) 
#     return -1 # --> O(1) 

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 6

# result = linearSearch(array, target)
# if result == -1:
#     print("Not Found") 
# else:
#     print("Element found at index no =", result)




#Binary Search


# • Binary Search is faster than Linear Search.

# • Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one.

# • Binary Search only works on sorted arrays.

# Binary Search Pseudocode

#1. Start
#2. Input the sorted array A, number of elements n, and value key to search.
#3. Set low = 0 and high = n − 1.
#4. Repeat while low ≤ high

# Find middle index

    # mid = (low + high) // 2
# If A[mid] = key
    # Return mid (element found).
# Else if A[mid] < key
    # Set low = mid + 1.
# Else
    # Set high = mid − 1.
#5. If element not found return -1.
#6. Stop.




# def binarySearch(array, target): # array = [1,2,3,4,5,6,7,8,9] (sorted)
#     low = 0
#     high = len(array) - 1

#     while low <= high: # --> O(log n) 
#         mid = (low + high) // 2 # middle index
#         if array[mid] == target: # --> O(1)
#             return mid # found
#         elif array[mid] < target: 
#             low = mid + 1
#         else: 
#             high = mid - 1
#     return -1 # not found

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 4 
# result = binarySearch(array, target)
# if result == -1:
#     print("Not Found")
# else:
#     print("Element found at index no =", result) # output: 3 (4 is at index 3)