# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
import tkinter as tk

i = 1

def something():
    global i
    i = i + 1
    entry1 = tk.Entry(frame)
    entry1.grid(row=i, column=0)

    clicked = StringVar()
    clicked.set("Expenses")

    drop = tk.OptionMenu(frame, clicked, "Expenses", "Liability", "Assets", "Income")
    drop.grid(row=i, column=2)

    entry3 = tk.Entry(frame)
    entry3.grid(row=i, column=3)

    myButton.grid(row=i + 1, column=0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ii = i +1
    window = tk.Tk()
    window.geometry("800x400")


    window.title("My Computer")

    frame = LabelFrame(window, text="Expense", padx=0, pady=0)
    frame.grid(row=0, column=0, padx=10, pady=10)

    label1 = tk.Label(frame, text='Type')
    label1.config(font=('helvetica', 14))
    label1.grid(row=0, column=0)

    entry1 = tk.Entry(frame)
    entry1.grid(row=1, column=0)

    clicked = StringVar()
    clicked.set("Expenses")

    drop = tk.OptionMenu(frame, clicked, "Expenses", "Liability", "Assets", "Income")
    drop.grid(row=1, column=2)

    entry3 = tk.Entry(frame)
    entry3.grid(row=1, column=3)

    global myButton
    myButton = Button(frame, text="+", command=something)
    myButton.grid(row=2, column=0)

    window.mainloop()
