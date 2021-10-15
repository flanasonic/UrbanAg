import sqlite3
import json

# Write a function to convert CSV to JSON
# Takes the file paths as arguments

def make_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary and add to data
        for rows in csvReader:

            # Primary key is actually always going to be called "id" 
            # For now, we'll just use "company_id" to test and fix it later
            key = rows['id']
            data[key] = rows

    # open a json writer and use json.dumps() function 
    # to dump the data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    
# set the variables to the correct file paths
csvFilePath = r'./data/facility.csv'
jsonFilePath = r'./data/facility.json'

# now call the make_json function
make_json(csvFilePath, jsonFilePath)