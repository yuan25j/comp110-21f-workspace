"""Numeric Operator Program, takes two numbers, does mathematical calclations"""

__author__ = "730458275"

left = input("Left-hand side:")
right = input("Right-hand side:")
left_int = int(left)
right_int = int(right)
print(left + " ** " + right + " is " + str(left_int**right_int))
print(left + " / " + right + " is " + str(left_int/right_int))
print(left + " // " + right + " is " + str(left_int//right_int))
print(left + " % " + right + " is " + str(left_int%right_int))