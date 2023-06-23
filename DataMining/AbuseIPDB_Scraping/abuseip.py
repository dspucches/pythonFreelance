# Author: Dominic Spucches
# Date: 6/20/2023
# About: These script was built to input a set of IP addresses then gathers the required data from the output. This includes the number of times that IP has been reported; the domain it's associated with; and the report table. This will output the data into a CSV file.

import openpyxl
import tkinter as tk
import time
import sys

from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
from contextlib import redirect_stdout


def uploadform(event=None):
    filename = filedialog.askopenfilename()  # stores imported file into the variable 'filename'
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active

    for cell in sheet['A']:
        value = cell.value

        browser = webdriver.Edge()  # Sets the browser to Microsoft Edge
        browser.get('http://www.abuseipdb.com/')  # opens the edge browser with abuseipdb.com
        assert 'AbuseIPDB' in browser.title

        elem = browser.find_element(By.CLASS_NAME, 'form-control')  # Find the search box by html class name
        elem.send_keys(value + Keys.RETURN)  # inserts the IP address then hits the return key to search

        elem = browser.find_elements(By.ID, 'report-wrapper')  # finds the entire report of the search
        if 'was found in our database!' in elem[0].text:
            elem = browser.find_element(By.CLASS_NAME, 'text-primary')
            workbook = Workbook()
            sheet = workbook.active
            row_num = 0
            for row in sheet.iter_rows(min_row=1):
                for cell in row:
                    cell.value = elem.text
                    row_num += 1
                    workbook.save('hello.xlsx')
            # print(elem.text)
            # print(naughtyip.text)
        else:
            print(value + " was not identified as malicious")

        time.sleep(10)
        browser.quit()
        # driver.implicitly_wait(35)


root = tk.Tk()
button = tk.Button(root, text='Import Excel Document', command=uploadform, height=5, width=45)
button.pack()
root.mainloop()

abuseipdbscript.txt
Displaying abuseipdbscript.txt.
