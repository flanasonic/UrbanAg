import sqlite3

# include the exists function from the os.path python module
from os.path import exists

# assume db is in current working folder where script is running
db_name = "./UrbanAg.db"

# create a Connection object that represents our db
# if the file exists, it will open it
# if the file doesn't exist, it will create it
# Note - the way it's written here, it will look for and create
# the .db file in whatever folder the program is running in
conn = sqlite3.connect(db_name)

# create a Cursor object - we'll call its execute() method 
# to perform SQL commands
cursor = conn.cursor()

# create a function that given a table name like "company" will 
# go and open the sql/company/create_company.sql file and run it

def run_sql_script(script_prefix, table_name):
    # use an f-string to create a filename path from the table name
    filename_to_open = f"./sql/{table_name}/{script_prefix}_{table_name}.sql"
    # check if our file does not exist and
    # if it does not, warn and exit our function
    if (not exists(filename_to_open)):
        print(f"HEY! {filename_to_open} does not exist! ")
        return

    # create a file object that points to our file
    file_handle = open(filename_to_open, "r")

    # use .read() to read the contents and save the result to 
    # a variable as a single string
    file_contents = file_handle.read()
    cursor.execute(file_contents)

# let's make a list of all the tables we would like to create
# in the order we would like to create them
tables = [
    "company", 
    "facility"
]

# loop through the list of table names and call the function 
# that gets their create_table script and runs it...
for table_name in tables:
    print(f"   dropping table {table_name} if it exists...")
    run_sql_script("drop", table_name)

    print(f"   creating table {table_name}...")
    run_sql_script("create", table_name)

# now lets see what tables are in our database
print(" ")
print("Dababase: " + db_name + " now has these tables:")
results = cursor.execute("SELECT name FROM  sqlite_master  WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
for row in results:
    print(f"  {row[0]}")
