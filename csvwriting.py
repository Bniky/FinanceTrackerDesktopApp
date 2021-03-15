import csv
import os


def addrow(file, row):  # Adds a row of data
    with open(file, "a", newline="") as f:
        Fwriter = csv.writer(f)
        Fwriter.writerow(row)


def addrows(file, rows, mode="a"):  # Adds a bunch of rows of data
    with open(file, mode, newline="") as f:
        Fwriter = csv.writer(f)
        Fwriter.writerows(rows)


def filecheck(file, header):  # Checks to see if file is empty/has right header
    #Throw in a If loop on whether file exists before you get into stuff below.
    #This Function is sort of useless now, keeping around for now
    info = os.stat(file) #T/F May not be the best thing here, throw in Try catch for file not found
    if info.st_size == 0:  # If file is empty
        addrow(file, header)
        print("File was empty, headers added")
        return True
    else:
        print("Has something", info.st_size)
        with open(file, "r") as f:
            Freader = csv.reader(f)
            if next(Freader) != header:  # If first line diff to header
                # print(f"{file} has different Headers to the default")
                return False
            else:
                return True


def createcsv(file, header):  # Creates csv with headers provided
    if os.path.exists(file):  # Checks if that file path leads somewhere
        print("That filename already exists, choose another")
        return
    else:
        with open(file, "w") as f:
            addrow(file, header)
        return


def changerow(file, rownum, newrow):
    with open(file, "r") as f:
        reader = csv.reader(f)
        lines = list(reader)  # Turn csv into list of lists(rows)

    lines[rownum] = newrow  # Change the row you wanted
    addrows(file, lines, "w")  # Rewrite the whole file



headers = ["Date", "Name", "Amount", "Occurrence", "Type"]

#createcsv("Test.csv",headers)
#addrow("Test.csv",[1,2,3,4,5,6,7,8,9])
#addrows("Test.csv",[[1,2,3,4,5],[1,2,3,4,5]])



