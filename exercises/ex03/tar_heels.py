"""An exercise in remainders and boolean logic."""
__author__ = "730458275"


# Begin your solution here...
user_integer: int = int(input("Enter an int: "))
word = ""

if user_integer % 2 and user_integer % 7 != 0:
    word = "CAROLINA"
else: 
    if user_integer % 2 == 0:
        word = "TAR"
    if user_integer % 7 == 0:
        word = "HEELS"
    if user_integer % 14 == 0:
        word = "TAR HEELS"
print(word)
