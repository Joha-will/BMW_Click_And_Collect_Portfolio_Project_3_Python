from datetime import datetime
import random
import os
import time
import sys
import colorama
from colorama import Back
import gspread
from google.oauth2.service_account import Credentials

colorama.init(autoreset=True)

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

DESCRIPTION = "is ultramodern luxury car with the latest features and "\
    "technologies.\nOne of the things that make this car stand out is the "\
    "attention to detail.\nThere is no doubt you will enjoy this car. "

bmw_one = bmw_list[0]
bmw_two = bmw_list[1]
bmw_three = bmw_list[2]

# code from programiz to set current date and time.
time_date = datetime.now()
current_date = time_date.strftime("%H:%M - %d/%m/%Y")

final_choice = []
final_order = []


def print_text(text):
    """
    This code is from
    www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def clear_terminal():
    """
    This function clears/refreshes the
    terminal when users quit or completes
    the ording process.
    """
    os.system('clear')


def welcome_logo():
    """
    This function displays a bmw
    logo to the users.
    """
    print("██████╗ ███╗   ███╗██╗    ██╗   ██████╗██╗     ██╗ ██████╗██╗  ██╗")
    print("██╔══██╗████╗ ████║██║    ██║  ██╔════╝██║     ██║██╔════╝██║ ██╔╝")
    print("██████╔╝██╔████╔██║██║ █╗ ██║  ██║     ██║     ██║██║     █████╔╝ ")
    print("██╔══██╗██║╚██╔╝██║██║███╗██║  ██║     ██║     ██║██║     ██╔═██╗ ")
    print("██████╔╝██║ ╚═╝ ██║╚███╔███╔╝  ╚██████╗███████╗██║╚██████╗██║  ██╗")
    print("╚═════╝ ╚═╝     ╚═╝ ╚══╝╚══╝    ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝")
    print("                     █████╗ ███╗   ██╗██████╗     ")
    print("                     ██╔══██╗████╗  ██║██╔══██╗    ")
    print("                     ███████║██╔██╗ ██║██║  ██║    ")
    print("                     ██╔══██║██║╚██╗██║██║  ██║    ")
    print("                     ██║  ██║██║ ╚████║██████╔╝    ")
    print("                     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ")
    print("     ██████╗ ██████╗ ██╗     ██╗     ███████╗ ██████╗████████╗")
    print("    ██╔════╝██╔═══██╗██║     ██║     ██╔════╝██╔════╝╚══██╔══╝")
    print("    ██║     ██║   ██║██║     ██║     █████╗  ██║        ██║   ")
    print("    ██║     ██║   ██║██║     ██║     ██╔══╝  ██║        ██║   ")
    print("    ╚██████╗╚██████╔╝███████╗███████╗███████╗╚██████╗   ██║   ")
    print("     ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ")
    print("                              ╓▄╗╗╗▀▀▀▀▀▀▀▀▀▀═──┬╤▄")
    print("                          ▄██╜   ▄███████▀   ▌▓█  ╫██▄")
    print("                      ╓▄██▀   ▄███████▀     ▐│█   ██ ╟▌▀▄")
    print("                    ▄██▀   ╓███████▀     ▄███▐▌┌ ╠▀╫▐╚ ┌─█")
    print("              ▄╗═▀╬└░░░╡░░░╠╙╙╙▀▀▀╙╙╙╙╜▀▀▀▀▀┌▐████▀▀╓═   ▐")
    print("         ╓╗▀╙╙╔░         ╚┘       ╓╔┌─  ─     ╔ ╚▄─ ╓┌▒ ▓▐")
    print("      ▄▀╙─ ░░         ╧     ╓┌╔░╛  ┌ ░╔░═  ─  ┌  ╔░╓╗╣╬╗█▐")
    print("   ▄█               ╛  ╔┌░░░┴ ┌┌░░░ │┘╓╔─  ╓░╓╦░▄▒╬╬╝╬╟██▐")
    print("  ╓█║  ╘  ░┬╚░░░░  ░┌░  ░░╔░▒│   ░╜░░  ╧┌▄▓▓▒╒█╬╬╝╙ ╬╠██▌")
    print("  ▌ ╟████▄ ╣▀ ░░│  ░░ │░░─┬═▄▄▄╧╚╝▀██░╛╔██ █▌╟╬╜ ╓╩▄██▀")
    print("  ▌░ └████▌█████████▓████▌█╦▄╔█▌█╓█▀─░║███▌ ▌╬▒╦╬███╙")
    print("  ╙▒╕░┌┐╙▀▀╙████████▀░░░╙─═╩▀▀▀░░░░  ║████▌ █╬▄██▀")
    print("   ▌▓╟▄    ░░╔╔╔╔┌ ░░░░░░░░╦░░░  │  ▐╫▌███▌ ███▀")
    print("   █▒▌╚█████▄▄▄      ═──═══└░└╚ ╚▄  ╬█▌███ ╟█▀")
    print("   ╙▀██▄╙╚╩╠████████▌╘▒▓████████▌╙▒╠╟████▀┌")
    print("       ╙▀▀███▄╠╠╙╚╩╬▄┘╠╙╙╙▀▀▀▀▀▀▀░╠╬████▄═")
    print("              ╙▀▀▀██████▄▄▄██████████▀▀└")
    print("                        └╙╙╙╙╙╙╙")


def initial_val():
    """
    This is the initial validation which asks users
    to enter Y if they would like to place an order
    and starts the ordering process. Otherwise, it
    raises a ValueError and restarts.
    """
    while True:
        try:
            print_text("Would you like to place an order?\n")
            initial_question = input("Enter 'Y' if Yes. \n").lower()

            if initial_question == 'y':
                print_text("\nPlease wait loading ...")
                print("\n")
                break

            else:
                raise ValueError()

        except ValueError:
            print_text("Invalid data entered, please try again! \n")
            clear_terminal()
            return all_functions()


def create_user_name():
    """
    This function asks users to enter a username name.
    Then it validates it by checking if it begins with
    a capital letter, if the length is correct and if
    it's made up of letters and numbers. Once the
    username has met the requirment it then proceeds
    to the next step or it raises a ValueError to let
    users know what they are doing wrong. It also enables
    users to quit/exit ordering process by enter Q.
    """
    while True:
        print_text('\n')
        print_text("Username should begin with a capital letter.\n")
        print_text("Username should be 3 or more characters.\n")
        print_text("Username should only have letters and numbers. \n")
        print_text("You can enter Q to quit/exit this process at any time. \n")
        print('\n')
        try:
            final_order.clear()
            user_name = input("Enter a username you would like:\n")

            if user_name.lower() == 'q':
                return quit_func()

            elif len(user_name) < 3:
                raise ValueError("Username name should have 3 or more values!")

            elif not user_name[0].isupper():
                raise ValueError("Username must begin with a Capital letter!")

            elif not user_name.isalnum():
                raise ValueError("Username can only have letters and numbers!")

            else:
                print_text("Username is valid! :)")
                print_text("\n")
                final_order.append(current_date)
                final_order.append(user_name)
                print_text("\n")
                print_text(f'Hi {user_name}, welcome to BMW click & collect.')
                print('\n')
                break

        except ValueError as e:
            print(f"{Back.RED}Invalid username: {e}, please try again!")
            continue


def user_age():
    """
    This function asks user for their age.
    """
    print_text("Please enter your age below.\n")
    print_text("You can enter Q to quit/exit this process at any time. \n")
    print("\n")
    ask_for_age = input("How old are you? \n")
    validate_age(ask_for_age)


def validate_age(your_age):
    """
    This function validates the data passed to it from
    the user_age function. If for their age is more
    than 18 it continues the ordering process. If their
    age is less than 18 the process ends.
    """
    while True:
        try:
            if your_age.lower() == 'q':
                return quit_func()

            elif not your_age.isdigit():
                raise ValueError("Age must only be numbers!")

            if len(your_age) > 2:
                raise ValueError("Age cannot be more than 2 numbers!")

            elif int(your_age) < 17:
                print_text(f"Sorry {final_order[1]} you are not old enough.\n")
                return quit_func()

            else:
                print_text("Age confirmed! \n")
                break
        except ValueError as e:
            print(f"{Back.RED}{e}")
            return user_age()


def user_location():
    """
    This function asks users to input their
    town/city.
    """
    print("\n")
    print_text("The name of City/Town must begin with a capital letter. \n")
    print_text("You can enter Q to quit/exit this process at any time. \n")
    print('\n')
    curr_location = str(input("What is the name of your City/Town?\n"))
    validate_location(curr_location)


def validate_location(cities):
    """
    This function validates user location
    function when users input data.
    """
    while True:
        try:
            if cities.lower() == "q":
                return quit_func()

            elif not cities[0].isupper():
                raise ValueError("Town name must begin with a capital letter")

            else:
                print_text("\nCity/Town confirmed! \n")
                final_order.append(cities)
                break

        except ValueError as e:
            print(f"{Back.RED}Invalid data entered:City/{e}, please try again")
            return user_location()


def show_bmw():
    """
    This function instructs the users to enter one of the questions showed
    below. Once entered correctly, it displays a list of cars available.
    """
    print('\n')
    print_text("Please ask one of the questions listed below marked (*). \n")
    print_text("Each sentence must begin with a capital letter! \n")
    print_text("Each sentence must end with question mark! \n")
    print_text("Please ask the question beginning with a capital letter. \n")
    print('\n')
    print_text("(*). What cars are available in stores today? \n")
    print_text("(*). Can you show me the list of cars in stores today? \n")
    print_text("You can enter Q to quit/exit this process at any time. \n")
    while True:
        try:
            user_question = str(input("Ask a question!\n"))
            if user_question in list_of_questions:
                print('\n')
                print_text("Here is a list of the cars that are available.")
                print('\n')
                for car in bmw_list:
                    print(f"{car} \n")
                    print("""
