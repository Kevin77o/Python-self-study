# A set is a data type that consists of a collection of items, much like a list.
# The first is that they cannot have duplicate values in them, and the second is that the items they
# contain are unordered, like the key value pairs of a dictionary.
# HOW TO CREATE
# there 2 basic ways:
# set_1 = {9, 8, 7, 6}
# set_2 = set({"a", "b", "c", "d", "e"})
# print(set_1) # => {8, 9, 6, 7}
# print(set_2) # => {'a', 'c', 'd', 'b', 'e'}

# dublicate items will be ignored and will only appear once in the set
set_111 = {9, 8, 8, 8, 7, 6}
#print(set_111) # =>{8, 9, 6, 7}

# if you want to create an empty set that you can change later, you have to use the set function to create an empty set.
# Since just using an empty set of curly brackets creates a dictionary instead of a set to create an empty
set_empty = set() # will create an empty set
dict_empty = {} # will create an empty dictionary

# to get all of the odd positive integers from one to 12 using a range
set_3 = set(range(1, 12, 2))
# print(set_3) # => {1, 3, 5, 7, 9, 11}
# # a set can hold items that are of different data types
# set_4 = {"a", 3.14, 18, True}
# print(set_4) #=> {True, 18, 3.14, 'a'}
# Unlike lists or tuples, sets cannot have their items accessed from them by index.
# So if you want to acceess an element from a set, you have to use a for loop:
set_5 = {3, 6, 9, 12, 15}
# for num in set_5:
#     print(num)
    # 3
    # 6
    # 9
    # 12
    # 15
# print(12 in set_5) # True
# print(10 in set_5) # False
# WHEN SETS ARE USEFUL
#Sets are useful in situations where you want to use a collection of items, but you don't want duplicate

# SET METHODS
# .add() method takes an item of any data type as its arguments and adds that to the set.
# scifi = {"star trek", "star wars", "halo"}
# scifi.add("mass effect") # => {'star trek', 'star wars', 'mass effect', 'halo'}
# print(scifi)
# scifi.add("star wars")
# print(scifi) # => nothing has been changed and no error message, i.e. {'mass effect', 'star wars', 'star trek', 'halo'}

# .remove() method takes one arguments of any data type and removes that item from the set that it is called on.
# fruits = {"apple", "orange", "banana", "tomato"}
# fruits.remove("tomato")
# print(fruits) # => {'orange', 'banana', 'apple'}
# fruits.remove("pear")
# print(fruits) # => error message

# .discard() does the same thing as remove and also takes one argument.
# The difference is that if discard is used on a piece of data that is not in a set, it will just do nothing instead of giving back an error message.
# fruits.discard("pear")
# print(fruits) # => {'banana', 'apple', 'orange'}, i.e. no error message
# fruits.discard("apple")
# print(fruits) # => {'orange', 'banana'}

# .clear() takes no arguments and just gets rid of everything in the set that it is called on,
# mountains = {"Everest", "Kilimanjaro", "Fuji"}
# print(mountains) # => {'Kilimanjaro', 'Fuji', 'Everest'}
# mountains.clear()
# print(mountains) # => set()

# .copy() returns a copy of a set that has its own place in memory.
mountains = {"Everest", "Kilimanjaro", "Fuji"}
set_copy = mountains.copy()
print(set_copy is mountains) # => False, that means that the copy and the original set are not the same set, although
# hat it has the same values as the set, it is a copy of
print(set_copy) # => {'Kilimanjaro', 'Fuji', 'Everest'}

# .union() method combines all of the items from two different sets into a single set
# set_11 = {1, 2, 3, 4, 5}
# set_22 = {6, 7, 8, 9, 10}
# set_33 = set_11.union(set_22)
# print(set_33) # => {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# alternatively to combine sets we can use a pipe character
# set_33 = set_11 | set_22
# print(set_33) # => {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# .intersection() a method which allows you to find out what items two sets have in common, which is
# also known as their intersection
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
# set_3 = set_1.intersection(set_2)
# print(set_3) # => {8, 6, 7}
# alternatively using &
# set_3 = set_1 & set_2
# print(set_3) # => {8, 6, 7}

# subtraction and .difference()
# you can subtract one set from another based on the items that make up their intersection or, in other words,
# what they have in common.
# from the previous example
# set_3 = set_2 - set_1
# print(set_3) # => {9, 10}

# set_3 = set_1 - set_2
# print(set_3) # => {4, 5}
# .difference() method does the same thing
set_3 = set_1.difference(set_2)
print(set_3) # => {4, 5}

# SET COMPREHENSIONS
# this is a third slightly more advanced way to create a set
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1) # => {4, 6, 8, 10, 12}
# 1) the entire thing must be enclosed in curly brackets to signal to Python that it is a set.
# 2) there is a for loop that goes over an iterable data type such as a range or string.
# 3) there is an action that is done to each item that the for loop iterates over.
# That action could be a math operation or a method call.

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2) # => {'s', 'l', 'p', 'a', 'c'}
# In this example, the for loop iterates through all of the letters in the string, all caps, before
# each item is added to the set, it is made lowercase using the lower method.









