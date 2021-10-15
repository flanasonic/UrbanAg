from flask import Flask
import sqlite3

######################################
# Prepare our Sqlite database for use

# create a connection to our database
conn = sqlite3.connect(db_name)

# open a cursor
cursor = conn.cursor()

#####################################
# Let's make a web service that reads 
# from our database

# Create a "Flask" object 
web_server = Flask(__name__)

# This next line is an annotation - it "decorates" a function
# here - meaning - let's "decorate" our function with extra
# properties that we can't normally do when we write a function
# Here, we're saying this function should be called when a browser
# calls our webserver and gives the path "/companies" 
# ... when our web server gets a request for /companies... call this
# function
@web_server.route("/companies")
def getCompanies():
    # Prepare a string variable with some HTML boilerplate
    # for a simple web page.
    html = "<html><head><title>"
    # the += here is shorthand for "add this string on to the end"
    # alt:  html = html + "whatever"
    html += "Indoor Farming Companies"
    html += "</title></head><body>"
    html += "<h1>Controlled Environment Agriculture Companies</h1>"

    # now let's call our database - issue a "select" from 
    # our companies table and get company names
    # we'll get the list of companies in the result variable
    # I think results will be a list of Row objects
    results = cursor.execute("SELECT name, employees FROM companies")

    # results should look something like this:
    #
    #           row  | contents
    #           0  | [ 'some name', 103   ] <-- array/list
    #           1  | [ 'another name', 20 ]
    # for each row  item [0] -^        ^- item[1]

    # add some html to our response for an unordered list
    html += "<ul>"

    # because we have a list of rows now - we can iterate 
    # through them in a for loop and extract their goodness
    for row in results:
        # add the field from each row to our html as a list item
        # Row objects also behave like lists - here the 0th item
        # in the row is the name we SELECTed above
        html += "<li>" + row[0] + " Number of Employees: " + str(row[1]) + "</li>"

    # outside the loop now - tack on the end of our htmnl
    html += "</ul></body></html>"

    # return our HTML string and some other junk the web needs
    return html, 200, { 'Content-Type': 'text/html', "X-Julie": "awesome" }

# I don't know what this does - copy paste from the flask example
if __name__ == '__main__':
    # Run our web server
    web_server.run(debug=True)
