import gspread

from google.oauth2.service_account import Credentials

import random

from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bmw_Car_Orders')


list_of_questions = [
    "Can I see the cars in stores today?",
    "What cars are available in stores today?",
    "Can you show me the list of cars in stores today?"
]
bmw_list = [
    {'Make': 'BMW', 'Model': '1 Series', 'Colour': 'Red', 'FuelType': 'Disel'},
    {'Make': 'BMW', 'Model': 'M50', 'Colour': 'Blue', 'FuelType': 'Disel'},
    {'Make': 'BMW', 'Model': 'M2 Comp', 'Colour': 'Grey', 'FuelType': 'Petrol'}
]

descriptions = "is high quality with great endurance."

bmw_one = bmw_list[0]
bmw_two = bmw_list[1]
bmw_three = bmw_list[2]

# code from programiz to set current date and time.
time_date = datetime.now()
current_date = time_date.strftime("%H:%M - %d/%m/%Y")

final_choice = []
final_order = []


def initial_val():
    """
    This is the initial validation which asks users
    to enter Y if they would like to place an order
    and starts the ordering process. Otherwise, it 
    raises a ValueError and restarts.
    """
    while True:
        try:
            print("Enter 'Y' if Yes.")
            initial_question = input("Would you like to place an order? ").lower()

            if initial_question == 'y':
                print("\nPlease wait loading ... \n")
                break
            
            else:
                raise ValueError()

        except ValueError:
            print("Invalid data entered, please try again! \n")
            return all_functions()


def create_user_name():
    """
    This function would ask the user to enter a username
    5 characters long.
    """
    
    print("Username should begin with a capital letter.")
    print("Username should be 5 or more characters.")
    print("Username should only have letters and numbers. \n")
    print("You can always enter Q to quit/exit this process if needed. \n")
    
    while True:
        try:
            user_name = input("Enter a username you would like: ")
            
            if user_name.lower() == 'q':
                print("GoodBye for now :) \n")
                return all_functions()
            elif len(user_name) < 5:
                raise ValueError("Username name should have 5 or more values!")
            elif not user_name[0].isupper():
                raise ValueError("Username must begin with a Capital letter!")
            elif not user_name.isalnum():
                raise ValueError("Username can only have letters and numbers!")
            
            else:
                final_order.clear()
                print("Username is valid! :) \n")
                print("Now loading... \n")
                final_order.append(current_date)
                final_order.append(user_name)
                print(final_order)

                print(
                    f"Hello {user_name} and welcome to BMW click and collect. \n")
                break

        except ValueError as e:
            print(f"Invalid username: {e}, please try again!")
            continue


def user_location():
    """
    Prompts the user for their location.
    """
    print("(*) The name of City/Town must begin with a capital letter. \n")
    curr_location = str(input("What is the name of your City/Town? "))
    validate_location(curr_location)


def validate_location(cities):
    """
    This function validates user location
    function when users input data.
    """
    while True:
        try:
            if cities.lower() == "q":
                print("GoodBye for now :) \n")
                return all_functions()
            elif cities[0].isupper():
                print("Location confirmed! \n")
                final_order.append(cities)
                print(final_order)
                break
            elif not cities[0].isupper():
                raise ValueError("City/Town name must begin with a capital letter")
            #broke app
            else:
                raise ValueError('read instructions')

        except ValueError as e:
            print(f"Invalid data entered: {e}, please try again")
            return user_location()


