import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bmw_Car_Orders')

city = []


def initial_val():
    """
    This is the initial validation so the user
    can input y or n to start the game.
    """
    print("Enter 'y' if Yes and 'n' if No.")
    initial_question = input("Would you like to place an order? ").lower()

    if initial_question == 'y':
        print("Game loading... \n")
    elif initial_question == 'n':
        print("GoodBye for now :) \n")

    else:
        print("Invalid data entered, please try again! \n")
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
                raise ValueError("Username name should have 5 or more values!")
            elif not user_name[0].isupper():
                raise ValueError("Username must begin with a Capital letter!")
            elif not user_name.isalnum():
                raise ValueError("Username can only have letters and numbers!")
            else:
                print("Username is valid! :)\n")
                print("Now loading...\n")
                print(
                    f"Hello {user_name} and welcome to BMW click and collect.")
                break

        except ValueError as e:
            print(f"Invalid username: {e}, please try again!")
            continue


def show_bmw():
    """
    Prompts the user to user a question.
    """
    list_of_question = ["Can I see the BMW's in stores today", "What cars are available in stores today", "Can you show me the list of cars in stores today"]
    print("Questions you can ask. \n")
    print("(*). Can I see the BMW's in stores today \n")
    print("(*). What cars are available in stores today \n")
    print("(*). Can you show me the list of cars in stores today \n")
    while True:
        try:
            user_question = input("Ask a question! :)")

            for question in list_of_question:
                if user_question != num:
                    print("Try asking one of the questions above!")
                    continue
                else:
                    break




