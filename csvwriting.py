import csv
import os

def addrow(file,row): # Adds a row of data
    with open(file,"a", newline="") as f:
        Fwriter = csv.writer(f)
        Fwriter.writerow(row)
    pass

def fileCheck(file, header=["Name","Amount"]): # Checks to see if file is empty/has right headers
    info = os.stat(file)
    if info.st_size == 0: #  If file is empty
        addrow(file,header)
        print("File was empty, headers added")
        return True
    else:
        print("Has something", info.st_size)
        with open(file,"r") as f:
            Freader = csv.reader(f)
            if next(Freader)!= header: # If first line diff to header
                #print(f"{file} has different Headers to the default")
                return False
            else:
                return True


def addrows(): # Adds multiple rows of data
    pass

# def fieldCheck(row): # Checks if each piece of data is the right type
#     if type(row[0])== str and type(row[1]) == float:
#         pass












