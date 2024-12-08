from sqlite3 import DatabaseError
from make_query import make_query
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

def get_product_query_type():
    print()
    print("Please enter a number to select from the following options:")
    print("1 - View list of available services")
    print("2 - View service details")
    print("3 - Suggest a new service for the business to offer")
    print("4 - Modify service (Admin only)")
    print("5 - Delete service (Admin only)")
    print("6 - Go back")
    field = input("Input: ")
    match field:
        case "1":
            read_product_list()
            get_product_query_type()
        case "2":
            read_product_details()
            get_product_query_type()
        case "3":
            add_new_product()
            get_product_query_type()
        case "4":
            update_product()
            get_product_query_type()
        case "5":
            delete_product()
            get_product_query_type()
        case "6":
            return
        case _:
            print("Looks like that's not an option!")
            get_product_query_type()


    
def add_new_product():
    name = input("Enter service name: ")
    price = input("Enter service price: ")
    description = input("Enter service description: ")
    product = Product(name, price, description)
    create_product_query = f'INSERT INTO Service(Name, Price, Description) VALUES ("{name}", "{price}", "{description}");'
    make_query(create_product_query)
    return product

def delete_product():
    valid = False
    while not valid:
        field = input("Which service would you like to delete? ")
        product = get_product_by_name(field)
        if field == "exit":
            return
        elif product is None:
            print("Sorry that is not an available service.")
        else:
            valid = True
    delete_product_query = f'DELETE FROM Service WHERE Name = \'{product.name}\';'
    result = make_query(delete_product_query)
    if len(result) == 0:
        return None
    return result[0]

def update_product():
    valid = False
    while not valid:
        field = input("Which service would you like to modify? ")
        product = get_product_by_name(field)
        if field == "exit":
            return
        elif product is None:
            print("Sorry that is not an available service.")
        else:
            valid = True

    valid = False
    while not valid:
        print("What would you like to update?")
        print("1 - Product Name")
        print("2 - Product Price")
        print("3 - Product Description")
        print("4 - Go back")
        field = input()
        try:
            field_num = int(field)
            if field_num > 4 and field_num > 0:
                print("Sorry, not an option! Please try again.")
            elif field_num == 4:
                return
            else:
                valid = True
                updated_value = input("What would you like to update the value to? ")
        except ValueError: 
            print("Please enter a number.")

    match field:
        case "1":
            make_update_product_query(product, "Name", updated_value)
        case "2":
            try:
                updated_value = int(updated_value)
                make_update_product_query(product, "Price", updated_value)
            except  ValueError:
                print(f'Price of \'{product.name}\' not modified. Please restart and ensure the new value of price is an integer.')
                update_product()
        case "3":
            make_update_product_query(product, "Description", updated_value)


def make_update_product_query(product, field, updated_value):
    update_product_query = f'UPDATE Service SET {field} = "{updated_value}" WHERE Name = "{product.name}";'
    make_query(update_product_query)
    update_product_field(product, field, updated_value)
    print(f'Updating {field} to be {updated_value}')

def update_product_field(product, field, value):
    match field:
        case "Name":
            product.name = value
        case "Price":
            product.price = value
        case "Description":
            product.description = value

def read_product_details():
    valid = False
    while not valid:
        field = input("Which service would you like more information on? ")
        result = get_product_by_name(field)
        if field == "exit":
            return
        elif result is None:
            print("Sorry that is not an available service.")
        else:
            valid = True
    print("Product Name: ", result.name)
    print("Product Price: ", result.price)
    print("Product Description: ", result.description)
            

def get_product_by_name(name):
    find_product_query = f'SELECT Name, Price, Description FROM Service WHERE Name="{name}";'
    product_result = make_query(find_product_query)
    if len(product_result) == 0:
        return None
    product_result = product_result[0]
    return Product(product_result[0], product_result[1], product_result[2])

def read_product_list():
    find_all_product_query = f'SELECT Name, Price, Description FROM Service'
    product_list = make_query(find_all_product_query)
    if len(product_list) == 0:
        print("No services available.")
        return
    print("Currently we have ", len(product_list), " services available")
    for row in product_list:
        print("Service Name: ", row[0])