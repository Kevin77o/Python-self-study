tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)

# there are two ways how to create a tuple
tuple_4 = (5, 4, 3, 3, 1)
# by using the tuple function, which takes string or list as an argument and returns tuple:
tuple_5 = tuple([3.14, 2.205, 10])  # list is an argument
tuple_6 = tuple("edcba")  # string is an argument
# print(tuple_5) # => (3.14, 2.205, 10)
# print(tuple_6) # => ('e', 'd', 'c', 'b', 'a')

# But there is no point in using a dictionary instead of a list or string, since if you do that,
# then only the keys will be made into a tuple.

# Each item in a tuple has an index number, just like the items in a list or characters in a string,
# thus you can also access values from a tuple by index or by slice like you can with lists or strings.
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(tuple_8[2]) # =>3
# print(tuple_8[:8]) # => (1, 2, 3, 4, 5, 6, 7, 8)
# print(tuple_8[2:7]) # =>(3, 4, 5, 6, 7)
# print(tuple_8[3:]) # =>(4, 5, 6, 7, 8, 9, 10)
# Unlike lists and dictionaries, tuples are an immutable data type, which means that they cannot be changed
# tuple_8[0] = "a"  # =>TypeError: 'tuple' object does not support item assignment
# Tuples are useful for when you want to have a collection of data that you know you will not change later
# tuple_12 = (1, 3, 5)
# list_1 = [1, 3, 5]
# print(tuple_12.__sizeof__())  # => 48
# print(list_1.__sizeof__())  # => 72

# The final instance where you would want to use a tuple over another data type is as a key in a dictionary.
# occupations = {("Angus", "Young"): "musician",
#                ("Narendra", "Modi"): "prime minister",
#                ("Richard", "Branson"): "entrepreneur",
#                ("Quentin", "Tarantino"): "filmmaker"}
# seven_wonders = {("29`58'44'N", "31`08'02'E"): "The Great Pyramid of Giza, Egypt",
                # ("33`13'23'N", "43`40'45'E"): "Hanging Gardens of Babylon"}
# Tuple looping
# how to iterate through a tuple using a for loop or a while loop, and how to slice tuples using step
# iterating through a tuple works the same way as for a list
#major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")
# FOR LOOP
# for city in major_cities: # where city is just a placeholder name for each element in the tuple
#     print(city) # => Tokyo
# London
# New York
# Shanghai
# Sydney
# WHILE LOOP
# count = 0
# while count < len(major_cities): #=> length = 5
#     print(major_cities[count]) #=> program will runr until index = 4 (0 to 4)
#     count += 1
# Tokyo
# London
# New York
# Shanghai
# Sydney

# another way using a while loop:
# backwards = len(major_cities) - 1
# while backwards >=0:
#     print(major_cities[count])
#     backwards -= 1
    # Tokyo
    # London
    # New York
    # Shanghai
    # Sydney

# TUPLE SLICING WITH STEP
# works the same as it does for strings and lists
ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3]) # stride length of 3 => (1, 4, 7, 10)
print(ints[1::2]) # evens only  =>  (2, 4, 6, 8, 10)
print(ints[7::-1]) # backwards from 8  => (8, 7, 6, 5, 4, 3, 2, 1)
print(ints[8::-2]) # odds only backwards  => (9, 7, 5, 3, 1)

# NESTED TUPLES
# nested tuples, which means that you can have a tuple or multiple tuples within another tuple
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
# Note that if you have a tuple within another tuple, all of the other items don't also need to be tuples.
# So this is also acceptable:
nested_2 = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
# Suppose that we want to get the second tuple from within the tuple assigned to nested_2.
print(nested_2[4]) # => (7, 8, 9)
# to get a single item from a tuple nested within another tuple, let's use the last tuple (10, 11, 12) and access 11
print(nested_2[5][1]) # =>11

# COUNT METHOD
#.count() returns the number of times that a value entered as its argument appears in a tuple
repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7)) # => 2
print(repeat.count(3)) # => 3
print(repeat.count(0)) # =>4

# INDEX METHOD
# If you know a value exists in a tuple but you don't know it's index number, you can enter it as an
# argument for the index method, which will return the index number you are looking for if it is found.
ints = (1, 1, 7)
print(ints.index(7)) # =>2
print(ints.index(1)) # =>0 - returns the index of the fist element found
print(ints.index(8)) # => ValueError: tuple.index(x): x not in tuple
