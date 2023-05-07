#print("Hello world")


# Lecture8 L I S T S

# lists can be assigned to variables
# example_list_1 = [5, 4, 3, 2, 1]
# example_list_2 = [2.718, 9.31]
# example_list_3 = ["blue", "green", "red", "yellow", "purple", "orange"]
# example_list_4 = [True, False, False, True, True, True]
# example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]  # is known as a list of lists
# example_list_6 = [10, 3.141592, "tree", False, [1, 2, 3]]

# function list() takes str and converts it into list
# print(list("blah")) #['b', 'l', 'a', 'h']

# in and not in operators
# checked_list = [1, 2, 3, 4]
# print(1 in checked_list) # True
# not_in_ex = 8 in checked_list # False
# print(not_in_ex)

# exercise 8.84
# var1 = [12, 3.145, False, "str", [-1, 15, 2]] # a list of items of different data types assigned to a variable
# var2 = list("Hello") # another variable assigned a call of  list() function with a string "Hello" as a argument
# print("e" in var2) #check if the letter "e" is in the list assigned to var2 and print True/False =>True
# print("a" not in var2) #check if the letter "a" is not in the list assigned to var2 and print True/False =>True

# I N D E X E S in the list
# starts with 0
# indexes_ex = ["carpet", "hardwood", "linoleum"]
# to access "hardwood"
# print(indexes_ex[1])
# access of a list inside another list
# indexes_ex = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# print(indexes_ex[2][0]) # => 6
# indexes_ex1 = ["carpet", "hardwood", "linoleum"]
# print(indexes_ex1[2][0]) # => l

# negative indexes
# negative = [1, 2, 3, 4, 5]
# print(negative[-1]) # => 5
# print(negative[-2]) # => 4
# print(negative[-3]) # => 3
# print(negative[-4]) # => 2
# print(negative[-5]) # => 1

# using items accessed by index in expressions
#print("I have used \"" + mixed[-1] + "\" as a nexample too many times.")

# list slicing
#sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sliced [:4]) # => [1, 2, 3, 4]
# print(sliced [3:8]) # => [4, 5, 6, 7, 8]
# print(sliced [6:]) # => [7, 8, 9]
# print(sliced [1:-1]) # => [2, 3, 4, 5, 6 7, 8]

# reassigning a list's items
# example = [2, 4, 6, 8, 0]
# print(example)
# reassign a value held by an index number:
#example[3] = 10 # 8 -> 10
#print(example)
# reassign multiple values by using a slice:
# print(example) # [2, 3, 2, 1, 0]
# example[4:7] = [7, 6, 5] #[0, , ] -> [7, 6, 5]
# print(example) # [2, 4, 6, 8, 7, 6, 5]

# exercise 8.87
# var1 = [[0, 2], [4, 6], [8, 10], [12, 14]] # assigning a list of lists to a variable var1
# # access the first list of var1 by index and then print it:
# print(var1[0])
# # access the 14 of var1 and print it:
# print(var1[-1][-1])
# var2 = ["chair", "table", "desk", "lamp", "bed"] # creating var2 and assigning a list to it
# print(var2[-5])
# # Print "Most people own at least 2 chairs." where 2 is taken from var2 and chair from var2
# print("Most people own at least " + str(var1[0][-1]) + " " + var2[0] + "s.")
# var3 = [0.98, 8.76, 6.54, 4.32] # assign a list to var3
# # Print the slice [8.76, 6.54, 4.32] from var3
# print(var3[1:])
# # Print the slice [8.76, 6.54] from var3
# print(var3[1:3])
# # Print the slice [0.98, 8.76] from var3
# print(var3[:2])

# del and list methods
# used on list data type
# del statement allows to delete values from a list
# planets = ["pluto", "mars", "earth", "venus"]
# del planets[0]
# print (planets) # => ["mars", "earth", "venus"]

# .remove()
# planets = ["pluto", "mars", "earth", "venus"]
# planets.remove("pluto")
# print (planets) # => ["mars", "earth", "venus"]

# when you try to remove a value used multiple times in a list,
# then .remove("value") will delete only the first instance of the value

# .append() list method - takes argument and adds it to the end of the list
# pets = ["cat", "dog", "parrot"]
# print(pets)
# pets.append("fish")
# print(pets) # => ['cat', 'dog', 'parrot', 'fish']

