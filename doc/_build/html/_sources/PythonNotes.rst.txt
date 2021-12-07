Everything I ever learned about Pyton is written HERE.

Python!
============

Common uses for Python:
* Web development
* data analysis
* file processing
* machine learning
* game programming

[ ] List, Array
{ } Object
( ) Function

**object oriented programming (OOP) -**
the pattern of defining classes and creating objects to represent the responsibilities of a program.

**class -**
a template for a data type that describes the kinds of information it will hold and how a programmer will interact with it. The keyword *class* is used to define a class and names are capilized by convention.

The *pass* keyword can be used to indicate that the body of the class was intentionally left blank, so we don't cause an IndentationError.

**object -**
an instance of a class. Each object can hold different kinds of data.
 
**variables -**
names can contain letters and digits, but must begin with a letter or underscore. By convention, variable names are written in all lowercase. The assignment statement gives variable its value. The equals sign "=" is the assignment token.

**data type -**
the kind information you store in your variable, such as strings, integers, floats, lists. A variable’s type determines what you can do with it and how you can use it. Operations are defined at the type level.

We can check a variables data type using this syntax::

    (type(my_variable))

**keywords -**
Python has 33 keywords, they can’t be used as variable names.

**arithmetic operators -** 
integers and floats can both use +, -, *, and /. Strings can use + and *. When * is used to repeat a string it is referred to as the “repetition operator.”

**lists -**
a versatile data type that, in Python, can contain multiple different data types within the same square brackets/ Data types that can be used in lists include numbers, strings, other objects, even other lists. A list can also be empty, like this: []

**functions -**
reusable blocks of code. Like a recipe, a function keeps the steps for a task in one place. Functions can take *arguments* that tell Python the values we want to work with.::

    def some_function(some_input1, some_input2):
      # … do something with the inputs …
      return output

**iterable -**
any object that can return its members one at a time. *Sequences* and *generators* are two iterable types commonly used in Python.

**enumerate() -**
the enumerate() function provides both a counter and the value from an iterable at the same time, saving the step of having to create and incremente our own counter variable. It can use in a loop in almost the same way the original iterable object is used. Instead of putting the iterable directly after in in the for loop, we place it inside the parentheses of enumerate(). ::

    for idx, item in enumerate(iterable):
      print(idx, item)

**instantiation -**
to create an instance of a class, AKA an *object*. To do so we add () to the name of the class, then assign this new instance to a variable so we can access it later. ::

    class Car:
      pass  
      # pass lets us leave the body of the class blank without causing an IndentationError

    ferrari = Car()  # this is a class instantiation


**type () -**
the type() function returns the class that the object is an instance of. ::

    facade_type = type(Facade())
      print(facade_type)
      # prints this: <class '__main__.Facade'>
      #  __main__ means “this current file we’re running”
      # the output from type() could be read as “the class Facade that was defined 
      # here, in the script you’re currently running.”

**method -** 
built-in functionality for a specific data type, it is defined as part of a class. If the method requires an input value it goes inside (). Methods are defined similarly to functions, but indented to indicate they are part of the class. The first argument is *self*, meaning the instance of the object itself. When we call a method, the object making the calling is automatically passed as the first argument. ::

    example: 
    snack_list.append('cookie')

    example:
    shopping_list.remove("Olive oil")  

CLASS VARIABLES:
Used when we want to make the same data available to every instance of a class. Class variables are defined in the indented part of the class definition. They are accessed using the object.variable syntax.

  Example:
  class Circle:
    pi = 3.14   # pi is a class variable
    def area(self, radius): 
      return Circle.pi * radius **2 

