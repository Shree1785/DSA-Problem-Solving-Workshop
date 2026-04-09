


# Problem Summary (Simple Words)
# A company records sales of N products for M days.
# For each day, there are N numbers representing revenue from each product.
# We need to find the maximum revenue for each day.

# So basically:

# Read M rows.
# Each row has N numbers.
# For each row → print the largest number.


# Example

# Input

# 3 4
# 100 198 300 322
# 122 282 221 111
# 220 566 245 764

# Meaning:

# M = 3 days
# N = 4 products

# Day-wise revenue:

# Day 1 → 100 198 300 322 → max = 322
# Day 2 → 122 282 221 111 → max = 282
# Day 3 → 220 566 245 764 → max = 764

# Output

# 322 282 764


# # Read number of days (M) and products (N)
# M, N = map(int, input().split())

# result = []

# # Read sales for each day
# for i in range(M):
#     sales = list(map(int, input().split()))
#     result.append(max(sales))

# # Print maximum revenue for each day
# for r in result:
#     print(r, end=" ")



##Remove Leading Zeros from a List of Integers

# Question: Write a function to remove leading zeros from a list of integers.
# Logic: Use a list slicing or a loop to remove zeros until a non-zero element is encountered.
# Sample Input: [0, 0, 1, 2, 0, 3, 0, 0, 4]
# Expected Output: [1, 2, 0, 3, 0, 0, 4]


# Using Loop


# def remove_leading_zeros(lst):
#     i = 0
    
#     # find first non-zero element
#     while i < len(lst) and lst[i] == 0:
#         i += 1
    
#     return lst[i:]


# numbers = [0, 0, 1, 2, 0, 3, 0, 0, 4]

# result = remove_leading_zeros(numbers)

# print(result)


# Using List Slicing


# def remove_leading_zeros(lst):
    
#     # find index of first non-zero element
#     index = 0
#     while index < len(lst) and lst[index] == 0:
#         index += 1

#     # slicing the list from first non-zero element
#     return lst[index:]


# # sample list
# numbers = [0, 0, 1, 2, 0, 3, 0, 0, 4]

# result = remove_leading_zeros(numbers)

# print(result)