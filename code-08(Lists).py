my_list = [13, 'hello', 18.1, 'c', -1, 100] # Using Bracket & Comma for list
print(my_list[0])

# Indexing:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
another_list = [1,2,3,4,5]
print(my_list + another_list)


my_list = [13, 'hello', 18.1, 'c', -1, 100]
another_list = [1,2,3,4,5]
my_list = my_list + another_list
print(my_list)

# Slicing:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
another_list = [1,2,3,4,5]
print(another_list[1:3])
print(another_list[::2])

# Get the Length of List
my_list = [13, 'hello', 18.1, 'c', -1, 100]
print(len(my_list))

# Change an item in the list:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
my_list[4] = 22
print(my_list)


# Using Method:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
my_list.append(14)
print(my_list)

# Using POP Method:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
my_list.pop() # Remove the last item
print(my_list)

my_list = [13, 'hello', 18.1, 'c', -1, 100]
popped_item = my_list.pop() # Keep the removed item
print(my_list)
print(popped_item) # Display the removed item

my_list = [13, 'hello', 18.1, 'c', -1, 100]
my_list.pop(1) # Remove the second item
print(my_list)

# Using Sort Method:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
list_of_numbers = [4,0,100,-9,5]
list_of_numbers.sort() # Sort the numbers
print(list_of_numbers)

# Using Reverse Method:
my_list = [13, 'hello', 18.1, 'c', -1, 100]
list_of_numbers = [4,0,100,-9,5]
list_of_numbers.sort()
list_of_numbers.reverse()
print(list_of_numbers)

