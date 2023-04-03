# lists

# array = lists

# First List = shopping list
# [] = list
shopping_list = ["milk", "bread", "eggs", "chocolate", "jam" ]
print(type(shopping_list))

print(shopping_list)

# Accessing a particular part of the list

print(shopping_list[1])

# Change an element in a list
shopping_list[2] = "butter"
print(shopping_list)

# Using list methods

#adding to a list with append ()
shopping_list.append("fish")
print(shopping_list)

# removing items with remove()

shopping_list.remove("bread")
print(shopping_list)

# removing the last item from the list, without specifying

shopping_list.pop()
print(shopping_list)

# Can I have a list with mixed data types? YES
mixture = [1, 2, 3, 4.5, "five", "six"]
print(mixture)

# Slicing
print(mixture[:4])

# Reverse the order of the slice
print(mixture[-3::])

# Step over
print(mixture[::2])

# Tuples

# Tuples are IMMUTABLE - cannot be changed

tuple_example = ("bread", "eggs", "milk")
print(tuple_example)

# Dictionaries

# Another way to manage data but they are a little bit more dynamic
# Key value pairs

# Key = reference to the object
#Value = data storage mechanism(i.e. String, Int, List, Dictionary)

student_1 = {
    "name": "fatima",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "setup"]
    }

print(student_1["name"])

# Access a part of the list in the dictionary

print(student_1["completed_lesson_names"][0])

# Changing a value in a dictionary
student_1["completed_lessons"] = 3

print(student_1["completed_lessons"])

# Changing an element within a dictionary

student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())

# Sets and Frozen sets

# set in python is a list that has no order/indexing

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

car_parts.add("windows")
print(car_parts)

car_parts.discard("doors")
print(car_parts)

# Frozen sets
x = frozenset([1, 2, 3, 4])
x.add(5)
print(x)