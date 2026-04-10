

# Points	           Recursion	 Iteration	
# Space efficient?        No	        Yes	      No stack memory requires in case of iteration
# Time efficient?	      No	        Yes	      In case of recursion system needs more time for pop and push operations to stack memory hence recursion less time efficient
# Easy to code?           Yes	        No	      We use recursion especially in the cases we know that a problem can be divided into smaller sub problems



# Factorial Solution

# def factorial(num): #num=1
#     if num <= 1:  # base condition
#         return 1
#     return num * factorial(num-1)

# print(factorial(4))

# # 4*factorial(3)
# # 3*factorial(2)
# # 2*factorial(1)
# # 4*3*2*1 = 24



# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome('awesome'))        # false
# print(isPalindrome('foobar'))       # false
# print(isPalindrome('tacocat'))       # true
# print(isPalindrome('amanaplanacanalpanama'))   # true
# print(isPalindrome('amanaplanacanalpandemonium'))  # false



# def power(base, exponent):
#     if exponent == 0:  
#         return 1
#     return base * power(base, exponent-1)

# print(power(2,0))   # 1
# print(power(2,2))   # 4
# print(power(2,4))   # 16

# # 2*power(2,1)
# # 2*power(2,0)
# # 2*2*1



# def power(base, exponent):
#     if exponent == 0:   # 0==0
#         return 1
#     return base * power(base, exponent-1)

# print(power(2,0))  # 1
# print(power(2,2))  # 4
# print(power(2,4))  # 16

# # 2*power(2,1)
# # 2*power(2,0)
# # 2*2*1



# def capitalizefirst(arr):

#     result = []
#     if len(arr) == 0:
#         return result

#     result.append(arr[0][0].upper() + arr[0][1:])  # Taco = Taco
#     return result + capitalizefirst(arr[1:])

# print(capitalizefirst(['car', 'taco', 'banana']))  # ['Car', 'Taco', 'Banana']




# productOfArray Solution

# def productOfArray(arr):
#     if len(arr) == 0:,
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))      #6
# print(productOfArray([1,2,3,10]))   #60




# fib Solution

# def fib(num):
#     if (num < 2):
#         return num
#     return fib(num - 1) + fib(num - 2)

# print(fib(4))   # 3
# # print(fib(10))  # 55
# # print(fib(28))  # 317811
# # print(fib(35))  # 9227465

# # 0 1 1 2 3 5