"""Finding duplicate letters in a word."""
__author__ = "730458275"
word: str = input("Enter a word: ")
i = 0
k = 1
indexed_letter = "dog"
duplicates = False
while i < len(word):
    indexed_letter = (word[i])
    while k < len(word):
        if indexed_letter == (word[k]):
            duplicates = True
        k += 1
    i += 1
    k = i + 1
print("Found duplicate: " + str(duplicates))