"""Counting letters in a string."""

__author__ = "730458275"


# Begin your solution here.

letter: str = input(" What letter do you want to seach for?: ")
word: str = input("Enter a word: ")
i = 0
final = 0
while i < len(word):
    if letter == (word[i]):
        final += 1
    i += 1
final_print = str(final)
print("Count: " + final_print)