import sqlite3

# include the exists function from the os.path python module
from os.path import exists

from csv import reader as csvreader

# we are making the assumption here here that our db is in 
# the current working folder where our script is running
db_name = "./UrbanAg.db"

# create a function that given a table name, will look for a file 
# called /data/table_name.csv, then open it up and insert each row 
# of the CSV file into the SQL table referred to by table_name
def populate_table(table_name):

    # create a Connection object that represents our db
    conn = sqlite3.connect(db_name)

    # create a Cursor object
    cursor = conn.cursor()

    # use an f-string to create a filename path from the table name
    filename = f"./data/{table_name}.csv"

    # using the exists method from the os.path module
    # check if our file does not exist and
    # if it does not, warn us and exit our function
    if(not exists(filename)):
        print(f"HEY! {filename} does not exist!")
        return
    
    # create a file object that points to our CSV file
    with open(filename, 'r') as file_handle:

        # create an empty list of rows, later we'll push in here the rows of 
        # data we want to insert into our db
        rows = []

        # create an id integer, we'll increment by 1 for each row and add 
        # it to the id column of our db
        # we start with 0 because the first line of our file should just be a 
        # header row containing the names of the columns
        # the first line with real data to insert will have id = 1
        id = 0

        file_lines = csvreader(file_handle)
        for line in file_lines:
        # the "line" variable here corresponds to one line in our CSV file
        # each line is a list of the fields that were separated by commas in 
        # our CSV file
        # Let's add the value of our id to each line at index 0
        # this lets us avoid having to maintain a list of ids in our CSV file
        # good because we can add rows to our CSV without re-numbering ids
        # Note - DON'T include id field in the CSV file since the script is 
        # taking care of it
            line.insert(0, id)

        # add this line to our list of rows, but first convert it to a tuple 
        # because sqlite will want us to do this
            line = tuple(line)
            rows.append(line)

        # increment our id to the next number
            id = id + 1

    # the first line of our file has our column names
    # let's grab it out of our list of rows and save to a new var??
    column_list = rows.pop(0)

    # remember- above we converted each row to a tuple, but we need 
    # to be able to change this line, so we convert it back to a list
    column_list = list(column_list)

    # this is supposed to be our list of column headers, so instead of having 
    # id value, we'll change to the column name "id"
    column_list[0] = 'id'

    # using the comma as delimiter, we split each line into a list
    # this is useful for all of the rows that are values.  
    # But for our list of column names in column_list we actually want 
    # these as a comma separated string for our SQL statement
    columns = ",".join(column_list)

    # let's create the first part of our sql insert statement
    # we'll turn this into a template we can use to insert
    # all of our rows later...
    insert_sql = f"insert into {table_name}({columns}) values "

    # for this sql statement to work as a "template" for inserting all of our
    # rows, we need to add a "placeholder" for each field we want to insert
    # in each of our rows
    # placeholders are just ? characters
    # we want one placeholder for every column name we have in our header
    # we also want parentheses around all all of our placeholders
    # if we have three columns in our table, our placeholders would look like
    # (?,?,?)
    placeholders = []

    # note below we're looping over column_list (the list)
    # not columns (the comma delimited string)
    for column_name in column_list:
        placeholders.append("?")
    
    # placeholders is now a list of (?) strings - one for each column
    # let's turn it into a comma separated string and add it to the end of
    # our insert statement template
    placeholders = ",".join(placeholders)
    insert_sql += f"({placeholders})"

    # so now we have a complete template.  
    # As an example of what it should look like...
    # For a table called people with three columns
    # id, name, color
    # we should have a sql template that looks like this
    #
    #  insert into table people(id, name, color) values (?,?,?)
    #
    # now let's say we're inserting a row to this table with values
    # 101, "Jeff", "Purple"
    # 
    # if we give these values to the sqlite execute function as a list
    # it will put 101 in the first placeholder spot, "Jeff" in the second
    # placeholder spot, and "Purple" in the third 
    #
    # so effectively, the sqlite execute function takes the template and the
    # list of values and makes this:
    # 
    # insert into tale people(id, name, color) values (101, "Jeff", "Purple")
    #
    # this template / placeholder technique is sometimes known 
    # as a "Prepared Statement"

    # loop through our list of rows and add each one using our sql template
    for row in rows:
        # Uncomment this next line if you get stuck and need to debug a 
        # problem with the insert statement
        print(f"{insert_sql} {row}")
        cursor.execute(insert_sql, row)

    # use the db connection object we created earlier to "commit" 
    # the new rows we just inserted
    # conn.commit() makes them "permanent"

# create a list of the tables we want to populate
tables_to_populate = [ "company", "facility"]

# TODO: Ask Patrick - but first we have to create the connection and the cursor again??
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# loop over the list of tables_to_populate and call our function
for table in tables_to_populate:
    populate_table(table)

conn.commit()
conn.close()