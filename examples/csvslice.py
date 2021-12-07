import pandas as pd
import argparse

# Run this script like so:
# python csvslice.py -i legislators-current.csv -c "state,first_name,last_name,phone" -o out.csv

# Create command line arguments for input filename columns to select
# and output filename
# Tutorial on argparse
# https://docs.python.org/3/howto/argparse.html
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="csv file to input", required=True)
parser.add_argument("-c", "--columns", help="list of columns to select", required=True)
parser.add_argument("-o", "--output", help="output filename", required=True)
args = parser.parse_args()

print(f"Reading: {args.input}")
# Create a pandas DataFrame df from the csv file
#TODO check if the file exists first...
df = pd.read_csv(args.input)

# Uncomment the code below to print all column names from the file
#
# Get the column names as a list:
#colunm_names = df.columns.to_list()
#col_index = 1
# print(f"{args.input} has these columns:")
# for name in colunm_names:
#     print(f"{col_index}: {name}")
#     col_index += 1

## newline just to keep things separated
#print(" ")

columns = str.split(args.columns,",")
print(f"Selecting: {columns}")
newDf = df[columns]
print(f"Preview: {newDf}")
print(f"Writing: {args.output}")
newDf.to_csv(args.output, index=False)
# Note: you can remove index=False or set it to true
#       to give each row a unique number starting
#       from 1
