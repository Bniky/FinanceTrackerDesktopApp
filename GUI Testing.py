import tkinter as tk
from tkinter import messagebox
import csv

root = tk.Tk()

listo = []

listo.append(tk.Entry(root,width= 50,borderwidth=1))
print(listo)
listo[0].grid(row=0, column=0, padx=5)

# typefield = tk.Entry(root,width= 50,borderwidth=1)
# namefield = tk.Entry(root,width= 50,borderwidth=1)
# amountfield = tk.Entry(root,width= 50,borderwidth=1)
# datefield = tk.Entry(root,width= 50,borderwidth=1)
#
# typefield.pack()
# namefield.pack()
# amountfield.pack()
# datefield.pack()
#
#
# root.title("GUI Testing")
#
# frame = tk.LabelFrame(root, padx = 50, pady = 50)
# frame.pack(padx=100,pady=100)
#
# def addrow(file, row):  # Adds a row of data
#     with open(file, "a", newline="") as f:
#         Fwriter = csv.writer(f)
#         Fwriter.writerow(row)
#
#
# def CommandBlue():
#     listi = []
#     listi.extend([typefield.get(),namefield.get(),amountfield.get(),datefield.get()])
#     addrow("testing.csv",listi)
#
# def Click():
#     label = tk.Label(frame,text=e.get(),bg="yellow",).pack(pady=5)
#
# def Popup():
#     messagebox.askyesno("Test", "Further Test")
#
# button = tk.Button(frame,text="Click Here BOIIIII", command=CommandBlue, bg="blue",fg="white").pack()
#
# button2 = tk.Button(frame, text="Pop Up", command = Popup, bg="blue",fg="white").pack()

root.mainloop()

