import mysql.connector # Requires the mysql-connector-python driver
# Use command "pip install mysql-connector-python"
# Create a connection to the MySQL server
mydb = mysql.connector.connect(
host="139.62.210.180", # 139.62.210.180
user="cop3703_1", # cop3703_1
password="password", # password
database="cop3703_1" # cop3703_1
)
# Open the connection
mycursor = mydb.cursor()
def make_query(query):
    # Send a query to the MySQL server
    #mycursor.execute("select FirstName, LastName from Account where AccountType=2")
    mycursor.execute(query)
    # Read the results returned from the MySQL server
    myresult = mycursor.fetchall()
    mydb.commit()
    return myresult