INSTANCE VARIABLES:
Specific to the object they are attached to. We assign them using the same attribute notation used to access class variables, the object.variable syntax (Note - Instance variables and class variables are both considered "attributes" of an object.

  Example:
  class Store:
    pass

  alt_rocks = Store()   # this is our object
  alt_rocks.store_name = "Alt Rocks" 

Attribute errors:
If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

hasattr():
lets us check whether an object has a given attribute. It returns a boolean - True if it does and False if it not.

  Syntax:
  hasattr(object, “attribute”) 

It has two parameters - object and attribute. "Object" is the object we are testing to see if it has the attribute in question. "Attribute" is the name of the attribute we are inquiring about.
  
getattr():
returns the value of a given object and attribute. We can also supply an optional third argument that will be the default if the object doesn't have the attribute.

  Syntax:
  getattr(object, “attribute”, default)
  

Constructors:
Methods that are used to prepare an object being instantiated. 

init method:
Used to initialize a newly created object. It is called every time the class is instantiated.

  Example:
  class Animal:
    def __init__(self, voice):
      self.voice = voice

  cat = Animal('Meow')
  print(cat.voice) # Output: Meow

  #When an Animal object is created, the instance variable 'voice' is created and 
  #set to the input value

dir() function:
it’s possible for an object to have some attributes that are not explicitly defined 
in its constructor. dir() lets us investigate an object’s attributes at runtime. 

internal attributes:
Python automatically adds a number of attributes to all objects that get created. 
These internal attributes are usually indicated by double-underscores. 

__repr__() method:
let's us tell Python what we want the string represention of the class to be.
__repr__() can only have one parameter, self, and must return a string.

COMMENTS:
  CTRL = / lets you comment out multiple lines of code


CONTROL STRUCTURES:
used to test a condition then instruct code to perform an action if true and do something 
else if false. These are all control structures:

--> Comparison operators: test if a condition is true or false using symbols to compare 
values: <, >, ==, <=, >=, !=

--> If statements: if, elif, else - test a condition and decide to run a piece of code 
based on whether it is true or not. They start with the if keyword and and end with : to tell the 
computer the statement is finished.

--> Booleans: data with only 2 values - True or False. Boolean values always start with 
an uppercase letter. Can be used with if statement to test whether condition is True or 
False. 

--> Boolean operators: allow you to test two or more conditions at one time - and, or, not 

--> Try and except: used to handle unexpected or incorrect data types r values from user 
input. They try statements test whether the user inputs a specific data type or a specific 
value. If not, an error will occur. The except statement is triggered to print a message 
about the error.

WORKING WITH LISTS:
--> Accessing elements in a list:

  Example:
  soups = ['minestrone', 'lentil', 'pho', 'laksa']
  soups[2]   # 'pho'

--> Multi-dimensional lists:
Multi-dimensional lists are lists that contain other lists. They can be accessed 
similarly to one-dimensional lists. Instead of a single pair of [] we use an additional 
set for each dimension past the first.

  Examples:
  List = [['apples', 'oranges', 'lemons'] , ['mangoes']]
  List[0][1])	# 'oranges'

--> sorted()
this function returns a new sorted version of the list.

  Example:
  def combine_sort(lst1, lst2):
    unsorted = (lst1 + lst2) 
    sortedList = sorted(unsorted)
    return sortedList

--> .remove()
To use .remove() on a 2D list, call it on the sublist you are modifying and pass 
the value you want to remove in between the parenthesis ().

--> .insert() 
expects two inputs, the first being a numerical index, followed by any value 
as the second input.

--> .pop()
lets us remove elements at a specific index, it takes an optional single input.(Note: .pop() will return the value that was removed! If we want to know what element was deleted, we simply assign a variable to the call of the .pop() method)

--> .count()
lets us count the number of times item appears in lst. Note: .count() returns a value!

  Example:
  def more_than_n(lst, item, n):
    if lst.count(item) > n:
      return True
    else:
      return False

