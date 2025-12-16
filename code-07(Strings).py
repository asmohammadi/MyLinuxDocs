my_str = 'Hello, I want to learn Python'
print(my_str[4])

my_str[4] = 'i' # Error, cannot assign anything to the piece of String

my_str = my_str[:4] + 'i' + my_str[5:] # Correct version
print(my_str)

my_str = 'Hello, I want to learn Python'
print(my_str.upper()) # Using Method

my_str = 'Hello, I want to learn Python'
print(my_str.lower()) # Using Method

my_str = 'Hello, I want to learn Python'
print(my_str.split()) # Using Method

my_str = 'Hello, I want to learn Python'
print(my_str.split('e')) # Using Method (Seperator)

my_str = 'a, b, c, d'
print(my_str.split(',')) # Using Method (Seperator)
