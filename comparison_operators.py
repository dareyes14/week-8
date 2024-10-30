
#Comparison operators
# Logical operators
# Decision making
# loops(for loops, while loops, range, enumerator)
# min/max practice
# Random in python
# List comprehension


# review practice
# Append the value of current to the end of the list seconds Please use the list.append() method to do that.


seconds = [1.23, 1.45, 1.02]
current = 1.11

# Remove item 1.45 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]


# Remove items 1.45, 1.02, and 1.11 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]

#print(seconds)
# #remmove item 1.45 from seconds
# seconds.remove(1.45)
print(seconds)
for i in seconds:
    if i ==1.45 or i == 1.02 or i == 1.11:
        seconds.remove(i)
        print(seconds)

################################comparison operators#########################
#remember....
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to




# Comparison Operators Practice  1:
# Create two variables (num1 and num2) with the following values: 36 and 17. Check if num1 is greater than or equal to num2 and store the result of that comparison in a variable called my_bool

# num1 = 36
# num2 = 17

# my_bool = num1 >= num2
# print(my_bool)

# # Comparison Operators Practice  2:
# # Create two variables (num1 and num2):
# # Inside num1, store the result of the square root of 25
# # Inside num2, store the number 5.
# # Check if num1 is equal to num2 and store the result of that comparison in a variable called my_bool.
# import math 

# num3 = math.sqrt(25)
# num4 = 5

# my_bool2 = num3 == num4
# print(my_bool2)

# # Comparison Operators Practice #3:
# # Create two variables (num1 and num2):

# # Inside num1, store the result of 64 x 3

# # Inside num2, store the result of 24 x 8

# # Check if num1 is different from num2 and store the result of that comparison in a variable called my_bool.

# num5 = 64*3
# num6 = 24*8
# my_bool3 = num5 != num6
# print(my_bool3)


#######################comparison operators challenge#####################
# Challenge: Compare two numbers entered by the user and check if they are equal or not.
# If they are not equal, print which one is greater.

# Prompt the user for two numbers

# # Check for equality and greater number

# num7 = input("Choose a number: ")
# num8 = input("Choose another number: ")
# if num7 > num8:
#     print(f'{num7} is greater than {num8}')
# elif num8 > num7:
#     print(f'{num8} is greater than {num7}')
# elif num7 == num8:
#     print(f'{num7} equal {num8}')
# elif num8 == num7:
#     print(f'{num8} equal {num7}')