--> .range()
accepts starting number, ending number (exclusive), and amount to increment by. range() is unique in that it creates a range object, not just a typical list. To use this object as a list, we have to convert it using the built-in function called list(). Range objects do not need to be converted to lists in order to determine their length.

  Example:
  my_range2 = range(2, 9, 2)
  # start at 2, end at 9, increment by 2 after each loop

  Example:
  def every_three_nums(start):
    return list(range(start, 101, 3)

--> .sort()
Lists can be sorted 2 ways - either by using a method or a built-in function. .sort() modifies a list directly. Note: It does not return a value and thus does not need to be assigned to a variable. If we do assign the result of the method, it would assign the value of None to the variable. When sorting a 2D list with .sort(), the list by default will be sorted by the first element in each sublist. 

  Example:


--> .sorted()?????
.sorted() function generates a new list rather than modifying the one that already exists. 
It comes before a list, instead of after as all built-in functions do.

  Syntax:

--> Slicing Lists: 

  Syntax:
  myList[START_NUMBER:END_NUMBER]

--> .zip() 
takes two (or more) lists as inputs and returns an object that contains 
a list of pairs. Each pair contains one element from each of the inputs. 

The object can be converted to a list using the built-in function list(). 
With 2D lists, our inner lists don’t use square brackets [] around the values
because they have been converted into tuples.

TUPLES:
A data structure that allows us to store multiple pieces of data, similar to lists. They are often 
used to store data that is meant to be grouped together, but is not necessarily similar. Unlike lists, 
tuples are immutable.

We use () for tuples, rather than the square brackets used for lists. 

  Example:
  my_info = ('Julie', "Park Slope", "Developer")

--> Unpacking tuples 
"Unpacking" a tuple means you can store the elements inside the tuple in variables.
 
  Example:
  name, neighborhood, occupation = my_info
  name --> Julie
  neighborhood --> Park Slope
  occupations --> Developer

A one element tuple must have a trailing comma, like this one_element_tuple = (Julie,)

LOOPS:
Keywords that let you repeat blocks of code until a condition is met.

--> For Loops
repeat a block of code a fixed # of times

  Syntax:
  for <temporary variable> in <collection>:
    <action>

  Example:
  for i in range(1,21):
  print(i)

  Example:
  password = input(‘Please provide a password’)
  num_ct = 0

  for letter in password:
    if letter.isnumeric() == True
      num_ct += 1
    print(‘Your password contains ’, num_ct, ‘ digits)


--> While Loops
perform a set of instructions as long as a given condition is true.

  Syntax:
  while <conditional statement>:
    <action>

LOOP CONTROL STATEMENTS:

--> break
lets you terminate the loop when a certain condition is  met. Break is
usually paired with a conditional

--> continue
skips the current iteration of a loop when a condition is found true. 
Continue is usually paired with a conditional. 

  Example:
  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
    for age in ages:
      if age < 21:
        continue
    print(age)

  Example:
  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
  scoops_sold = 0

  for location in sales_data:
    print(location)
    for element in location:
      scoops_sold = scoops_sold + element
  print("A total of", scoops_sold, "scoops were sold across all locations.")



LIST COMPREHENSIONS:
list comprehensions let use write loops using less code????

  Syntax:
  new_list = [<expression> for <element> in <collection>]

list comprehensions can also include conditional logic. 


FUNCTIONS:

The parameter is the name defined in the parenthesis of the function and 
can be used in the function body. (Parameters are treated like variables
within a function.)

The argument is the data that is passed in when we call the function and 
assigned to the parameter name. (Arguments are like values when we call the 
function)

3 types of arguments
- Positional: can be called by their position in the function definition.
- Keyword: can be called by their name.
- Default: are given default values.

Functions can also return a value to the program so that this value can be 
modified or used later. We use the Python keyword return to do this.

BUILT-IN FUNCTIONS:
max(), min(), round(), len()


STRINGS:
A string can be thought of as a list of characters. Each character has an index.

Unlike a regular list, strings are immutable - they cannot be changed once they are created. 
We can create new strings from a string, but we cannot change the string itself.

--> Concatentation:
A string can be concatenated with another string using +

--> Slicing:
We can "slice" a single character or more than one.
  
  Syntax: 
  string[first_index:last_index]

We can also use negative indices to count backward from the end of the string.
The last character is [-1]

--> Escape characters:
A special character can be used in s string when we add a backslash in front of it. 

  Example:
  
--> Iterating through stings
Because strings are lists, we can iterate through them using for or while loops. 

  Example:
  favorite_fruit = "blueberry"
  counter = 0
  for character in favorite_fruit:
    if character == "b":
    counter = counter + 1
    print(counter)

  Example:
  def letter_check(word, letter):
    for character in word:
      if character == letter:
        return True
    return False

Note - when using a for loop to iterate through a string, we don't need to initialize 
the variable. The for loop statement will initialize the variable to the first character 
of the string.

--> In
We can also use "in" to check if one string is part of another string.
  Example:


STRING METHODS:
String methods enable us to perform complicated tasks on strings quickly and efficiently. String methods can only create new strings, they do not change the original string.  

A string method is called at the end of a string and each one has its own method specific arguments. 

  Syntax: string_name.string_method(arguments)


--> .split()
Splits a string into a list of items. If an argument is passed, that value is used as the delimiter on which to split the string. If no argument is passed, the split will be made where there is whitespace. 

  Example:
  text_list = text.split(",")

To split by something in a string that is not necessarily a character, we can use escape sequences.

  \n Newline - splits multi-line string by line breaks
  \t Horizontal Tab - splits string by tabs

  Example: 
  chorus_lines = smooth_chorus.split('\n')

--> .join()
takes a list of strings and creates a string. It acts on the delimiter you want to join with, therefore the list you want to join has to be the argument.

  Syntax:
  'delimiter'.join(list_you_want_to_join)

Any string can be used as a delimiter to join together a list of strings.

Comma is often used because it lets us create a string of comma separated 
variables, or CSV.

You can also join using escape sequences, such as \n as the delimiter

--> .strip()
cleans off wnoise from the beginning and end of a string. It can be used to 
remove whitespace or a character argument.

  Example:

--> .replace() 
replaces all instances of a character/string in a string with another 
character/string. 

it takes two arguments and replaces all instances of the first 
argument in a string with the second argument. 

  Syntax: 
  string_name.replace(character_being_replaced, new_character)

  Example:


--> Find
searches a string for a character/string and returns the index value that character/string is found at.

it takes a string as an argument and searches the string it was run on for that string. It then returns the first index value where that string is located.

--> Format
allows you to interpolate a string with variables. It replaces empty brace {} placeholders in the string with its arguments.

  Syntax: 
  string_name.format(argument1, argument2)

.format() can be made even more legible by including keywords. Using keywords allows us list our arguments in any order, not just the order we want them to appear in the string.


MODULES:
A module is a collection of Python declarations intended broadly to be used as a tool. Modules are also often referred to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

  Syntax:
  from module_name import object_name

Sometimes the module name and the name of the object you want to import are the same.

- Namespaces: A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run. Python defaults to naming the namespace after the module being imported.

We can also use aliases to give the module our own name.
  Syntax:
  import module_name as name_you_pick_for_the_module

- Decimal is a good module for dealing with the weird formatting that floating point arithmetic can cause

datetime module
required: year, month, day
optional: hour, minute, second, microseconds, timezone

days of week or numbered 0-6 with 0 as Monday

  Example:
  birthday = datetime(1976, 7, 31, 9, 30, 15)

  birthday.year
  prints this >>> 1976

datetime.now()

we can also use subtract with datetime using the minus sign, this is calle datetime delta.but dates can't be added or multiplied

--> strptime() function allows us to take a string and parse through it to convert it into a datetime. (The 'P' stands for "parse.)

--> strftime() function allows to take a datetime and convert it into a string.


FILES:
like variables, files and classes have scope. Even files inside the same directory do not have access to each other’s variables, functions, classes, or any other code. Files are actually modules, so you can give a file access to another file’s content using the import statement


DICTIONARIES:
A python dictionary is an unordered collection of items. It contains data as a set of key: value pairs. Values can be any type – string, integer, list, another dictionary, boolean, etc. Keys, however, must always be an immutable data type, such as strings, numbers, or tuples.

  Example:
  my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}


Access a value in a dictionary:
Values can be accessed by placing the key within square brackets next to the dictionary.

  Example:
  zodiac_elements["earth"]


Access a value in a nested dictionary:
In order to access the value of any key in the nested dictionary, use indexing [] syntax.

  Dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}
 
  Dict['Dict1'][1]	# 'Geeks'
  Dict['Dict2']['Name'] # 'For'


