# Example of List in Python

# Creating a list
my_list = [1, 2, 6, 7, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2
print(my_list[-1])  # Output: 5

# Slicing a list
print(my_list[1:4])  # Output: [2, 6, 7]
print(my_list[3:])  # Output: [7, 3, 4, 5]
print(my_list[:3])  # Output: [1, 2, 6]

# Changing elements in a list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 6, 7, 3, 4, 5]

# Adding elements to a list
my_list.append(8)
print(my_list)  # Output: [10, 2, 6, 7, 3, 4, 5, 8]

# Removing elements from a list
my_list.remove(2)
print(my_list)  # Output: [10, 6, 7, 3, 4, 5, 8]

# Sorting a list
my_list.sort()
print(my_list)  # Output: [3, 4, 5, 6, 7, 8, 10]

# Looping through a list
for i in my_list:
    print(i)        # Output: 3 4 5 6 7 8 10

# Concatenating two lists
temp_list = [1, 2, 3, 4, 5]
my_list.extend(temp_list)
print(my_list)  # Output: [3, 4, 5, 6, 7, 8, 10, 1, 2, 3, 4, 5]


# Removing elements from a list using pop() method
my_list.pop(-1)  
        # Output: 5
print(my_list)  # Output: [3, 4, 6, 7, 8, 10, 1, 2, 3, 4]


# quick way to copy a list using copy() method
temp_list = my_list.copy()
print(temp_list)  # Output: [3, 4, 6, 7, 8, 10, 1, 2, 3, 4]

