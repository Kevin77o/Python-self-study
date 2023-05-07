# def function_name(parameter):
#     print(parameter + 2)
#
#
# var_1 = 3
# function_name(var_1)
#first_str = "The number "


# def function_name1(p1, p2, p3):
#     print(p1 + str(p2) + p3)
#
#
# function_name1(first_str, 5, " is an integer.")
#
# def default_ex (num1=7, num2=8):       # assigning default parameters, no spaces before and after '='
#     print(num1 * num2)
#
#
# default_ex ()     # the outcome is 7*8=56
# default_ex (2)    # the outcome is 2*8=16


# if we want to not only print the result of a function, but use it, then we need 'return' and assign a call of the function to a variable or use it in the expression
# def default_ex (num1=7, num2=8):       # assigning default parameters, no spaces before and after '='
#     return num1 * num2
#
#
# product = default_ex(2)


# exercise 3.33
# def hello_world_printer ():
#     print("hello world")
#
# hello_world_printer ()
# exercise 3.34
# def name_printer(par1):
#     print(par1)
#
#
# name = input("Please enter your name ")
# name_printer(name)

# exercise 3.37
# length = int(input("Please enter length as integer "))
# width = int(input("Please enter width as integer "))
# height = int(input("Please enter height as integer "))
#
#
# def volume (l=length, w=width, h=height):
#     return length * width * height
#
#
# print("The volume of the rechtangular prism is " + str(volume()) + " cubic feet")

# exercise 3.39 Celsius to Fahrenheit with integers

# user_temp_C = int(input("Please enter temperature in Celsius as integer value "))
#
#
# def fahrenheit (C_temp):
      # to avoid the approximation error that would occur if the float 1.8 was used in  the calculation, 1.8*10 is used
      # instead, resulting in the integer 18. To balance this out, 32 is also multiplied by 10.
      # After the calculations in the parentheses are finished, the result is divided by 10, which gives the correct
      # Fahrenheit temperature
#     return (1.8*C_temp*10 + 32*10) / 10
#
#
# print("The Fahrenheit equivalent of " + str(user_temp_C) + " degrees Celsius is " + str(fahrenheit(user_temp_C)) + ".")

# exercise 3.39 Celsius to Fahrenheit with round()

# user_temp_C = int(input("Please enter temperature in Celsius as integer value "))
#
#
# def fahrenheit (C_temp):
#     # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
#     # after the decimal point
#     return round((1.8*C_temp + 32), 1)
#
#
# print("The Fahrenheit equivalent of " + str(user_temp_C) + " degrees Celsius is " + str(fahrenheit(user_temp_C)) + ".")

# M O D U L E S
# generic import
# random module is used for creating random things such as random floats or integer values
#
# import random
#
# print(random.randint(1, 10)) # the output will be a random integer equal to 1, 10 or any other integer between 1 and 10


# function import
# from random import randint
# print(randint(10, 20))

# universal import
# from random import * #every function from a random module has been imported
#
# print(random()) #returns a flot that is greater than or equal to 0.0 and less than 1.0

# exercise 3.43
# a program that approximates the number of miles per gallon that a car gets
# from random import randint
#
# gallon_num = randint(10, 25)
# print(gallon_num)
# miles_num = randint(200, 400)
# print(miles_num)
#
#
# def MPG(miles, gallon):
#     return miles // gallon
#
#
# print("MPG is approximately equal to " + str(MPG(miles_num, gallon_num)) + " miles per gallons.")

# Variable scope. Global statements used if you want to use a global variable inside a function


def loc_ex():
    global fruit
    fruit = "pear"
    print (fruit)


loc_ex()   # the outcome is pear as the function uses global variable and changes its value
fruit = "apple"
print(fruit) # the outcome is apple as the variable has changed the value after the call of the function