--
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'] , ['Geeks']]
 
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
--

Values can be written by placing a key within square brackets next to the dictionary and using the assignment operator (=). If the key already exists, the old value will be overwritten. 

  Example:
  my_dictionary["song"] = "Paradise City"

Python will throw a KeyError if we try to access a key that does not exist. There are a few ways to check for the existence of a key, so we can avoid this error

--> with "in" using an if statement

  Example:
  key_to_check = "Landmark 81"
 
  if key_to_check in building_heights:
    print(building_heights["Landmark 81"])

  
-- > or by just using "in" to return a boolean value
  
  Example:
  inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10}
 
  print("the peacemaker" in inventory)
  # returns False because this key does not exist


--> try/except
  
  Example:
  key_to_check = "Landmark 81"
  try:
    print(building_heights[key_to_check])
  except KeyError:
    print("That key doesn't exist!")

--> .get()
Takes a key and searches for the corresponding value. By default, it returns None if the key does not exist. 

  Example:
  building_heights.get("My House")
  # returns the value corresonding to the key "My House"
  # returns None if the key doesn't exist 

With. get() we can also specify a value to return if they key does not exist. 

  Example:
  building_heights.get('Mt Olympus', 0)
  # returns 0 if they key doesn't exist

--> .pop()
lets us delete a key:value pair from a dictionary as long as we have the key value. it takes a key as an argument and removes it from the dictionary. At the same time, it also returns the value that it removes from the dictionary.

  Example:
  old_dict.pop("old key")

