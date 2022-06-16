# Deans Lists : Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.

# Name :: Isaiah Moragne
# File name :: dean.py
# Descript :: The program takes in user input, quits if it is the banned ZZZ input, and then ask for GPA. It then checks and states whether or not they achieved Dean's List or Honor Roll or neither.

lname = input('What is your last name? : ')
if lname == 'ZZZ' or lname == 'zzz':
    quit

fname = input('What is your first name? : ')

gpa = float(input('What is your GPA? : '))

if gpa >= 3.5:
    print(fname + ' ' + lname, "has made the Dean's List")
elif gpa < 3.5 and gpa >= 3.25:
    print(fname + ' ' + lname, 'has made the Honor Roll')
else:
    print(fname + ' ' + lname, "has not made Honor roll or the Dean's list ")

# I was going to add a Try/Except to the inputs to prevent Tracebacks but since we are so early on it seems like overkill to me.
