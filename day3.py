##Rearrange Positive and Negative Numbers:
##Question- Given an array containing both positive and negative numbers, rearrange them in an alternating fashion.
##Logic- Separate positive and negative numbers, then merge them alternately
##Sample Input:[-1,2,3,4,5,-6]
##Expected Output: [-1,2,3,4,-6,5]


# arr = [-1, 2, 3, 4, 5, -6]

# pos = []
# neg = []


# for i in arr:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# result = []
# i = j = 0


# while i < len(neg) and j < len(pos):
#     result.append(neg[i])
#     result.append(pos[j])
#     i += 1
#     j += 1


# while i < len(neg):
#     result.append(neg[i])
#     i += 1

# while j < len(pos):
#     result.append(pos[j])
#     j += 1

# print(result)


##Find the Majority Element:
##Question- Find the majority element (element that appears more than n/2 times) in an array
##Logic- Use Moore's Voting Algorithm to find the majority element
##Sample Input: [3,3,4,2,4,4,2,4,4]
##Expected Output: Majority Element:4

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]


candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1


count = 0
for num in arr:
    if num == candidate:
        count += 1

if count > len(arr) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element")