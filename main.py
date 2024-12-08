from product import get_product_query_type
from transaction import handle_transaction
from user import *


######################      Main CLI loop to handle user input        ######################

#Main CLI loop to show and select options
def handle_verified_user(run):
    global user
    while run and user is not None:
        print("\nPlease enter a number to select from the following options:")
        print("1 - Start a new transaction.")
        print("2 - Change password")
        print("3 - About our services")
        print("4 - Update my account info")
        print("5 - Delete my account")
        print("6 - Exit? ")
        selected_option = selected_option = input()
        match selected_option:
            case "1":
                handle_transaction()
            case "2":
                forgot_password(user.email)
            case "3":
                get_product_query_type()
            case "4":
                update_user_account(user)
            case "5":
                delete_a_user(user)
                user = None
                return
            case "6":
                exit(0)
            case _:
                print("Please select a valid option!")
            
            
run = True
user = None
while run:
    if not user: #User is not logged in
        user = handle_unverified_user() #Attempt to log the user in
    else:
        handle_verified_user(run)

######################      ^Main CLI loop to handle user input^        ######################


