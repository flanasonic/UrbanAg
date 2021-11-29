from flask import Flask
import sqlite3

######################################
# Prepare our Sqlite db for use
# make a web service that reads from our db
# create an instance of the Flask class and save the object to a 
# variable called "web_server"
# Note - the value of __name__ depends on how the script is being 
# executed. We're running it directly here, so __name__ is equal to '__main__'. 
# If we were importing the script as a module into another Python script, 
# then __name__ would be equal to its filename.
web_server = Flask(__name__)


# TODO: make it so that it returns JSON instead of HTML
# create a function called "getCompanies" that will return some HTML
# Use the route() decorator to bind the URL path '/companies' to 
# the getCompanies function, so when our web server gets a request for 
# '/companies' this function will be called

@web_server.route("/companies")
def getCompanies():
    # create a Connection object that represents our db
    conn = sqlite3.connect(db_name)

    # create a Cursor object
    cursor = conn.cursor()

    # Prepare a string variable with some HTML boilerplate
    # for a simple web page.
    html = "<html><head><title>"
    html += "Indoor Farming Companies"
    html += "</title></head><body>"
    html += "<h1>Controlled Environment Agriculture Companies</h1>"

    # now let's call our database - issue a "select" from 
    # our companies table and get company names
    # we'll get the list of companies in the result variable
    # ??? I think results will be a list of Row objects???
    results = cursor.execute("SELECT name, employees FROM companies")

    # add some html to our response for an unordered list
    html += "<ul>"

    # use a for loop to iterate through our list of rows and extract 
    # their info
    for row in results:
        # add the field from each row to our html as a list item
        # Row objects also behave like lists - here the 0th item
        # in the row is the name we SELECTed above
        html += "<li>" + row[0] + " Number of Employees: " + str(row[1]) + "</li>"

    # outside the loop now - tack on the end of our htmnl
    html += "</ul></body></html>"

    # return our HTML string and some other junk the web needs
    return html, 200, { 'Content-Type': 'text/html', "X-Julie": "awesome" }

if __name__ == '__main__':
    # Run our web server
    web_server.run(debug=True)
