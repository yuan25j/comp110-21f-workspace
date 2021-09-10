"""Repeating a beat in a loop."""

__author__ = "730458275"

# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
Counter: int = 0
beat = " " + beat
statement = ""
if times <= 0:
    print("No beat...")
else:
    while Counter < times:
        statement = statement + beat
        Counter += 1
print(statement)
