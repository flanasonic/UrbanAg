import json
import sqlite3 

# assume db is in current working folder where script is running
db_name = "./UrbanAg.db"

# create a Connection object that represents the db
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row

# create a Cursor object - we'll call its execute() method 
# to perform SQL commandss
cursor = conn.cursor()

def table_to_json(table_name):
    # use an f-string to add our table name into a 
    # SQL statement string
    sql = f"SELECT * FROM {table_name}"

    # tell cursor to run the SQL statement
    cursor.execute(sql)

    # now fetch the data and save it in memory
    rows = cursor.fetchall()

    # make an empty list to collect all the rows
    rowarray_list = []

    # go through all the rows selected above
    for row in rows:
        d=dict(zip(row.keys(), row))
        rowarray_list.append(d)

    # convert our rowarray_list to a json string
    # using the json.dumps() function 
    json_data= json.dumps(rowarray_list)

    # save the json string into a file
    #??? Patrick - am I correct that we are making an empty file here 
    # called "rowarrays_file" and this variable name stays the same no
    # matter what the table name is?? And then where does this json file get saved?
    rowarrays_file = f"{table_name}.json"
    file = open(rowarrays_file, 'w')
    file.write(json_data)
    print(f" wrote {len(rowarray_list)} rows from {table_name} to {rowarrays_file}")
    #print(f"Here's my JSON\n {json_data}")
    #print(json_data, f)

    print(f"Here's my JSON:\n {json_data}", file)
