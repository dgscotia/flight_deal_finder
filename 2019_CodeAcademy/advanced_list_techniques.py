my_dict = {
    'animal type': 'dog',
    'weight in kg.': 8,
    'name': 'Rover',
    'age': 11
}

print my_dict.items() # prints the keys and values as tuples
print my_dict.keys() # only prints the keys in a list
print my_dict.values() # only prints the values in a list

for key in my_dict:
    print key, my_dict[key]

# LIST COMPREHENSION
# prints all even values to 50
print [i for i in range(51) if i % 2 == 0]

even_squares = [x ** 2 for x in range (11) if x % 2 == 0]
print even_squares

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print cubes_by_four

to_21 = range(22)
odds = to_21[1::2]
middle_third = to_21[8:15]
print middle_third

# Anonymous Functions - FUNCTIONAL PROGRAMMING
# Use LAMBDA to avoid giving functions a name.
print lambda x: x % 3 == 0
# is the same as
def by_three(x):
    return x % 3 == 0

# filter() - takes two arguments, FUNCTION and ITERABLE, and returns a list of elements from the iterable for which the function returns True.
my_list = range(16)
print "Look here"
print filter(lambda x: x % 3 == 0, my_list)

squares = [x ** 2 for x in range(1,11)]
print filter(lambda y: 30 <= y <= 70, squares)

threes_and_fives = [x for x in range(1,16) if (x % 3 == 0 or x % 5 == 0)]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
print garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda y: y != 'X', garbled)