--------------------------------------------------------------------------
                    """)
                break
            elif user_question.lower() == 'q':
                return quit_func()

            else:
                raise ValueError("The questions are marked with (*)")
        except ValueError as e:
            print(f"{Back.RED}Invalid data entered: {e}")
            return show_bmw()


def choice_of_car():
    """
    This function asks users for their choice of car
    and instructs them to input 1,2 or 3 based on the list of
    cars shown. Once they have selected the car of their
    choice, it adds the car to the order list and shows them
    the car they have chosen.
    """
    while True:
        try:
            print_text("Type 1,2 or 3 to choose one of the car.\n")
            print_text("Or Enter 4 to quit/exit this process at any time. \n")
            print('\n')
            pick_car = int(input("Which car are you interested in?\n"))
            final_choice.clear()

            if pick_car == 1:
                final_choice.append(bmw_one)
                print(f"\n{final_choice}")
                return confirm_car_choice()

            elif pick_car == 2:
                final_choice.append(bmw_two)
                print(f"\n{final_choice}")
                return confirm_car_choice()

            elif pick_car == 3:
                final_choice.append(bmw_three)
                print(f"\n{final_choice}")
                return confirm_car_choice()

            elif pick_car == 4:
                return quit_func()

            else:
                raise ValueError("Type 1, 2 or 3 to choose one of the car.\n")
        except ValueError as e:
            print(f"{Back.RED}Invalid data entered: {e}")
            for car in bmw_list:
                print(f"\n{car} \n")
            continue


def confirm_car_choice():
    """
    This function asks users to enter
    Y to confirm the choice they
    have made or N to back to list of
    cars.
    """
    print_text("You can enter Q to quit/exit this process at any time. \n")
    print('\n')
    print_text("Please can you confirm this is the correct car.\n")
    confirm_choice = str(input("Enter 'Y' if Yes and 'N' if No. \n")).lower()
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
                print_text("Great Choice! \n")
                break

            elif data1 == 'n':
                print_text('Not a problem \n')
                for car in bmw_list:
                    print(f"{car} \n")
                    print("""
