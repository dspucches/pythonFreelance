import tkinter
from tkinter import *
from tkinter import filedialog
import pandas as pd

def on_input_button_click():
    file_path = filedialog.askopenfilename()
    file_path_label.config(text=file_path)

    # Read Excel file and get data into pandas DataFrame
    df = pd.read_excel(file_path)

    # Do something with DataFrame, e.g. print it
    print(df)

root = Tk()

label = Label(root, text="Enter some text:")
label.pack()

text_input = Entry(root)
text_input.pack()

input_button = Button(root, text="Import Excel file", command=on_input_button_click)
input_button.pack()

file_path_label = Label(root, text="")
file_path_label.pack()

root.mainloop()
