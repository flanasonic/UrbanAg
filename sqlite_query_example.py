import sqlite3

# assuming here that db is in current working folder where script is running
db_name = "./UrbanAg.db"

# create a Connection object that represents our db
# if the file exists, it will open it
# if it doesn't exist, it will create it
# Note - the way it's written here, it will look for and create
# the .db file in whatever folder the program is running in
conn = sqlite3.connect(db_name)

# create a Cursor object - we'll call its execute() method 
# to perform SQL commands
cursor = conn.cursor()


# execute some SQL statements
cursor.execute("""INSERT INTO company (name) VALUES ('TomatoHaus')""")


# we can also save a SQL statement to a variable then execute
sql_statement_1 = """INSERT INTO company (name, employees) 
 VALUES('You Grow Girl Inc.', 20) """
cursor.execute(sql_statement_1)

# ?? Julie to test this out....????
# So far, the changes we've made to our DB (create table, inserts...)
# were done in a temporary place - allowing us to execute multiple sql
# statements and only make them permanent (i.e. commit() them) after
# all of them complete succesfully.  If any errors occur (e.g. bad SQL
# statement) - the cursor.execute() should throw an exception.
# 
# see https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute  
conn.commit()

# now let's execute a select and get the data we just inserted
results = cursor.execute("SELECT name FROM company")

print("Company Names from our Database:")
# results should be a list of Row objects...
# see https://docs.python.org/3/library/sqlite3.html#sqlite3.Row 
for row in results:
    # Each row also looks like an array...
    # in this case, we expect only one value per row - the "name" field
    # so we can access it at the [0] position
    print(row[0])