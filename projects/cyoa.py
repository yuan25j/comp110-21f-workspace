"""Choose your Own Adventure Game."""
__author__ = "730458275"
from random import randint
points: int = 0 
player: str = ""
NAMED_CONSTANT = "\U0001F600"
checkmark = "\U00002714"
wrong = "\U0000274C"


def main() -> None:
    """Main Function, starts the program and operates as menu for game.""" 
    greet() 
    global points
    choice = input("What would you like to do first Please choose a number 1-3.\n1. Guess the Number \n2. Double or Nothing \n3. End Game")
    while choice != "3":
        if choice == "1":
            option_one()
        elif choice == "2":
            points = option_two(points)
        else:
            print(f"{wrong}Choose a valid response.")
        choice = input("1. Guess the Number \n2. Double or Nothing \n3. End Game")
    if choice == "3":
        game_end()


def greet() -> None:
    """Greets the player and collets the name."""
    global player
    player = input("What is your name")
    print(f"Welcome, {player},{NAMED_CONSTANT} This is my fun python game!")


def option_one() -> None:
    """Option one for RNG to obtain points."""
    number_chosen: str = input(f"Hello, {player}, please choose a number 1-5.")
    random_number: str = str(randint(1, 5))
    global points
    while random_number != number_chosen:
        new_number: str = input(f"{wrong}Try another number!")
        number_chosen = new_number
    if random_number == number_chosen:
        points = points + 5
        print(f"{checkmark}You got 5 points! Choose another option!")
    

def option_two(x: int) -> int:
    """Option 2 to double or lose all your points by solving an equation."""
    num_1: int = randint(1, 10)
    num_2: int = randint(1, 10)
    operator: int = randint(1, 3)
    guess: str = "" 
    symbol: str = ""
    if operator == 1:
        guess = str(num_1 + num_2)
        symbol = "+"
    if operator == 2:
        guess = str(num_1 - num_2)
        symbol = "-"
    if operator == 3:
        guess = str(num_1 * num_2)
        symbol = "*"
    print(f"Solve the following equation {player}: {num_1} {symbol} {num_2}")
    answer: str = input("What is your answer?")
    if answer != guess:
        x = 0
        print(f"{wrong}You got it wrong, you lost all of your points")
    if answer == guess:
        print("You got it!")
        print(f"{checkmark}You doubled your points!")
    
    return int(x * 2)

    
def game_end() -> None:
    """Ends the game."""
    global points
    print(f"Goodbye, Your total points are {points}")


if __name__ == "__main__":
    main()
