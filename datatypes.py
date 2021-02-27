# DATATYPES LESSON
# Python Data Types from Basic to Advanced
# 1. Booleans
# 2. Numbers
# 3. Strings
# 4. Bytes
# 5. Lists
# 6. Tuples
# 7. Sets
# 8. Dictionaries

# 1. Booleans
condition = False
if condition == True:
    print("You can continue with the prpgram.")
else:
    print("The program will end here.")
# skip the explicit comparison, same result
condition = False
if condition:
    print("You can continue with the prpgram.")
else:
    print("The program will end here.")

# if condition:
#    is equivalent to,
# if condition == True:

str = "Learn Python"
len(str)
# 12
len(str) == 12
# True
len(str) != 12
# False

A, B = True + 0, False + 0
print(A, B)
# 1
# 0
type(A), type(B)
# (<class 'int'>, < class 'int' > )


# 2. Numbers

#The numbers in Python are classified using the following keywords.
# int, float, and complex.
# Python has a built- in function type() to determine the data type of a variable or the value.
# Another built- in function isinstance() is there for testing the type of an object.
# In Python, we can add a “j” or “J” after a number to make it imaginary or complex.
# Example.

num = 2
print("The number (", num, ") is of type", type(num))

num = 3.0
print("The number (", num, ") is of type", type(num))

num = 3+5j
print("The number ", num, " is of type", type(num))
print("The number ", num, " is complex number?", isinstance(3+5j, complex))
# Output
# The number ( 2 ) is of type <class 'int'>
# The number(3.0) is of type <class 'float'>
# The number(3 + 5j) is of type <class 'complex'>
# The number(3 + 5j) is complex number? True
# example below.
complex(1.2, 5)
# (1.2 + 5j)
num = 1234567890123456789
num.bit_length()
# 61
num
# 1234567890123456789
num = 1234567890123456789123456789012345678912345678901234567891234567890123456789
num.bit_length()
# 250
num
# 1234567890123456789123456789012345678912345678901234567891234567890123456789
# A float type number can have precision up to 15 decimal places.
import sys
sys.float_info
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
sys.float_info.dig
# 15
# Note – The dig in above example is the maximum number of decimal digits in a float.

# 3. Strings
# one or more characters enclosed within either single quotes ‘ or double quotes ” is considered as String in Python.
# multi - line strings which require a triple quotation mark at the start and one at the end.

str = 'A string wrapped in single quotes'
str
# 'A string wrapped in single quotes'
str = "A string enclosed within double quotes"
str
# 'A string enclosed within double quotes'
str = """A multiline string
starts and ends with
a triple quotation mark."""
str
# 'A multiline string\nstarts and ends with\na triple quotation mark.'

# #########
# Strings in Python are immutable. It means the memory will be allocated once and re - used thereafter.
# #########
A = 'Python3'
id(A)
# 56272968
B = A
id(B)
# 56272968

# Strings in Python 2.
print(type('Python String'))
# < type 'str' >
print(type(u'Python Unicode String'))
# < type 'unicode' >

# Strings in Python 3.
print(type('Python String'))
# < class 'str'>
print(type(u'Python Unicode String'))
# <class 'str'>

# Python allows slicing strings
str = "Learn Python"
first_5_chars = str[0:5]
print(first_5_chars)
# Learn
substr_from_2_to_5 = str[1:5]
print(substr_from_2_to_5)
# earn
substr_from_6_to_end = str[6:]
print(substr_from_6_to_end)
# Python
last_2_chars = str[-2:]
print(last_2_chars)
# on
first_2_chars = str[:2]
print(first_2_chars)
# Le
two_chars_before_last = str[-3:-1]
print(two_chars_before_last)
# ho

# 4. Bytes
# The byte is an immutable type in Python.It can store a sequence of bytes(each 8 - bits) ranging from 0 to 255.
# Make an empty bytes object (8-bit bytes)
empty_object = bytes(16)
print(type(empty_object))
# <class 'bytes'>
print(empty_object)
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# buf = b''
# while message_not_complete(buf):
#     buf += read_from_socket()

# 5. Lists
# Python list is an array like construct which stores arbitrarily typed objects in an ordered sequence.
# It is very flexible and does not have a fixed size.Index in a list begins with zero in Python.

assorted_list = [True, False, 1, 1.1, 1 + 2j, 'Learn', b'Python']
first_element = assorted_list[0]
print(first_element)
# True
print(assorted_list)
# [True, False, 1, 1.1, (1 + 2j), 'Learn', b'Python']
for item in assorted_list:
    print(type(item))
# <class 'bool'>
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'str'>
# <class 'bytes'>

simpleton = ['Learn', 'Python', '2']
id(simpleton)
# 56321160
simpleton
# ['Learn', 'Python', '2']
simpleton[2] = '3'
id(simpleton)
# 56321160
simpleton
# ['Learn', 'Python', '3']

# Nesting inside a list
# Interestingly, a list can contain another list.Such a list is called as the nested list.
nested = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
for items in nested:
    for item in items:
        print(item, end=' ')
# 1
# 1
# 1
# 2
# 2
# 2
# 3
# 3
# 3

# Slicing a list
# With the slicing operator[], we can extract an element or a bunch of them from a list.
languages = ['C', 'C++', 'Python', 'Java', 'Go', 'Angular']
print('languages[0:3] = ', languages[0:3])
# languages[0:3] = ['C', 'C++', 'Python']
print('languages[2:] = ', languages[2:])
# languages[2:] = ['Python', 'Java', 'Go', 'Angular']

