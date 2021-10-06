import json
import sqlite3 

db_name = "UrbanAg.db"

# shorthand for db connection

conn = sqlite3.connect(db_name)

with conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    sql= "SELECT * FROM company"

    # tell cursor to run the sql statement
    cursor.execute(sql)
    
    # now fetch the data and save it in memory
    rows = cursor.fetchall()
    
    rowarray_list = []
    for row in rows:
        d=dict(zip(row.keys(), row))
        rowarray_list.append(d)


    json_data= json.dumps(rowarray_list)
    rowarrays_file = "rowarrays.js"
    file = open(rowarrays_file, 'w')

    #print(f"Here's my JSON\n {json_data}")
    #print(json_data, f)

    print(f"Here's my JSON:\n {json_data}", file)
