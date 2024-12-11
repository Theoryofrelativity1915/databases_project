from make_query import make_query

class Appointment:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

def get_appointment_query_type():
    print()
    print("Please enter a number to select from the following options:")
    print("1 - Add a product to cart")
    print("2 - View additional product details")
    print("3 - Update a transaction")
    print("4 - Remove a transaction")
    print("5 - Go back")
    field = input("Input: ")
    match field:
        case "1":
            add_product()
            get_appointment_query_type()
        case "2":
            read_details()
            get_appointment_query_type()
        case "3":
            update_transaction()
            get_appointment_query_type()
        case "4":
            delete_transaction()
            get_appointment_query_type()
        case "5":
            return
        case _:
            print("Looks like that's not an option!")
            get_appointment_query_type()

def add_product():
    transID = input("Enter the TransactionID you wish to add to. ")
    datetemp = f'SELECT Appointment_DateTime FROM Appointment WHERE TransactionID="{transID}";'
    staffIDtemp = f'SELECT Staff_AccountID FROM Appointment WHERE TransactionID="{transID}";'
    custIDtemp = f'SELECT Customer_AccountID FROM Appointment WHERE TransactionID="{transID}";'
    locationtemp = f'SELECT LocationID FROM Appointment WHERE TransactionID="{transID}";'
    date = make_query(datetemp)
    staffID = make_query(staffIDtemp)
    custID = make_query(custIDtemp)
    location = make_query(locationtemp)
    transID = transID[0][0] if transID else None
    date = date[0][0].strftime('%Y-%m-%d %H:%M:%S') if date else None
    staffID = staffID[0][0] if staffID else None
    custID = custID[0][0] if custID else None
    location = location[0][0] if location else None
    service = input("Enter the service ID you would like to add. ")
    quant = int(input("Enter how many you would like to add. "))
    pricetemp = f'SELECT Price FROM Service WHERE ID = {service}'
    price = make_query(pricetemp)[0][0]
    price = price * quant
    add = f'Insert into Appointment (TransactionID, Appointment_DateTime, Staff_AccountID, Customer_AccountID, LocationID, Service_Purchased_ID, Quantity, Appointment_Total) VALUES ({transID}, "{date}", {staffID}, {custID}, {location}, {service}, {quant}, {price})'
    make_query(add)
    

def delete_appointment(appointment):
    pass

def modify_item(transaction, action, name=None, quantity=None):
    if action == "add":
        for product, quantity in transaction.items:
            insert_item_query = f'INSERT INTO Appointment(Appointment_ID, Service_Purchased_ID) ' \
                                f'VALUES ({transaction}, "{name}");'
            make_query(insert_item_query)

def get_product_by_name(name):
    find_product_query = f'SELECT Name, Price, Description FROM Service WHERE Name="{name}";'
    product_result = make_query(find_product_query)
    if len(product_result) == 0:
        return None
    product_result = product_result[0]
    return Appointment(product_result[0], product_result[1], product_result[2])

def read_details():
    name = input("Enter product to see information: ")
    result = get_product_by_name(name)
    print(f'Name: {result.name}\nPrice: {result.price}\nDescription: {result.description}')
    return None

def update_transaction():
    transID = input("Enter the TransactionID you wish to modify. ")
    quanChange = input("Enter the service_ID you would like a different amount of. ")
    quant = input("How many of the service would you like? ")
    find_transaction = f'UPDATE Appointment SET Quantity = {quant} WHERE TransactionID={transID} AND Service_Purchased_ID = {quanChange};'
    make_query(find_transaction)
    return None
    


def delete_transaction():
    transID = input("Enter the transactionID you wish to remove. ")
    deletefield = f'DELETE FROM Appointment WHERE TransactionID="{transID}";'
    make_query(deletefield)
    return None