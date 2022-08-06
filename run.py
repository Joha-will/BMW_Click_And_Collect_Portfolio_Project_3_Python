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
list_of_questions = [
    "Can I see the BMW's in stores today",
    "What cars are available in stores today",
    "Can you show me the list of cars in stores today"
]
bmw_list = [
    {'Make': 'BMW', 'Model': '1 Series', 'Colour': 'Red', 'FuelType': 'Disel'},
    {'Make': 'BMW', 'Model': 'M50', 'Colour': 'Blue', 'FuelType': 'Disel'},
    {'Make': 'BMW', 'Model': 'M2 Comp', 'Colour': 'Grey', 'FuelType': 'Petrol'}
    ]

bmw_one = bmw_list[0]
bmw_two = bmw_list[1]
bmw_three = bmw_list[2]


def initial_val():
    """
    This is the initial validation so the user
    can input y or n to start the game.
    """
    print("Enter 'y' if Yes and 'n' if No.")
    initial_question = input("Would you like to place an order? ").lower()

    if initial_question == 'y':
        print("Please wait loading ...\n")
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
    print("\nQuestions you can ask. \n")
    print("(*). Can I see the BMW's in stores today \n")
    print("(*). What cars are available in stores today \n")
    print("(*). Can you show me the list of cars in stores today \n")
    while True:
        try:
            user_question = str(input("Ask a question! "))
            if user_question in list_of_questions:
                print("Here are the cars we have available in stores today.\n")
                for car in bmw_list:
                    print(f"{car} \n")
                break
                
            else:
                print("this is not it")
                raise ValueError("This is not it")
        except ValueError as e:
            print(f"This is not it {e}")
            continue


def choice_of_car():
    """
    This function ask the user for their choice of car
    and ask them to input 1,2 or 3 based on the list of
    cars shown.
    """
    print("To choose one of the car from the list. Type 1,2 or 3! \n")
    while True:
        try:
            pick_car = int(input("Which car are you interested in? "))
            if pick_car == 1:
                print(f"bmw_one \n")

            elif pick_car == 2:
                print(f"bmw_two \n")

            elif pick_car == 3:
                print(f"bmw_three \n")

            else:
                raise ValueError("To choose one of the car from the list. Type 1,2 or 3! \n")
            
        except ValueError as e:
            print(f"Invalid data entered: {e}")
            continue         


def all_functions():
    """
    This function runs all the other functions
    """
    initial_val()
    create_user_name()
    show_bmw()
    choice_of_car()


all_functions()
