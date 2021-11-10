import json
import sqlite3 

#db_name = "UrbanAg.db"
db_name = "C:/Users/Julie/git/UrbanAg/UrbanAg.db"

# create a Connection object that represents the db
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row

# create a Cursor object, we will call its execute() 
# method to perform SQL commands
cursor = conn.cursor()

def table_to_json(table_name):
    # Template string that adds our table name
    # to a SQL statement string
    sql = f"SELECT * FROM {table_name}"

    # tell cursor to run the sql statement
    cursor.execute(sql)

    # now fetch the data and save it in memory
    rows = cursor.fetchall()

    # List to collect all the rows in
    rowarray_list = []

    # Go through all the rows we SELECTed above
    for row in rows:
        d=dict(zip(row.keys(), row))
        rowarray_list.append(d)

    # Call the json thingy to turn the list of stuff
    # from our table into a json string
    json_data= json.dumps(rowarray_list)

    # put the json string into a file
    rowarrays_file = f"{table_name}.json"
    file = open(rowarrays_file, 'w')
    file.write(json_data)
    print(f" wrote {len(rowarray_list)} rows from {table_name} to {rowarrays_file}")
    #print(f"Here's my JSON\n {json_data}")
    #print(json_data, f)

    print(f"Here's my JSON:\n {json_data}", file)
