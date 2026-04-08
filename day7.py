
##Sort Dictionary by Key or Value

#Question- Write a function to sort a dictionary by keys or values in ascending or descending order.
#Logic- Use the sorted() function with a custom key or use list comprehension.
#Sample Input- {"C": 3, "B": 2, "A": 1}
#Expected Output (Ascending by Key)- {"A": 1, "B": 2, "C": 3}
#Expected Output (Descending by Value)- {"C": 3, "B": 2, "A": 1}

# # Function to sort dictionary

# def sort_dictionary(d):

#     # Ascending order by key
#     asc_key = dict(sorted(d.items()))
#     print("Ascending by Key:", asc_key)

#     # Descending order by value
#     desc_value = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
#     print("Descending by Value:", desc_value)


# # Sample input
# d = {"C": 3, "B": 2, "A": 1}

# sort_dictionary(d)

##Remove All Elements from a Dictionary

#Question- Write a function to remove all elements from a dictionary.
#Logic- Use the clear() method or assign an empty dictionary {}.
#Sample Input- {"A": 1, "B": 2, "C": 3}
#Expected Output- Empty Dictionary: {}

# Function to remove all elements from dictionary

# def clear_dictionary(d):
#     d.clear()
#     return d


# # Sample input
# d = {"A": 1, "B": 2, "C": 3}

# print("Original Dictionary:", d)

# d = clear_dictionary(d)

# print("Empty Dictionary:", d)


##Count the Number of Non-Empty Values in a Dictionary

#Question- Write a function to count the number of non-empty (non-null) values in a dictionary.
#Logic- Iterate through the dictionary and count values that are not empty.
#Sample Input- {"A": 1, "B": "", "C": 3, "D": None, "E": "Five"}
#Expected Output- Number of Non-Empty Values: 3


# Function to count non-empty values in dictionary

# def count_non_empty(d):
#     count = 0

#     for value in d.values():
#         if value:      # checks if value is not empty
#             count += 1

#     return count


# # Sample input
# d = {"A": 1, "B": "", "C": 3, "D": None, "E": "Five"}

# result = count_non_empty(d)

# print("Number of Non-Empty Values:", result)