--------------------------------------------------------------------------
                       """)
                return choice_of_car()

            elif data1 == 'q':
                return quit_func()

            else:
                raise ValueError()

        except ValueError:
            print(f"{Back.RED}Invalid data entered!")
            print(final_choice)
            return confirm_car_choice()


def show_features():
    """
    This function asks users to enter
    Y for a description of the car they
    have selected or N to go to the next
    step.
    """
    print_text("You can enter Q to quit/exit this process at any time. \n")
    print('\n')
    print_text("Would you like a description of the car?\n")
    car_features = str(input("Enter 'Y' if Yes and 'Q' if No. \n")).lower()
    validate_show_features(car_features)


def validate_show_features(data2):
    """
    This function validates the data passed to it
    from the show features function. It checks
    if the user has entered y, n, or q and executes
    set tasks. Otherwise it raises a ValueError.
    """
    while True:
        try:
            if data2 == 'y':
                if final_choice[0] == bmw_one or bmw_two or bmw_three:
                    print_text(f"""
                    \nThis {final_choice[0]['Model']} {DESCRIPTION}
                    """)
                    break

            elif data2 == 'n':
                print_text("Not a problem \n")
                break

            elif data2 == 'q':
                return quit_func()

            else:
                raise ValueError()
        except ValueError:
            print(f'{Back.RED}Invalid data entered')
            return show_features()


def make_order():
    """
    This function asks users if they want
    to place an order on the car they have
    chosen.
    """
    print_text("\nEnter 'Y' if Yes and 'N' if No. \n")
    print_text("You can enter Q to quit/exit this process at any time. \n")
    print('\n')
    place_order = str(input("Would you like to complete the order?\n")).upper()
    validate_order(place_order)


def validate_order(data3):
    """
    This function validates the data passed to it
    from the make order function. It checks
    if the user has entered Y, N, or Q and executes
    set tasks. Otherwise it raises a ValueError.
    """
    while True:
        try:
            if data3 == 'Y':
                print_text("Of course! \n")
                print('\n')
                print_text("Your order is being prepared for collection...\n")
                break

            elif data3 == 'N':
                return quit_func()

            elif data3 == 'Q':
                return quit_func()

            else:
                raise ValueError()

        except ValueError:
            print(f"{Back.RED}Invalid data entered, please try again.")
            return make_order()


def reference_num():
    """
    This function generates a random 7 digit
    number when called. Then append the number
    to the final order list and print a detailed
    message to the users.
    """
    ref_num = random.randint(10000000, 99999999)
    final_order.append(ref_num)
    print_text(f"Your reference number is {final_order[3]}.\n")
    print('\n')
    print_text(f"""
    \nMake a note of your reference number to collect your car at the nearest
