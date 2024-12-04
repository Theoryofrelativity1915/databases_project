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
        selected_option = int(input())
        match selected_option:
            case 1:
                return login()
            case 2:
                return create_and_login_user()
            case 3:
                forgot_password()
            case _:
                print("Please enter a valid selection!")
        return None
                
def change_password(email):
    change_password_query = f'UPDATE Accounts SET '
    
def make_update_user_account_query(user, field, updated_value):
    update_account_query = f'UPDATE Accounts SET {field} = "{updated_value}" WHERE Email = "{user.email}"'

def update_user_account(user):
    print("What would you like to update?")
    print("1 - Password")
    print("2 - Email")
    print("3 - First name")
    print("4 - Last name")
    print("5 - Phone number")
    print("6 - Password")
    print("7 - Go back")
    field = input()
    updated_value = input("What would you like to update the value to? ")
    match field:
        case 1:
            make_update_user_account_query(user, "Password", updated_value)
        case 2:
            make_update_user_account_query(user, "Password", updated_value)
        case 3:
            make_update_user_account_query(user, "Password", updated_value)
        case 4:
            make_update_user_account_query(user, "Password", updated_value)
        case 5:
            make_update_user_account_query(user, "Password", updated_value)
        case 6:
            make_update_user_account_query(user, "Password", updated_value)
        case 7:
            make_update_user_account_query(user, "Password", updated_value)
        case _:
            print("Looks like that's not an option!")
            

#TODO What happens when user doesn't exist?
def delete_a_user(user):
    delete_user_query = "DELETE FROM Accounts WHERE Email=\"{user.email}\";"
    make_query(delete_user_query)
    print("User deleted?")

def get_password_wrapper(username):
    get_users_password_query = f'SELECT * FROM Accounts WHERE email="{username}";'
    result = make_query(get_users_password_query)
    if len(result) == 0:
        return None
    print(result)
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
    print("User created!")
    exit(-1)
    return user

def forgot_password():
    email = input("Please enter your email: ")
    verification_code = None
    while verification_code != 1234:
        int(input("Please enter verification code sent to email. (This doesn't actually email a code. Just enter 1234)"))
    change_password(email)
