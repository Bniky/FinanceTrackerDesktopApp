import csv
import os
import tkinter as tk
from tkinter import ttk


def subrow(file, row):  # Adds a row of data
    with open(file, "a", newline="") as f:
        Fwriter = csv.writer(f)
        Fwriter.writerow(row)


def subrows(file, rows, mode="a"):  # Adds a bunch of rows of data
    with open(file, mode, newline="") as f:
        Fwriter = csv.writer(f)
        Fwriter.writerows(rows)


def filecheck(file, header):  # Checks to see if file is empty/has right header
    #Throw in a If loop on whether file exists before you get into stuff below.
    #This Function is sort of useless now, keeping around for now
    info = os.stat(file) #T/F May not be the best thing here, throw in Try catch for file not found
    if info.st_size == 0:  # If file is empty
        subrow(file, header)
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
            subrow(file, header)
        return


def changerow(file, rownum, newrow):
    with open(file, "r") as f:
        reader = csv.reader(f)
        lines = list(reader)  # Turn csv into list of lists(rows)

    lines[rownum] = newrow  # Change the row you wanted
    subrows(file, lines, "w")  # Rewrite the whole file


def getheaders(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        return next(reader)#the next line is the first line/headers


def csvfile(file,headers=False):
    with open(file, "r") as f:
        reader = csv.reader(f)
        lines = list(reader)
        if headers == False:
            del(lines[0])
        return lines


def rowadder():
    v1 = typefieldL
    v2 = namefieldL
    v3 = amountfieldL
    v4 = datefieldL
    xpad = 5
    ypad = 2

    rownum = fieldframe.grid_size()[1] # accessing row num from a tuple / starts from 1


    v1.append([tk.Entry(fieldframe),rownum,2])
    v1[rownum-1][0].grid(row=v1[rownum-1][1], column=v1[rownum-1][2], padx=xpad, pady = ypad)

    v2.append([tk.Entry(fieldframe), rownum, 3])
    v2[rownum - 1][0].grid(row=v2[rownum-1][1], column=v2[rownum-1][2], padx=xpad, pady = ypad)

    v3.append([tk.Entry(fieldframe), rownum, 4])
    v3[rownum - 1][0].grid(row=v3[rownum - 1][1], column=v3[rownum - 1][2], padx=xpad, pady = ypad)

    v4.append([tk.Entry(fieldframe), rownum, 5])
    v4[rownum - 1][0].grid(row=v4[rownum - 1][1], column=v4[rownum - 1][2], padx=xpad, pady = ypad)

    rowbutton = tk.Button(fieldframe, text="+", command= lambda: [rowbutton.grid_forget(), submitbutton.grid_forget(), rowadder()])
    rowbutton.grid(row=rownum, column=1)

    submitbutton = tk.Button(fieldframe, text="Submit All", command= lambda: [submitbutton.grid_forget(), rowbutton.grid_forget(), submit()])
    submitbutton.grid(row=rownum+1, column=5)


def submit():
    fieldlist=[typefieldL, namefieldL, amountfieldL, datefieldL]
    rownum = fieldframe.grid_size()[1] # accessing row num from a tuple / starts from 1

    for i in range(0,rownum-1): # subtract 1 because of the headers, all other buttons have vanished by this point
        row = []
        for list in fieldlist:
            row.append(list[i][0].get())

        subrow("testing.csv",row) #Hard coded the csv destination
        print("row here",row)

    for listo in fieldlist:
        for i in listo:
            i[0].grid_forget()

        listo.clear()


    typefieldL.append([tk.Entry(fieldframe),1,2])  # element = [tk field command, row, column]
    namefieldL.append([tk.Entry(fieldframe), 1, 3])
    amountfieldL.append([tk.Entry(fieldframe), 1, 4])
    datefieldL.append([tk.Entry(fieldframe), 1, 5])

    for i in typefieldL:  # May not need these for loops, but they are neat
        i[0].grid(row=i[1], column=i[2], padx=5, pady=2)
    for i in namefieldL:
        i[0].grid(row=i[1], column=i[2], padx=5, pady=2)
    for i in amountfieldL:
        i[0].grid(row=i[1], column=i[2], padx=5, pady=2)
    for i in datefieldL:
        i[0].grid(row=i[1], column=i[2], padx=5, pady=2)

    rowbutton = tk.Button(fieldframe, text="+", command=lambda: [rowbutton.grid_forget(), submitbutton.grid_forget(),                                                                 rowadder()])  # Add row button (TIDY UP!!!!!!!)
    rowbutton.grid(row=1, column=1)
    submitbutton = tk.Button(fieldframe, text="Submit",command=lambda: [submitbutton.grid_forget(), rowbutton.grid_forget(),submit()])  # Singluar submit version of the button
    submitbutton.grid(row=2, column=5)


def csvreader(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        lines = list(reader)  # Turn csv into list of lists(rows)

    lines.pop(0)
    for i in lines:
        data = tuple(i)
        mytree.insert('', 'end', text='', values=data)


def csvupdate(file):
    pass




root = tk.Tk()
root.title("Finance Tracker")

fieldframe = tk.LabelFrame(root, text="Field Entry Frame", padx=5, pady=5)
fieldframe.pack(expand=True, fill="both", side="left", padx=10, pady=10)

treeframe = tk.LabelFrame(root, text="Treeview Frame", padx=5, pady=5)
treeframe.pack(expand=True, fill="both", side="left", padx=10, pady=10)


rowbutton = tk.Button(fieldframe, text="+", command= lambda: [rowbutton.grid_forget(), submitbutton.grid_forget(), rowadder()])# Add row button (TIDY UP!!!!!!!)
rowbutton.grid(row=1, column=1)
submitbutton = tk.Button(fieldframe, text="Submit", command= lambda: [submitbutton.grid_forget(), rowbutton.grid_forget(), submit()]) # Singluar submit version of the button
submitbutton.grid(row=2,column=5)
delplaceholder = tk.Label(fieldframe, text="  ")  # Placeholder column for delete button
delplaceholder.grid(row=0, column=6)

typefieldL = [[tk.Entry(fieldframe),1,2]] # element = [tk field command, row, column]
namefieldL = [[tk.Entry(fieldframe),1,3]]
amountfieldL = [[tk.Entry(fieldframe),1,4]]
datefieldL= [[tk.Entry(fieldframe),1,5]]



for i in typefieldL: # May not need these for loops, but they are neat
    i[0].grid(row=i[1], column=i[2], padx=5, pady = 2)
for i in namefieldL:
    i[0].grid(row=i[1], column=i[2], padx=5, pady = 2)
for i in amountfieldL:
    i[0].grid(row=i[1], column=i[2], padx=5, pady = 2)
for i in datefieldL:
    i[0].grid(row=i[1], column=i[2], padx=5, pady = 2)




typelabel = tk.Label(fieldframe,text="Type")
typelabel.grid(row=0, column=2, sticky="w")
namelabel = tk.Label(fieldframe,text="Name")
namelabel.grid(row=0, column=3, sticky="w")
amountlabel = tk.Label(fieldframe,text="Amount")
amountlabel.grid(row=0, column=4, sticky="w")
datelabel = tk.Label(fieldframe,text="Date")
datelabel.grid(row=0, column=5, sticky="w")


blanklabel0 = tk.Label(fieldframe, text="  ")  # Left blank padding column
blanklabel0.grid(row=1, column=0)
blanklabel2 = tk.Label(fieldframe, text="  ")  # Right blank padding column
blanklabel2.grid(row=0, column=7)




fieldframe.columnconfigure(0, weight=1)  # First and last column are what stretches to fit the resizing...
fieldframe.columnconfigure(7, weight=2)  # effectively keeps rows 1-4 centered

#====================================

mytree = ttk.Treeview(treeframe, show= "headings")

mytree["columns"] = ("Type", "Name", "Amount", "Date")



mytree.column("Type", anchor="w", width=120)
mytree.column("Name", anchor="w", width=120)
mytree.column("Amount", anchor="w", width=120)
mytree.column("Date", anchor="w", width=120)


mytree.heading("Type", text="Type", anchor="w")
mytree.heading("Name", text="Name", anchor="w")
mytree.heading("Amount", text="Amount", anchor="w")
mytree.heading("Date", text="Date", anchor="w")



csvreader("testing.csv")

mytree.grid(row=0, column=0, columnspan=4, padx=5, pady = 2)

blanklabel0 = tk.Label(treeframe, text=" ")  # Left blank padding column
blanklabel0.grid(row=1, column=0)

t_typefield = tk.Entry(treeframe)
t_namefield = tk.Entry(treeframe)
t_amountfield = tk.Entry(treeframe)
t_datefield = tk.Entry(treeframe)

j = 2
t_typefield.grid(row=j, column=0, sticky="w", padx=5, pady = 2)
t_namefield.grid(row=j, column=1, sticky="w", padx=5, pady = 2)
t_amountfield.grid(row=j, column=2, sticky="w", padx=5, pady = 2)
t_datefield.grid(row=j, column=3, sticky="w", padx=5, pady = 2)


















# c = tk.Button(treeframe, text="Bye", command= lambda: csvreader("testing.csv") )
# c.pack()


root.mainloop()

#"Expenses", "Liability", "Assets", "Income"
