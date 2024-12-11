from product import get_product_query_type
from transaction import handle_transaction
from user import *
from appointment import get_appointment_query_type


######################      Main CLI loop to handle user input        ######################

#Main CLI loop to show and select options
def handle_verified_user(run):
    global user
    while run and user is not None:
        print("\nPlease enter a number to select from the following options:")
        print("1 - Start a new transaction.")
        print("2 - Modify an existing transaction.")
        print("3 - Change password")
        print("4 - About our services")
        print("5 - Update my account info")
        print("6 - Delete my account")
        print("7 - Exit? ")
        selected_option = selected_option = input()
        match selected_option:
            case "1":
                handle_transaction()
            case "2":
                get_appointment_query_type()
            case "3":
                forgot_password(user.email)
            case "4":
                get_product_query_type()
            case "5":
                update_user_account(user)
            case "6":
                delete_a_user(user)
                user = None
                return
            case "7":
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


