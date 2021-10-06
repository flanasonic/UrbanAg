import sqlite3
from os.path import exists

db_name = "UrbanAg.db"

# shorthand for db connection
conn = sqlite3.connect(db_name)

cursor = conn.cursor()

# Create a function that - when called with a table name like 
# run_sql_script("create", "company")
#
# will go and open the sql/company/create_company.sql file
# and run it
#
def run_sql_script(script_prefix, table_name):
    # make us a filename path from the table name
    # we'll use a template string: 
    # https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36
    filename_to_open = f"./sql/{table_name}/{script_prefix}_{table_name}.sql"

    # check if our file does not exist - warn and exit our function
    # if the file does not exist
    if (not exists(filename_to_open)):
        print(f"HEY! {filename_to_open} does not exist! ")
        return

    # get a "handle" on the file ...
    file_handle = open(filename_to_open, "r")

    # extract all the sql goodness inside 
    file_contents = file_handle.readlines()

    # readlines() gave us a list of strings - one for
    # eadch line in the file.  That's dumb, we want one
    # string with the whole file in it.  So we need to join
    # them together.  The bulit in string object has a join
    # function that works like this...  
    # 
    #    given a string like...
    # my_string = " Julie "  
    #    (it's Julie with a space before and after)
    #
    #    and a list like 
    # my_list = ['red', 'green', 'blue']
    #
    #    if we do 
    # my_new_string = my_string.join(my_list)
    #
    #    then my new string will be "red Julie green Julie blue"
    # 
    # Here we just want to join the lines of our file together
    # with nothing inbetween.  So we'll do
    file_contents = ''.join(file_contents)
    # do it...
    cursor.execute(file_contents)


# let's make a list of all the tables
# we would like to create - in the order
# we would like to crete them.
tables = [
    "company", 
    "facility"
]

# loop through the list of table names
# and call the function that gets their
# create_table script and runs it...
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
