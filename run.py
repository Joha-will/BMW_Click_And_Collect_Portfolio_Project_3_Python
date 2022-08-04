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
        print("GoodBye for now :)")
        quit()
    else:
        print("Invalid data entered, please enter 'y' if Yes or 'n' if No")
        return initial_val()


def create_user_name():
    """
    This function would ask the user to enter a username
    5 characters long.
    """
    while True:
        try:
            user_name = input("Enter a username you would like: ")

            if len(user_name) < 5:
                raise ValueError
            elif not user_name[0].isupper():
                raise ValueError
            elif not user_name.isalnum():
                raise ValueError
            else:
                print("Username is valid! :)")
                break

        except ValueError:
            print("Please enter valid username.")
            continue


initial_val()
create_user_name()