# .insert() adds an item to the list, but anywhere in the list (unlike .append())
# pets = ["cat", "dog", "parrot"]
# pets.insert(1, "turtle")
# print(pets)

# .sort() method used to sort items in the list, where all items are numbers or strings
# num_list = [2.718, 4, -19, 10000, 0]
# print(num_list)
# num_list.sort()
# print(num_list) # =>[-19, 0, 2.718, 4, 10000]

# str_list = ["Ringo", "John", "George", "Paul"]
# print(str_list)
# str_list.sort()
# print(str_list)  # => ['George', 'John', 'Paul', 'Ringo']

# reverse=True - to sort in the reverse order
# num_list = [2.718, 4, -19, 10000, 0]
# num_list.sort(reverse=True)
# print(num_list) # =>[10000, 4, 2.718, 0, -19]
#
# str_list = ["Ringo", "John", "George", "Paul"]
# str_list.sort(reverse=True)
# print(str_list)  # => ['Ringo', 'Paul', 'John', 'George']

# mixed = [0, False, 5.67, -2]
# mixed.sort()
# print(mixed) # => [-2, 0, False, 5.67]

# ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
# ASCIIbetical.sort()
# print(ASCIIbetical) # => ['Andy', 'Brian', 'Karen', 'apple', 'banana', 'kiwi']
# ASCIIbetical.sort(key=str.lower)
# print(ASCIIbetical) # => ['Andy', 'apple', 'banana', 'Brian', 'Karen', 'kiwi']

# .index() method allows to find the index no. of the item
# planets = ["pluto", "mars", "earth", "venus"]
# print(planets.index("pluto")) # => 0

# .index() method on an item that appears multiple times => only the index no. of the fist instance will be returned
# num = [4, 3, 2, 1, 0, 1, 2, 3, 4]
# print(num.index(1)) # => 3

# .pop() -as del statement removed the last item from the list. But retrns the resut, can be assigned to a variable
# bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
# end = bands.pop()
# print(bands) # => ['Queen', 'Led Zeppelin', 'The Beatles', 'MUSE']
# print(end) # => Radiohead

# using index as an argument for .pop()
# bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
# end = bands.pop(3)
# print(bands) # => ['Queen', 'Led Zeppelin', 'The Beatles', 'Radiohead']
# print(end) # => MUSE

# exercise 8.90
# 1) Create a variable called arctic_animals and
# assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# # 2) Use del to remove "tiger" from the list assigned to arctic_animals.
# del arctic_animals[4]
# # print(arctic_animals)
# # 3) Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
# arctic_animals.remove("elephant")
# # print(arctic_animals)
# # 4) Use the .append() method to add the string "arctic fox" to the list arctic_animals.
# arctic_animals.append("arctic fox")
# # print(arctic_animals)
# # 5) Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
# arctic_animals.insert(2, "snowy owl")
# #print(arctic_animals) # => ['penguin', 'polar bear', 'snowy owl', 'walrus', 'reindeer', 'arctic fox']
# # 6) Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
# arctic_animals.sort()
# print(arctic_animals) # =>['arctic fox', 'penguin', 'polar bear', 'reindeer', 'snowy owl', 'walrus']
# # 8) Use .index() to get the index number of "reindeer" from arctic_animals then print it.
# reindeer_index = arctic_animals.index("reindeer")
# print(reindeer_index) # => 3
# # 9) Use .pop() to get the last item from the list arctic_animals then print it.
# last_item = arctic_animals.pop()
# print(last_item)

# copy module and deepcopy()
# import copy
# ex_12 = [1, 2, 3, 4, 5]
# ex_13 = copy.deepcopy(ex_12) # assigns a new reference to the list
# ex_13[2] = 4
# ex_14 = ex_13
# ex_14[4] = 6
# print(ex_12) # => [1, 2, 3, 4, 5]
# print(ex_13) # => [1, 2, 4, 4, 6]

# list line continuation
# ex_15 = ["bush",
#          "fern",
#          "tree",
#          "moss"]
# print(ex_15) # => ['bush', 'fern', 'tree', 'moss']

# \ line continuation
ex_16 = 2 + \
        4 + \
        1
print(ex_16) # => 7
