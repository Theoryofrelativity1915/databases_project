from make_query import make_query
class User:
    def __init__(self, firstname, lastname, email, phone_num):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone_num = phone_num
    
    def __str__(self): # This lets us use the print() method on a user and print their info instead of the memory location of the class instance.
        return f'{self.firstname}\n{self.lastname}\n{self.email}\n{self.phone_num}\n'


def handle_unverified_user():
        print("Please enter a number to select from the following options:")
        print("1 - Log in")
        print("2 - Create user")
        print("3 - Forgot password")
        print("4 - Exit? ")
        selected_option = input()
        match selected_option:
            case "1":
                return login()
            case "2":
                return create_and_login_user()
            case "3":
                forgot_password()
            case "4":
                exit(0)
            case _:
                print("Please enter a valid selection!")
        return None
                
    
def make_update_user_account_query(user, field, updated_value):
    update_account_query = f'UPDATE Accounts SET {field} = "{updated_value}" WHERE Email = "{user.email}";'
    make_query(update_account_query)
    update_user_field(user, field, updated_value)
    print(f'Updating {field} to be {updated_value}')
    
def update_user_field(user, field, value):
    match field:
        case "FirstName":
            user.firstname = value
        case "LastName":
            user.lastname = value
        case "Email":
            user.email = value
        case "PhoneNum":
            user.phone_num = value

def update_user_account(user):
    print("What would you like to update?")
    print("1 - Password")
    print("2 - Email")
    print("3 - First name")
    print("4 - Last name")
    print("5 - Phone number")
    print("6 - Go back")
    field = input()
    updated_value = input("What would you like to update the value to? ")
    match field:
        case "1":
            make_update_user_account_query(user, "Password", updated_value)
        case "2":
            make_update_user_account_query(user, "Email", updated_value)
        case "3":
            make_update_user_account_query(user, "FirstName", updated_value)
        case "4":
            make_update_user_account_query(user, "LastName", updated_value)
        case "5":
            make_update_user_account_query(user, "PhoneNum", updated_value)
        case "6":
            return
        case _:
            print("Looks like that's not an option!")
            
def delete_a_user(user):
    delete_user_query = f'DELETE FROM Accounts WHERE Email=\"{user.email}\";'
    make_query(delete_user_query)
    print("Account deleted.")

def get_password_wrapper(username):
    get_users_password_query = f'SELECT * FROM Accounts WHERE email="{username}";'
    result = make_query(get_users_password_query)
    if len(result) == 0:
        return None
    return result[0]

def login():
    username = input("Please enter your email: ")
    attempted_password = input("Please enter your password: ")
    result = get_password_wrapper(username)
    if result is None:
        print("User not found.")
        return False
    actual_password = result[5]
    if actual_password != attempted_password:
        print("Looks like that's not the right password.")
        return False
    return User(result[1], result[2], result[4], result[3])

def create_and_login_user():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    phone_num = input("Please enter your phone number without special characters. (Example: 123-456-7890): ")
    user = User(firstname, lastname, email, phone_num)
    create_account_query = f'INSERT into Accounts(FirstName, LastName, PhoneNum, Email, Password) VALUES ("{firstname}", "{lastname}", "{phone_num}", "{email}", "{password}");'
    make_query(create_account_query)
    return user

def forgot_password(email = None):
    if email is None:
        email = get_user_account_by_email(input("Please enter your email: "))
    else:
        email = get_user_account_by_email(email)
    while email is None:
        print("Uh-oh, looks like we couldn't find an account with that email.")
        print("Would you like to: ")
        print("1 - Go back")
        print("2 - Try again")
        user_selection = input()
        match user_selection:
            case "1":
                return
            case "2":
                email = get_user_account_by_email(input("Please enter your email: "))
            case _:
                print("Please select a valid option!")
    verification_code = None
    while verification_code != "1234":
        verification_code = input("Please enter verification code sent to email. (This doesn't actually email a code. Just enter 1234) ")
    confirm_password = input("What would you like your new password to be? ")
    updated_password = input("Please confirm your password: ")
    while confirm_password != updated_password and confirm_password is not None:
        updated_password = input("What would you like your new password to be? ")
        confirm_password = input("Please confirm your password: ")
        if(updated_password != confirm_password):
            print("Uh-oh! Looks like those don't match. Please try again.")
    print("Changing password to ", confirm_password)
    # make_update_user_account_query(email, "Password", confirm_password)
    update_account_query = f'UPDATE Accounts SET Password = "{confirm_password}" WHERE Email = "{email}";'
    make_query(update_account_query)
    

def get_user_account_by_email(email):
    find_user_account_query = f'SELECT Email FROM Accounts WHERE Email = "{email}";'
    user_email = make_query(find_user_account_query)
    if len(user_email) == 0:
        return None
    user_email = user_email[0][0]
    return user_email