It also let us provide a default value to return if the key does not exist.

  Example:
  old_dict.pop("old key", "key doesn't exist")


To pop a value from one dictionary and assign it to another, you can use syntax like:

  new_dict["new key"] = old_dict.pop("old key")

--> list() function
the built-in list function lets us get a list of the keys in a dictionary


Merging Dictionaries with .update()
Python makes it easy to combine two dictionaries using the .update() function.

  Example:
  dict1 = {'color': 'blue', 'shape': 'circle'}
  dict2 = {'color': 'red', 'number': 42}
 
  dict1.update(dict2)
 
  # dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}

  For dict1.update(dict2), the key-value pairs of dict2 will be written into 
  the dict1 dictionary. For keys in both dict1 and dict2, the value in dict1 
  will be overwritten by the corresponding value in dict2.

Key-Value Methods:
there are multiple methods that return objects that contain the dictionary keys and values. they don't let us modify the dictionary, but are useful as they can be used to iterate through keys and values in dictionaries.

--> .keys() 
returns the keys through a dict_keys object. 

--> .values() 
returns the values through a dict_keys objects

--> .items() 
returns a dict_list object. Each element is a tuple consisting of: (key, value). It can also be useful for iteration.

  Example:
  pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, 
  "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

  for role, value in pct_women_in_occupation.items():
    print("Women make up " + str(value) + " percent of " + str(role) + "s")




List comprehension:
We can also create a dictionary using a list comprehension. 

  Syntax:
  new_dict = {key:value for key, value in zip(key_list, value_list)}

  Example: 

  Use a list comprehension to create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount   pair for each song in songs and each playcount in playcounts
 
  songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]

  playcounts = [78, 29, 44, 21, 89, 5]

  plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}


FILES:

Reading a File:

.open()
We use .open() to read a file. This creates a file object that points to our text file. By default it opens the file in read-mode. We don't need to indicate this, but we can opt to by passing second argument, 'r', to open(). 

  Example:
  with open('real_cool_document.txt') as cool_doc:

.read()
We can then use .read() to read the contents and save the result to a variable as a single string.

  Example:  
  with open('real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
    print(cool_contents)

.readlines() 
Lets us iterate through a file line by line and store each line in a variable.

  Example:
  with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)

