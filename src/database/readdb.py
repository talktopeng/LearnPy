import pypyodbc as odbc # pip install pyoyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = '.'
DATABASE_NAME = 'Contoso 10K'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
print(conn)

print(odbc.drivers())