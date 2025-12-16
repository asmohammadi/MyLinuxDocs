# Normal Dictionary:
my_dict = {"key1": 1, "key2": 2}

# Best way for Reading:
my_dict = {
    "key1": "hello",
    "key2": [1,2,3]
}

print(my_dict['key2']) # Get dictionary
print(my_dict['key2'][1]) # Get a list index from dictionary

# Example:
my_dict = {"key1": 1, "key2": {"a": [2,3,4], "b": 5}, "key3": ["a", "b", "c"]}
print(my_dict['key2']['a'][2])

# Change Dictionary:
my_dict = {"key1": 1, "key2": {"a": [2,3,4], "b": 5}, "key3": ["a", "b", "c"]}
print(my_dict)
my_dict['key1'] = 'hello'
print(my_dict)


# Example:
my_stu = {
    "name": "ali", 
    "age": 30, 
    "mark": 18
}
print(my_stu['name'])

# Add item to dictionary:
my_stu = {
    "name": "ali", 
    "age": 30, 
    "mark": 18
}
my_stu["aa"] = 'aa'
print(my_stu)

# Get all keys/values/items:
my_stu = {
    "name": "ali", 
    "age": 30, 
    "mark": 18
}
print(my_stu.keys())
print(my_stu.values())
print(my_stu.items()) # Display in Tupple mode