def show_bmw():
    """
    Prompts the user to user a question.
    """
    print("Questions you can ask can be found below with (*) marked. \n")
    print("Each sentence must begin with a capital letter! \n")
    print("Each sentence must end with question mark! \n")
    print("Please ask the question beginning with a capital letter.")
    print("(*). Can I see the cars in stores today? \n")
    print("(*). What cars are available in stores today? \n")
    print("(*). Can you show me the list of cars in stores today? \n")
    print("You can always enter Q to quit/exit this process if needed. \n")
    while True:
        try:
            user_question = str(input("Ask a question! "))
            if user_question in list_of_questions:
                print("Here are the cars we have available in stores today.\n")
                for car in bmw_list:
                    print(f"{car} \n")
                break
            elif user_question.lower() == 'q':
                print("GoodBye for now :) \n")
                return all_functions()
                
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
            print("Or can enter 4 to quit/exit this process if needed. \n")
            pick_car = int(input("Which car are you interested in? "))
            final_choice.clear()

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

            elif pick_car == 4:
                print("GoodBye for now :) \n")
                return all_functions()

            else:
                raise ValueError("To choose one of the car from the list. Type 1, 2 or 3! \n")
        except ValueError as e:
            print(f"Invalid data entered: {e}")
            continue


def confirm_car_choice():

    print("\n Enter 'y' if Yes and 'n' if No.")
    print("You can always enter Q to quit/exit this process if needed. \n")
    confirm_choice = str(input("Is this the car you want? ")).lower()
    validate_car_choice(confirm_choice)


def validate_car_choice(data1):
    """
    This function validates the data passed to it 
    from the confirm car choice function. It checks
    if the user has entered y, n, or q and executes
    set tasks. Otherwise it raises a ValueError.
    """
    while True:
        try:
            if data1 == 'y':
                print("Great Choice! \n")
                break
            
            elif data1 == 'n':
                print('Not a problem \n')
                for car in bmw_list:
                    print(f"{car} \n")
                return choice_of_car()

            elif data1 == 'q':
                print("GoodBye for now :) \n")
                return all_functions()
            else:
                raise ValueError()

        except ValueError:
            print("Invalid data entered!")
            print(final_choice)
            return confirm_car_choice()


def show_features():
    print("Enter 'y' if Yes and 'n' if No.")
    car_features = str(input("Would you like to read more about this car? ")).lower()
    validate_show_features(car_features)


def validate_show_features(data2):
    while True:

        if data2 == 'y':
            if final_choice[0] == bmw_one or bmw_two or bmw_three:
                print(f"\nThis {final_choice[0]['Model']} {descriptions}")
            break
    
        elif data2 == 'n':
            print("Not a problem \n")
            break

        elif data2 == 'q':
            print("GoodBye for now :) \n")
            final_choice.clear()
            return all_functions()    

        else:
            print('Invalid data entered')
            show_features()


def make_order():
    """
    This function asks users if they want
    to place an order on the car they have 
    choosen.
    """
    print("Enter 'y' if Yes and 'n' if No.")
    place_order = str(input("Would you like to place an order? ")).upper()
    validate_order(place_order)


def validate_order(data3):
    """
    This function validates the data that is
    provided to the make order function. And 
    makes a decision after.
    """
    while True:
        if data3 == 'Y':
            print("Of course! \n")
            print("Your order is being prepared for collection ... \n")
            break
        
        elif data3 == 'N':
            print('Not a problem')
            #make a decision
            break

        elif data3 == 'Q':
            print("GoodBye for now :) \n")
            final_choice.clear()
            return all_functions()
        
        else:
            print("Invalid data entered, please try again.")
            return make_order()


def reference_num():
    """
    This function generates a random 7 digit
    number when called.
    """
    ref_num = random.randint(10000000, 99999999)
    final_order.append(ref_num)
    print(f"Your reference number is {final_order[3]}. Take this with you to the nearest BMW store in {final_order[2]} \n")


def send_order():
    """
    This function sends all the information so 
    google work sheet, which stores the data so
    the order can be prepared for the customer.
    """
    final_order.append(final_choice[0]['Make'])
    final_order.append(final_choice[0]['Model'])
    final_order.append(final_choice[0]['Colour'])
    final_order.append(final_choice[0]['FuelType'])
    
    bmw_worksheet = SHEET.worksheet('Collections')
    bmw_worksheet.append_row(final_order)
    print("Order Successful! \n")
    return all_functions()


def all_functions():
    """
    This function runs all the other functions
    """
    initial_val()
    create_user_name()
    user_location()
    show_bmw()
    choice_of_car()
    show_features()
    make_order()
    reference_num()
    send_order()


all_functions()
