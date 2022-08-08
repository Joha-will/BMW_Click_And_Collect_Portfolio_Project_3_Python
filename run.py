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
    "Can I see the BMW's in stores today?",
    "What cars are available in stores today?",
    "Can you show me the list of cars in stores today?"
]
bmw_list = [
    {'Make': 'BMW', 'Model': '1 Series', 'Colour': 'Red', 'FuelType': 'Disel'},
    {'Make': 'BMW', 'Model': 'M50', 'Colour': 'Blue', 'FuelType': 'Disel'},
    {'Make': 'BMW', 'Model': 'M2 Comp', 'Colour': 'Grey', 'FuelType': 'Petrol'}
    ]

bmw_one = bmw_list[0]
bmw_two = bmw_list[1]
bmw_three = bmw_list[2]

final_choice = []


def initial_val():
    """
    This is the initial validation so the user
    can input y or n to start.
    """
    print("Enter 'y' if Yes and 'n' if No.")
    initial_question = input("Would you like to place an order? ").lower()
    while True:

        if initial_question == 'y':
            print("Please wait loading ... \n")
            break
        elif initial_question == 'n':
            print("GoodBye for now :) \n")
            continue

        else:
            print("Invalid data entered, please try again! \n")
            return initial_val()


def create_user_name():
    """
    This function would ask the user to enter a username
    5 characters long.
    """
    print("Username should begin with a capital letter. \n")
    print("Username should be 5 or more characters. \n")
    print("Username should only have letters and numbers. \n")
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
                print("Username is valid! :) \n")
                print("Now loading... \n")
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
    print("Questions you can ask. \n")
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
    while True:
        try:
            print("To choose one of the car from the list. Type 1,2 or 3! \n")
            pick_car = int(input("Which car are you interested in? "))

            if pick_car == 1:
                print(f"{bmw_one} \n")
                final_choice.append(bmw_one)
                print(final_choice)
                return confirm_car_choice()

            elif pick_car == 2:
                print(f"{bmw_two} \n")
                final_choice.append(bmw_two)
                print(final_choice)
                return confirm_car_choice()

            elif pick_car == 3:
                print(f"{bmw_three} \n")
                final_choice.append(bmw_three)
                print(final_choice)
                return confirm_car_choice()

            else:
                raise ValueError("To choose one of the car from the list. Type 1, 2 or 3! \n")
        except ValueError as e:
            print(f"Invalid data entered: {e}")
            continue


def confirm_car_choice():

    print("Enter 'y' if Yes and 'n' if No.")
    confirm_choice = str(input("Is this the car you want? ")).lower()
    validate_car_choice(confirm_choice)


def validate_car_choice(data1):
    while True:

        if data1 == 'y':
            print("Great Choice! \n")
            break
            
        elif data1 == 'n':
            print('Not a problem \n')
            final_choice.clear()
            for car in bmw_list:
                print(f"{car} \n")
            choice_of_car()
        else:
            print("Invalid data! \n")
            confirm_car_choice()


def show_features():
    print("Enter 'y' if Yes and 'n' if No.")
    car_features = str(input("Would you like to read more about this car? "))
    validate_show_features(car_features)


def validate_show_features(data2):
    while True:

        if data2 == 'y':
            print()
            break
    
        elif data2 == 'n':
            print("Not a problem")
    
        else:
            print('Invalid data entered')
            show_features()


def all_functions():
    """
    This function runs all the other functions
    """
    initial_val()
    create_user_name()
    show_bmw()
    choice_of_car()
    show_features()


all_functions()
