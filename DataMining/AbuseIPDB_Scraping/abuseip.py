# Author: Dominic Spucches
# Date: 6/20/2023
# About: These script was built to input a set of IP addresses then gathers the required data from the output. This includes the number of times that IP has been reported; the domain it's associated with; and the report table. This will output the data into a CSV file.

import pylightxl as ipinput
import tkinter as tk

from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename() # stores imported file into the variable 'filename'
    db = ipinput.readxl(filename) # reads the Excel file and stores into 'db'



root = tk.Tk()
button = tk.Button(root, text='Import Excel Document', command=UploadAction, height=5, width=45)
button.pack()

root.mainloop()