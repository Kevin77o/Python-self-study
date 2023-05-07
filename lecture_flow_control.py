# Comparison operators
# print(4 > 2)
# print(1 > 3)
# print(5.79 < 6)
# print(3 > 3)
# print("hello" == "hello")
# print("hello" != "world")

# != and == can be used to compare strings. Comparison is case-sensitive
# Floats and integers can be equivalent
# Boolean operators
# print(not 6482 > 0) # ->False
# print(not "Python" != "Python") # ->True

# I F  S T A T E M E N T
# veg = input("Type the name of a vegetable. ")
#
# if veg == "corn":
#     print("The vegetable is corn.")

# E L S E  S T A T E M E N T
# veg = input("Type the name of a vegetable. ")
#
# if veg == "corn":
#     print("The vegetable is corn.")
# else:
#     print("The vegetable is not corn.")

# nested I F and E L S E  S T A T E M E N T

# gpa = float(input("Type your GPA score with up to 1 decimal after.: "))
#
# if gpa < 3.7:
#     print("Declined, a person needs higher GPA to qualify.")
# else:
#     decision = input("Type Y or N to represent Instition decision.: ")
#     if decision == "Y":
#         print("Positive decision, a person qualifies for low APR loan.")
#     else:
#         if decision == "N":
#             print("Declined, a person doesn't qualify.")

# exercise 5.50
# score = int(input("Please enter student's score: "))
#
# if score >= 90:
#     print("Student's score is " + str(score) + " , which is A.")
# else:
#     if score >= 80:
#         print("Student's score is " + str(score) + " , which is B.")
#     else:
#         if score >=70:
#             print("Student's score is " + str(score) + " , which is C.")
#         else:
#             if score >= 60:
#                 print("Student's score is " + str(score) + " , which is D.")
#             else:
#                 print("Student's score is " + str(score) + " , which is F.")

# E L I F STATEMENT
# user_num = int(input("Please enter an integer: "))
#
# if user_num < 0:
#     print("The number you entered is less than 0")
# elif user_num == 0:
#     print("The number you entered is 0")
# elif 0 < user_num <= 100:
#     print("The number you entered can be 1, 100, or anything in between")
# else:
#     print("The number you entered is greater than 100.")


# exercise 5.50 with elif
# score = int(input("Please enter student's score: "))
# if score >= 90:
#     print("Student's score is " + str(score) + " , which is A.")
# elif score >= 80:
#     print("Student's score is " + str(score) + " , which is B.")
# elif score >= 70:
#     print("Student's score is " + str(score) + " , which is C.")
# elif score >= 60:
#     print("Student's score is " + str(score) + " , which is D.")
# else:
#     print("Student's score is " + str(score) + " , which is F.")


# exercise 5.53

# import random
# var_int = random.randint(1, 10)
#
# if var_int == 1:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'I'.")
# elif var_int == 2:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'II'.")
# elif var_int == 3:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'III'.")
# elif var_int == 4:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'IV'.")
# elif var_int == 5:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'V'.")
# elif var_int == 6:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'VI'.")
# elif var_int == 7:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'VII'.")
# elif var_int == 8:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'VIII'.")
# elif var_int == 9:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'IX'.")
# else:
#     print("The roman numeral equivalent of " + str(var_int) + " is 'X'.")

# truthy and falsy values. Empty string equals to a false value
# print(bool(""))
# print(bool(0))
# print(bool(0.0))

var_a = float(input("Please enter a float: "))
print(bool(var_a))
