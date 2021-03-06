import sqlite3

# include the exists function from the os.path python module
from os.path import exists

# assume our db is in the current working folder where script 
# is running
db_name = "./UrbanAg.db"

# create a function that takes a table name like "company" then goes
# and opens the sql/company/create_company.sql file and runs it
def run_sql_script(script_prefix, table_name):

    # create a Connection object that represents our db
    conn = sqlite3.connect(db_name)

    # create a Cursor object
    cursor = conn.cursor()

    # use an f-string to create a filename path from the table name
    filename_to_open = f"./sql/{table_name}/{script_prefix}_{table_name}.sql"
    # check if our file does not exist
    # if it does not exist, warn us and exit our function
    if (not exists(filename_to_open)):
        print(f"HEY! {filename_to_open} does not exist! ")
        return

    # create a file object that points to our file
    # TODO: do we need to use "with open" here??
    file_handle = open(filename_to_open, "r")

    # use .read() to read the contents and save the result to 
    # a variable as a single string
    file_contents = file_handle.read()
    cursor.execute(file_contents)


# loop through the list of table names and call the function
# that gets their drop table script and drops the table if it exists
# then gets their create_table script and runs it...

tables = ["company", 
        "facility"]

def drop_create(tables):
    # make a list of all the tables we would like to create
    # in the order we would like to create them

    for table_name in tables:
        print(f"   dropping table {table_name} if it exists...")
        run_sql_script("drop", table_name)
        print(f"   creating table {table_name}...")
        run_sql_script("create", table_name)

        # print a list of the tables that are now in our database
        print(" ")
        print("Dababase: " + db_name + " now has these tables:")



# sqlite_master contains info about what's in our db
# we want our query to include just the tables with our data,
# so we exclude any tables where name contains the word "sqlite"
# TODO: Ask Patrick - but first we have to create the connection and the cursor again??

def 
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
results = cursor.execute("SELECT name FROM  sqlite_master  WHERE type ='table' AND name NOT LIKE 'sqlite_%';")

for row in results:
        print(f"  {row[0]}")
