"""Drawing forests in a loop."""

__author__ = "730458275"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
times: int = int(input("Depth: "))
Counter: int = 0
i = 0
cycles = times - 1
statement = ""
while i < cycles:
    if times >= 0:
        while Counter < times:
            statement = statement + TREE
            Counter += 1
            print(statement)
    statement = ""
    times = 0  
    i += 1
