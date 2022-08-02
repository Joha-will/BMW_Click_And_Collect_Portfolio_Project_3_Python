import random


print("Hello and welcome to this game! \n")

print("Enter y for Yes and n for No.")
initial_question = input("Would you like to try this game? ").lower()


def initial_val():
    """
    This is the initial validation so the user
    can input y or n to start the game.
    """
    if initial_question != 'y' or 'n':
        print("Invalid data entered, please enter valid data!")
