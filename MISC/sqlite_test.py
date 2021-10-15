import sqlite3

# create connection to sqlite db file
db_connection = sqlite3.connect('UrbanAg.db')

# create a cursor so we can execute SQL statements
cursor = db_connection.cursor()

# before using cursor we check if table already exists and, if so, drop 
#cursor.execute("DROP TABLE IF EXISTS companies")
#cursor.execute("CREATE TABLE companies (name text, num_employees)")


sql_statement_1 = "INSERT INTO companies VALUES ('Strange Herbs', 30) "

# do some INSERTs into our new table
cursor.execute(sql_statement_1)


db_connection.commit()
results = cursor.execute("SELECT * FROM companies")

print("Company Names from our Database:")
# results should be a list of Row objects...
# see https://docs.python.org/3/library/sqlite3.html#sqlite3.Row 
for row in results:
    # Each row also looks like an array...
    # in this case, we expect only one value per row - the "name" field
    # so we can access it at the [0] position
    print(row)