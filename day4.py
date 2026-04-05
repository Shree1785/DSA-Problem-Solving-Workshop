# print('prashantjha777'.isalnum())#True
# print('prashantjha'.isalpha())#True
# print('777f'.isdigit())
# print('sdsdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))


# print("prashant".find("r"))
# print("prashant".index("r"))
# print("prashant jha".count('a'))

# print("prashant".find("r"))
# print("prashant".index("r"))
# print("prashant jha".count('z'))


##Check if a Key Exists in a Dictionary:

##Question- Write a function to check if a key exists in a dictionary
##Logic- Use the in operator or the get() method
##Sample Input- Dictionary: {"name":"Alice", "age":30},key:"age"
##Expected Output- Key Exists

# def check_key(d, key):
#     if key in d:
#         return "Key Exists"
#     else:
#         return "Key Does Not Exist"


# my_dict = {"name": "Alice", "age": 30}
# key = "age"

# result = check_key(my_dict, key)

# print(result)



##Count Frequency of Elements in a List using a Dictionary:

##Question- Write a function to count the frequency of elements in a list using a dictionary
##Logic- Iterate through the list and use a dictionary to store counts
##Sample Input- [1,2,3,4,5,6]
##Expected Output- {"1":1, "2":2, "3":2, "4":1, "5":1}


# def count_frequency(lst):
#     freq = {}
    
#     for item in lst:
#         key = str(item)   
#         if key in freq:
#             freq[key] += 1
#         else:
#             freq[key] = 1
            
#     return freq

# my_list = [1, 2, 3, 4, 2, 3, 5]

# result = count_frequency(my_list)

# print(result)