"parsing" or “parsed” means to make something understandable. For programming this is converting information into a format that’s easier to work with. So the phrase “parsed as a string” means we are taking the data from the csv file and turning it into strings. This is important in that we now have a long string and will need to convert it if we want to utilize the numbers within it.

In Python we can convert that data into a dictionary using the csv library’s DictReader object. 

.readline() 
When we don’t want to iterate through a whole file, we can use .readline() to read a single line at a time. 

  Example:
  with open('millay_sonnet.txt') as sonnet_doc:
    first_line = sonnet_doc.readline()
    second_line = sonnet_doc.readline()
    print(second_line)

.write() 
lets us create a file, as well as write over or just append an existing file.

'w' mode: 
to open a file in write-mode, we pass 'w' to open() as our second argument. Note: If the file already exists, this will completely write over it!!! We can then use .write() to indicate the text we want.

  Syntax:
  with open('file_to_write.txt', 'w') as file_object:
    # indent

  Example:
  with open('bad_bands.txt', 'w') as bad_bands_doc:
      bad_bands_doc.write("Back Street Boys")


'a' mode:
to append a file, rather than completely write over it, we pass 'a' as the second argument in open(). We then use .write() to indicate the text we want to add. This adds a new line with our text to the end of the file. 

  with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.write('Air Buddy')

WITH
The with keyword invokes a "context manager" for the file that we’re calling open() on. It takes care of opening the file when we call open() and then closing it after we leave the indented block. Since the files exist outside our Python script, we need to tell Python when we’re done with them so it can close the connection to that file. Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file. 

The with syntax replaces older ways to access files where you need to call .close() on the file object manually. We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards.

  Syntax (the old way):

  fun_cities_file = open('fun_cities.txt', 'a')
 
  # We can now append a line to "fun_cities".
  fun_cities_file.write("Montréal")

  # But we need to remember to close the file
  fun_cities_file.close()


** Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand. 

Reading a CSV File:
CSV files are an example of a text file that impose a structure to their data. Even though we can read them, there are ways to access the data in formats better suited for programming purposes. In Python, we can convert the data into a dictionary usig the csv library's DictReader object.

We call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.


  Example:
  
  users.csv

  Name,Username,Email
  Roger Smith,rsmith,wigginsryan@yahoo.com
  Michelle Beck,mlbeck,hcosta@hotmail.com
  Ashley Barker,a_bark_x,a_bark_x@turner.com


  import csv
 
  list_of_email_addresses = []
  with open('users.csv', newline='') as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
      list_of_email_addresses.append(row['Email'])

Steps:
1. import the csv library, so we can access the tools to parse our CSV file
2. create an empty list, which we’ll later populate with data from our CSV 
3. open up the CSV file in a temporary variable, include any optional additional arguments. (In our example, we're passing the       keyword argument newline='' to the file opening open() function so we don’t mistake a line break in a data field for a new row inour CSV)
5. use csv.DictReader() to convert the lines of our CSV file to Python dictionaries. By default, the 
   keys of the dictionary are the entries in the first line of our CSV file. 


Writing a CSV File:

  Example:

  access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 
  'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}]

  fields = ['time', 'address', 'limit']


  import csv

  with open('logger.csv', 'w') as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

    log_writer.writeheader()
    for item in access_log:
      log_writer.writerow(item)

Steps:
1. import the csv library
2. open the CSV file in a temporary variable, include any optional additional arguments. (In our example, we pass 'w' to open the file in write-mode.)
3. create an instance of csv.DictWriter() and save it to new variable. Pass the arugments (In our example, we pass logger_csv as the first argument, and then fields as a keyword argument to the keyword fieldnames.)
4. write the header using the .writeheader() method.
5. iterate through the list and add each element to the CSV using log_writer.writerow().


Reading a JSON File:

import json

with open('message.json') as message_json:
  message = json.load(message_json)

print(message['text'])

1. import the json library
2. Open up the JSON file in a temporary variable, include any optional additional arguments. 
3. Parse the open file using json.load() to create a Python dictionary and save it to a new variable.
4. To print out a key or value, include it in parentheses inside square brackets


Writing a JSON File:
