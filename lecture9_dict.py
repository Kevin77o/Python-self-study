# Introduction to dictionaries
# console = {"nintendo": "will"}
# consoles = {"nintendo": "will", "microsoft": "xbox", "sony": "playstation"}
# print(consoles["microsoft"])
# val = consoles["microsoft"]
# print(val)
# print("The " + consoles["sony"] + " 4 is Sony's newest gaming console.")
#
# # key values
# mohs_hardness = {9: "curundum", 10: "diamond"}
# floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
# mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}

# dictionaries are unordered
# print([2, 4, 6] == [2, 4, 6]) # => True
# print([2, 4, 6] == [6, 4, 2]) # => False
#
# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
# print(first == second) # => True

# IN and NOT IN operators to check if a key exists withing a dictionary
# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# print(0 in first) # => True
# print(1 not in first) # => False

# exercise 9.94
# dic = {1: "open", -5: "close", 0: False, "OK": 1.23, 5: True}
# print(dic[0])
# print(False in dic)
# print("close" not in dic)

# Dictionary Methods .keys(), .values(), .items(), .get()
# .keys()
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years.keys()) # -> dict_keys([1994, 1969, 1982, 2000])
# # usage of for operator to iterate through keys of a dictionary:
#
# for key in birth_years.keys():
#     print(key) # -> 1994, 1969, 1982, 2000 (but in a column)
# .values()
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years.values()) # -> dict_values(['bil', 'emily', 'elizabeth', 'turner'])
# for values in birth_years.values():
#      print(values) # -> bil emily elizabeth turner (but in a column)
#.items() method allows to get the values and the keys of a dictionary at the same time
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years.items()) # -> returns a list of tuples, i.e. dict_items([(1994, 'bil'), (1969, 'emily'), (1982, 'elizabeth'), (2000, 'turner')])
# for key, value in birth_years.items():
#     print(key, value) # ->
    # 1994 bil
    # 1969 emily
    # 1982 elizabeth
    # 2000 turner

# print(type(birth_years.keys())) #-> <class 'dict_keys'>
# print(type(birth_years.values())) #-> <class 'dict_values'>
# print(type(birth_years.items() )) #-> <class 'dict_items'>
#
# print(list(birth_years.keys())) #-> [1994, 1969, 1982, 2000]
# print(list(birth_years.values())) #-> ['bil', 'emily', 'elizabeth', 'turner']
# print(list(birth_years.items() )) #-> [(1994, 'bil'), (1969, 'emily'), (1982, 'elizabeth'), (2000, 'turner')]

#Using in and not in with values mathod
# check if birth_years contains value elizabeth:
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print ("elizabeth" in birth_years.values()) #=> True

#.get() method can look for a key in a dictionary and return something other than an error message
# and the program won't end
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# if 1975 in birth_years:
#     print(birth_years[1975])
# else:
#     print("1975 is not a key in birth_years.") # => 1975 is not a key in birth_years.
# # now the same with just one line of code using .get() method
# print(birth_years.get(1994, "1975 is not a key in birth_years.")) #=> bil

# other things about dictionaries
# 1) dict are mutable as lists
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years)
# people = birth_years
# people[1982] = "madeline"
# print(birth_years)
#
# # if a dict gets too long it can be distributed into several lines:
# birth_years = {1994: "bil",
#                1969: "emily",
#                1982: "elizabeth",
#                2000: "turner"}
# len() functiona to get the number of key-value pairs of a disc
# print(len(birth_years)) #=> 4

# exercise 9.97
# 1) create a variable and assign it to a dict, 2) make the dict span multiple lines
# dict_hits = {"Queen": "Bohemian Rhapsody",
#              "Bee Gee": "Stayin' Alive",
#              "U2": "One",
#              "Michael Jackson": "Billie Jean",
#              "The Beatles": "Hey Jude",
#              "Bob Dylan": "Like A Rolling Stone"
#              }
# # 3) print the length of the dict
# print(len(dict_hits)) # => 6
# # 4) use the .keys() method and
# # a for loop to get and print all of the keys from
# # the dictionary on separate lines.
# for key in dict_hits.keys():
#     print (key)
# # 5) print all of the values from the dictionary using the .values() method.
# print(dict_hits.values())
# # 6) use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
# for key, value in dict_hits.items():
#     print (key, value)
# # 7) use the .get() method to check the dictionary for the key
# #
# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.
# print(dict_hits.get("Promise of the Real","'Promise of the Real' is not found in the dictionary"))

# 9.99 Dictionary methods

# .fromkeys()

# .pop()

# .popitem()

# .fromkeys()
# method returns the dictionary using two values that it was given as arguments,
# the first argument it takes is used as keys and the second argument is used as a value.
# ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
# When you use .fromkeys(), it should be used on an empty dictionary, which is just represented by a set
#of empty curly brackets.
# Like with any other method, you just type period, then the name of the method to call .fromkeys().
# .fromkeys() can take one or two arguments when you call it.
# The first argument needs to be an iterable value, such as a list or string.
# Each item in that iterable value will be used as a key for the dictionary that from Keys will return.
# I'll just use a single item list with the string address in it for this example.
# The second arguments will be used as a value by the dictionary that .fromkeys() returns.
# It can be a value that is of any data type, whether it's an integer float, boolean value, list, string
# or even another dictionary.
# Given these two arguments .fromkeys() will generate a dictionary with one key value pair.
# print(ex_1) # => {'address': '1600 Pennsylvania Avenue NW'}
# if we change a list to a string in the key, then each character will become a key:
# ex_2 = {}.fromkeys("ad", "1600 Pennsylvania Avenue NW")
# print(ex_2) # => {'a': '1600 Pennsylvania Avenue NW', 'd': '1600 Pennsylvania Avenue NW'}
# # Also, each character or item in an iterable can only be used as a key one time.
# ex_3 = {}.fromkeys("addr", "1600 Pennsylvania Avenue NW")
# print(ex_3) # => {'a': '1600 Pennsylvania Avenue NW', 'd': '1600 Pennsylvania Avenue NW', 'r': '1600 Pennsylvania Avenue NW'}
# # If there is no 2nd argument in .fromkeys(), then None will be in the result
# ex_4 = {}.fromkeys(["brand"])
# print(ex_4) #=> {'brand': None}

# .pop() method
# The .pop() method does the same thing to dictionaries that it does to lists, it removes an item where
# an item in a dictionary is a key value pair.
# However, it is a bit of a different situation for dictionaries, since you can't just call pop on a
# dictionary with no argument and then have it remove the last key value pair.
# This is due to the fact that dictionaries are unordered.
# ex_5 = {"make": "Honda", "model": "civic", "year": 2016}
# # ex_5.pop("model")
# # print(ex_5) # => {'make': 'Honda', 'year': 2016}
# # the pop method also returns the value of the key value pair that has been removed.
# popped = ex_5.pop ("model")
# print(popped) # => civic
# # Also, if you try to use the .pop() method on a key that doesn't exist.
# # Then you will get a key error message.
# ex_5.pop("type")
# print(ex_5) # => KeyError: 'type'

# .popitem()
# allows you to remove the last key value pair from a dictionary without having
# to give it an argument.
# ex_6 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
# ex_6.popitem()
# print(ex_6) #=> {'name': 'bob', 'age': 38, 'occupation': 'accountant'}
# # .popitem() takes no arguments
# ex_6.popitem("name") # => TypeError: dict.popitem() takes no arguments (1 given)

# exercise 9.100
# 1. use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and
# the string "consonant" as the value for each of those keys.
# Only use lower case letters for the consonants.
# "y" counts as a consonant for this exercise.
# Use a for loop and the .items() method to print each of those key: value pairs on a different line.
# dict_consonants = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
# for key, value in dict_consonants.items():
#     print (key, value)
# # 2. paste this dictionary into your .py file then pop and print "Big Mac" from it
# #
# # fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# print(fast_food_items.pop("McDonald's")) #=> Big Mac
# # 3. use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items
# # then print new fast_food_items dictionary.
# fast_food_items.popitem()
# for key, value in fast_food_items.items():
#     print (key, value)

# Dictionary methods .clear(), .copy(), .update()
# The clear method just removes everything from a dictionary that it is called on, resulting in an empty
#
# dictionary, the clear method takes no arguments.
#
# So if we wanted to use it on this dictionary, we would just type the dictionary name clear parentheses.
# ex_1 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
# print(ex_1)
# ex_1.clear()
# print(ex_1) # => {}
# .copy()
# previous example:
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years) #=> {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# people = birth_years
# people[1982] = "madeline"
# print(birth_years) #=> {1994: "bil", 1969: "emily", 1982: "madeline", 2000: "turner"}
# so in this example by modifying people, we modified birth_years
# same thing using .copy() method:
# birth_years = {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# print(birth_years) #=> {1994: "bil", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# people = birth_years.copy()
# people[1982] = "madeline"
# print(birth_years) #=> {1994: 'bil', 1969: 'emily', 1982: 'elizabeth', 2000: 'turner'}

# .update() method allows us to add key value pairs from one dictionary
# to another or overwrite the values of existing keys in a dictionary with values
# from another dictionary

#city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
# population = {"population": 2930000}
# Update takes one argument, which is the dictionary that you want key value pairs to be added from.
# city_info.update(population)
# # print(city_info) # => {'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'population': 2930000}
# # print(population) # => {'population': 2930000}
# city_info["population"] = 3000000
# print(city_info) # =>{'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'population': 3000000}
# city_info.update(population)
# print(city_info) # =>{'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'population': 2930000}
# update with empty dictionary as its argument:
# city_info.update({})
# print(city_info) # => {'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto'}

# exercise 9.103
# Do all of this in a .py file in Pycharm.
#
# 1. paste these 2 dictionaries into your file
#
# a. internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# b. another_one = {"shroud": "Twitch"}
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# # 2. use .update() to add the contents of another_one to internet_celebrities.
# internet_celebrities.update(another_one)
# # 3. create a variable and assign it a copy of internet_celebrities.
# copy_IC = internet_celebrities.copy()
# # 4. use the .clear() method to get rid of the contents of internet celebrities.
# internet_celebrities.clear()
# # 5. print internet_celebrities.
# print(internet_celebrities) #=> {}
# # 6. print the variable you created in step 3.
# print(copy_IC) #=>{'DrDisrespect': 'YouTube', 'ZLaner': 'Facebook', 'Ninja': 'Mixer', 'shroud': 'Twitch'}

# .setdefault() method is useful for when you go through a dictionary and look for keys, only to find that
# certain keys that you are looking for don't exist.
# computers = {"Google": "CjromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
# # if "Lenovo" not in computers:
# #     computers["Lenovo"] = "ThinkPad"
# # print(computers) # => {'Google': 'CjromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}
# # same result with .setdefault() method, but in a more compact view
# computers.setdefault("Lenovo", "ThinkPad")
# print(computers) # => {'Google': 'CjromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}
# computers.setdefault("Lenovo", "IdeaPad")
# print(computers) # =>{'Google': 'CjromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}

# dict() function aka dect function gives you an alternative way to create a dictionary in Python
empty = dict()
print(empty) #=> {}
with_values = dict(a1=1, b_=2, c_3=3)
print(with_values)#=>{'a1': 1, 'b_': 2, 'c_3': 3}