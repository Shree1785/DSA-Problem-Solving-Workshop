
##Write a program to compress a string by replacing consecutive characters with their counts

# s = input("Enter a string: ")

# result = ""
# count = 1

# for i in range(len(s)):
#     if i < len(s) - 1 and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1

# print("Compressed string:", result)



###Reverse Each Word in a String

##Write a program to reverse each word in a string

# s = input("Enter a string: ")

# words = s.split()
# reversed_words = []

# for word in words:
#     reversed_words.append(word[::-1])

# result = " ".join(reversed_words)

# print("Reversed words string:", result)