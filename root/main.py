from tkinter import *
import sqlite3
import datetime


# Initiate tkinter root
root = Tk()

# Connect to database
conn = sqlite3.connect('ClassDates.db')

# Enable cursor
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE mktingDates(date, assignment)''')
# c.execute('''CREATE TABLE busAnalysis (date, assignment)''')

# Identifies the due date entry box
dueLabel = Label(root, text='Due Date')
dueLabel.grid(row=0, column=0)

# Identifies the assignment entry box
assignmentLabel = Label(root, text='Assignment')
assignmentLabel.grid(row=1, column=0)

# User inputs due date to be added to table
date = Entry(root)
date.grid(row=0, column=1)

# User inputs assignment to be added to table
assignment = Entry(root)
assignment.grid(row=1, column=1)

# When clicked collects the due date and assignment name and adds it to the business analysis table
def enterBtnBus():
    dateData = date.get()
    assignmentData = assignment.get()

    c.execute(f'''INSERT INTO busAnalysis VALUES(
              "{dateData}",
              "{assignmentData}"
              )''')

    conn.commit()
    print('Collected')


# Enter button for business class, when clicked adds the value from the date and assignment entries to the business analysis table
enterBus = Button(root, text='EnterBus', command=lambda: enterBtnBus())
enterBus.grid(row=2, column=3)

# When clicked collects the due date and assignment name and adds it to the marketing table
def enterBtnMkt():
    c.execute(f'''INSERT INTO mktingDates VALUES(
    "{date.get()}",
    "{assignment.get()}"
    )''')

    conn.commit()
    print('Collected')


# Enter button for marketing class, when clicked adds the value from the date and assignment entries to the marketing table
enterMkt = Button(root, text='EnterMkt', command=lambda: enterBtnMkt())
enterMkt.grid(row=2, column=1)

# Shows the user what is due
def dueFunc():
    # Today's date
    today = str(datetime.datetime.today())
    today = f'{today[5:7]}/{today[8:10]}/{today[2:4]}'
    # if today's date == a date in the table, it will show the user which assignment is due
    todaysDate = c.execute(f'''SELECT * FROM busAnalysis WHERE date="{today}"''')
    dueToday = Label(root, text=(str(todaysDate.fetchall())))
    dueToday.grid(row=0, column=3)


# Due date label, displays which assignments, if any, are due today
dueToday = Label(root, text='')
dueToday.grid(row=0, column=3)

# Due date button, allows the user to see which assignments, if any, are due today
dueBtn = Button(root,text='Due', command=lambda: dueFunc())
dueBtn.grid(row=1,column=3)


# Call the mainloop and close the connection to the db
root.mainloop()
conn.close()
