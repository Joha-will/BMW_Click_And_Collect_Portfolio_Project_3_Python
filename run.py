import random


print("Hello and welcome to this game! \n")



def initial_val():
    """
    This is the initial validation so the user
    can input y or n to start the game.
    """
    print("Enter 'y' if Yes and 'n' if No.")
    initial_question = input("Would you like to try this game? ").lower()

    if initial_question == 'y':
        print("Game loading... \n")
    elif initial_question == 'n':
        quit()
    else:
        print("Invalid data entered, please enter 'y' if Yes or 'n' if No")
        return initial_val()


def create_user_name():
    





initial_val()
