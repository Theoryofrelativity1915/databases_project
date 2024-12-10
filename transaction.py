import datetime
from appointment import create_appointment
from make_query import make_query


def create_transaction(customer_id, employee_id):
    transaction_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    insert_transaction_query = f"""
        INSERT INTO Transactions (DateTime) 
        VALUES ('{transaction_datetime}');
    """
    make_query(insert_transaction_query)

    get_transaction_id_query = "SELECT LAST_INSERT_ID();"
    transaction_id_result = make_query(get_transaction_id_query)
    transaction_id = transaction_id_result[0][0]

    print(f"Transaction {transaction_id} created successfully.")


    return transaction_id


def add_appointment_to_transaction():
    print("Adding appointment to transaction...")
    create_appointment()


def remove_appointment_from_transaction(transaction_id, service_id):
    transaction_check_query = f"SELECT * FROM Transactions WHERE ID = {transaction_id};"
    transaction_result = make_query(transaction_check_query)

    if not transaction_result:
        print(f"Transaction with ID {transaction_id} not found.")
        return

    appointment_check_query = f"SELECT * FROM Appointment WHERE TransactionID = {transaction_id} AND Service_Purchased_ID = {service_id};"
    appointment_result = make_query(appointment_check_query)

    if not appointment_result:
        print(f"Appointment with Service ID {service_id} not found in Transaction {transaction_id}.")
        return

    delete_appointment_query = f"DELETE FROM Appointment WHERE TransactionID = {transaction_id} AND Service_Purchased_ID = {service_id};"
    make_query(delete_appointment_query)
    print(f"Appointment with Service ID {service_id} removed from Transaction {transaction_id}.")


def view_previous_transactions(customer_id):
    select_transactions_query = f"""
        SELECT T.ID, T.DateTime, A.Service_Purchased_ID, S.Name 
        FROM Transactions T
        JOIN Appointment A ON T.ID = A.TransactionID
        JOIN Service S ON A.Service_Purchased_ID = S.ID
        WHERE A.Customer_AccountID = {customer_id};
    """
    transactions = make_query(select_transactions_query)

    if transactions:
        print(f"Previous transactions for Customer ID {customer_id}:")
        for transaction in transactions:
            transaction_id = transaction[0]
            transaction_datetime = transaction[1]
            service_id = transaction[2]
            service_name = transaction[3]
            print(
                f"Transaction ID: {transaction_id}, Date and Time: {transaction_datetime}, Service: {service_name} (ID: {service_id})")
    else:
        print(f"No previous transactions found for Customer ID {customer_id}.")


def handle_transaction():
    while True:
        print("\nSelect an option:")
        print("1 - Create a new transaction")
        print("2 - Add appointment to transaction")
        print("3 - Remove appointment from completed transaction")
        print("4 - View previous transactions")
        print("5 - Exit")

        user_choice = input("Input: ")

        if user_choice == "1":
            customer_id = int(input("Enter customer ID: "))
            employee_id = int(input("Enter employee ID: "))
            transaction_id = create_transaction(customer_id, employee_id)

        elif user_choice == "2":
            transaction_id = int(input("Enter transaction ID: "))
            add_appointment_to_transaction()

        elif user_choice == "3":
            transaction_id = int(input("Enter transaction ID: "))
            service_id = int(input("Enter service ID to remove: "))
            remove_appointment_from_transaction(transaction_id, service_id)

        elif user_choice == "4":
            customer_id = int(input("Enter customer ID: "))
            view_previous_transactions(customer_id)

        elif user_choice == "5":
            break
        else:
            print("Invalid option. Please try again.")