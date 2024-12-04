from product import add_new_product
from transaction import handle_transaction
from user import *


######################      Main CLI loop to handle user input        ######################

#Main CLI loop to show and select options
def handle_verified_user(user):
    print("Please enter a number to select from the following options:")
    print("1 - Start a new transaction.")
    print("2 - Change password")
    print("3 - Add a new service for the business to offer to customers")
    print("4 - Update my account info")
    print("5 - Delete a user")
    selected_option = selected_option = int(input())
    match selected_option:
        case 1:
            handle_transaction()
        case 2:
            change_password(user)
        case 3:
            add_new_product()
        case 4:
            update_user_account(user)
        case 5:
            delete_a_user(user)
            
            
run = True
user = None
while run:
    if not user: #User is not logged in
        user = handle_unverified_user() #Attempt to log the user in
    else:
        handle_verified_user(user)

######################      ^Main CLI loop to handle user input^        ######################


