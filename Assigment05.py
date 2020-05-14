# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Tao Ye,5.13.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    fileHandle = open(objFile, "r")
    for row in fileHandle:
        lstRow = row.split(",")
        dicRow = {"Task":lstRow[0], "Priority":lstRow[1].strip()}
        lstTable.append(dicRow)
    fileHandle.close()
except FileNotFoundError:
    print(objFile," does not exist yet.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task" + "  " + "Priority")
        for dicRow in lstTable:
            print(dicRow["Task"] + "  " + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task: ")
        taskExist = False
        for dicRow in lstTable:
            if (dicRow["Task"].lower() == strTask.lower()):
                taskExist = True
                break
        if (not taskExist):
            strPriority = input("Enter a Priority: ")
            dicRow = {"Task":strTask, "Priority":strPriority}
            lstTable.append(dicRow)
        else:
            print("The task", strTask, "already exists in the list.")
        continue
    # Step 5 - Remove an existing item from the list/Table
    elif (strChoice.strip() == '3'):
        taskChoice = input("What task would you like to delete?: ")
        taskExist = False
        for dicRow in lstTable:
            if (dicRow["Task"].lower() == taskChoice.lower()):
                lstTable.remove(dicRow)
                taskExist = True
        if (not taskExist): print("The task", taskChoice, "is not in the list.")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        fileHandle = open(objFile, "w")
        for dicRow in lstTable:
            fileHandle.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        fileHandle.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        fileHandle = open(objFile, "w")
        for dicRow in lstTable:
            fileHandle.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        fileHandle.close()
        input("Please hit Enter to exit")
        break  # and Exit the program