# 6. Tuples
# A tuple is a heterogeneous collection of Python objects separated by commas.
# It means objects of different data types can co - exist in a tuple.
# The tuple and a list are somewhat similar. Both objects are an ordered sequence. They enable indexing and repetition.
# Nesting is allowed. They can store values of different types.

# Python tuple syntax
# Example – Define a tuple
# Defining a tuple without any element
pure_tuple = ()
print(pure_tuple)
# Output- ()

# Example – Nested tuples
# Creating a tuple with nested tuples
first_tuple = (3, 5, 7, 9)
second_tuple = ('learn', 'python 3')
nested_tuple = (first_tuple, second_tuple)
print(nested_tuple)
# Output - ((3, 5, 7, 9), ('learn', 'python 3'))

# Example – Repetition in tuples
# How does repetition work with tuples
sample_tuple = ('Python 3',) * 3
print(sample_tuple)
# Output - ('Python 3', 'Python 3', 'Python 3')

# Example – Slicing in tuples
# How does slicing work with tuples
sample_tuple = (0, 1, 2, 3, 4)
tuple_without_first_item = sample_tuple[1:]
print(tuple_without_first_item)
tuple_reverse = sample_tuple[::-1]
print(tuple_reverse)
tuple_from_3_to_5 = sample_tuple[2:4]
print(tuple_from_3_to_5)
# Output -
# (1, 2, 3, 4)
# (4, 3, 2, 1, 0)
# (2, 3)

# Tuples do differ a bit from the list as they are immutable.Python does not allow to modify a tuple after creation
# Why need a Tuple as one of the Python data types?
# Python uses tuples to return multiple values from a function. Tuples are more lightweight than lists.
# It works as a single container to stuff multiple things. We can use them as a key in a dictionary.

# 7. Sets
# The set is one which supports mathematical operations like union, intersection, symmetric difference etc.
# A set is an unordered collection of unique and immutable objects.
# Its definition starts with enclosing braces {} having its items separated by commas inside.

# Why need a set?
# Set vs. List. It implements a highly optimized method that checks whether the container hosts a specific element
# or not.The mechanism used here is based on a data structure known as a hash table.

# Creating a set
sample_set = set("Python data types")
type(sample_set)
# <class 'set'>
sample_set
# {'e', 'y', 't', 'o', ' ', 'd', 's', 'P', 'p', 'n', 'h', 'a'}
another_set = {'red', 'green', 'black'}
type(another_set)
# <class 'set'>
another_set
# {'red', 'green', 'black'}

# Frozen set
# A frozen set is a processed form of the traditional set.
# It is immutable and only supports methods and operators that executes without altering the frozen set used in the context.
# An empty frozenset
frozenset()
# frozenset()
cities = {"New York City", "Saint Petersburg", "London", "Munich", "Paris"}
fset = frozenset(cities)
type(fset)
# <class 'frozenset'>
# Difference between a normal and the frozen set.
# Python program to demonstrate frozen set
# A standard set
sample_set = {"red", "green"}
# Add an element to the standard set
sample_set.add("black")
print("Standard Set")
print(sample_set)
# A frozen set
frozen_set = frozenset(["red", "green", "black"])
print("Frozen Set")
print(frozen_set)
# Output -
# Standard Set
# {'green', 'red', 'black'}
# Frozen Set
# frozenset({'green', 'red', 'black'})

# 8. Dictionaries
# A dictionary in Python is an unordered collection of key - value pairs.
# It’s a built - in mapping type in Python where keys map to values.
# These key - value pairs provide an intuitive way to store data.

# Why need a dictionary?
# The dictionary solves the problem of efficiently storing a large data set.
# Python has made the dictionary object highly optimized for retrieving data.

# Creating a dictionary
sample_dict = {'key': 'value', 'jan': 31, 'feb': 28, 'mar': 31}
type(sample_dict)
# <class 'dict'>
sample_dict
# {'mar': 31, 'key': 'value', 'jan': 31, 'feb': 28}

# Accessing dictionaries elements with keys
# Dictionaries act like a database.Here, we don’t use a number to get a particular index value as we do with a list.
# Instead, we replace it with a key and then use the key to fetch its value.
sample_dict['jan']
# 31
sample_dict['feb']
# 28

# Dictionaries methods to access elements
# keys() – It isolates the keys from a dictionary.
# values() – It isolates the values from a dictionary.
# items() – It returns the items in a list styleof(key, value) pairs.
sample_dict.keys()
# dict_keys(['mar', 'key', 'jan', 'feb'])
sample_dict.values()
# dict_values([31, 'value', 31, 28])
sample_dict.items()
# dict_items([('mar', 31), ('key', 'value'), ('jan', 31), ('feb', 28)])

# Modifying a dictionary(Add / update / delete)
sample_dict['feb'] = 29
sample_dict
# {'mar': 31, 'key': 'value', 'jan': 31, 'feb': 29}
sample_dict.update({'apr': 30})
sample_dict
# {'apr': 30, 'mar': 31, 'key': 'value', 'jan': 31, 'feb': 29}
del sample_dict['key']
sample_dict
# {'apr': 30, 'mar': 31, 'jan': 31, 'feb': 29}