import pyodbc


def getsqlversion(servername="."):
    # Set up your SQL Server connection details
    driver = 'SQL Server'
    # server = '.'  # Replace with your server name
    server = servername
    database = 'contoso 10k'  # Replace with your database name
    # username = 'your_username'  # Replace with your username
    # password = 'your_password'  # Replace with your password

    # Create the connection string
    # connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trust_Connection=yes'
    connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trust_Connection=yes'



    # Establish the connection
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()

        # Execute a query to get the SQL Server version
        cursor.execute("SELECT @@VERSION")
        
        # Fetch and print the result
        version = cursor.fetchone()[0]
        print("SQL Server Version:", version)