BMW store in {final_order[2]}.
    """)


def send_order():
    """
    This function sends all the information to
    google work sheet, which stores the data so
    the order can be prepared for the customer.
    """
    final_order.append(final_choice[0]['Make'])
    final_order.append(final_choice[0]['Model'])
    final_order.append(final_choice[0]['Colour'])
    final_order.append(final_choice[0]['FuelType'])

    bmw_worksheet = SHEET.worksheet('Collections')
    bmw_worksheet.append_row(final_order)
    print_text("Order Successful! \n")
    print('\n')
    print_text("This page will refresh in 30 seconds! \n")
    print('\n')
    print_text("Thank for ordering with BMW click and collect.\n")
    print('\n')
    print_text("Please wait....")
    time.sleep(30)
    clear_terminal()
    return all_functions()


def quit_func():
    """
    This function is used to quit/exit the ordering process
    when users use the quit option.
    """
    print("Thank you! \n")
    print_text("GoodBye for now :) \n")
    final_choice.clear()
    time.sleep(4)
    clear_terminal()
    return all_functions()


def all_functions():
    """
    This function runs all the other functions.
    """
    welcome_logo()
    initial_val()
    create_user_name()
    user_age()
    user_location()
    show_bmw()
    choice_of_car()
    show_features()
    make_order()
    reference_num()
    send_order()


all_functions()

