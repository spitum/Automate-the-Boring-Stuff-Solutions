import openpyxl
import sys
import os
import glob

#load text files
fileList = glob.glob("*.txt")

#blank spreadsheet
new = openpyxl.Workbook()
dest_filename = f'textfileToSpreadSheet.xlsx'

ws1 = new.active
ws1.title = "Updated"

string_list = []
for file in fileList:
    with open(file,'r') as file_object:
        contents = file_object.readlines()
        string_list.append(contents)

#change from list to list to flat list.
flat_list = [item for sublist in string_list for item in sublist]

#print(flat_list)


for i,line in enumerate(flat_list):
        print(i,line)
        ws1.cell(row=i+1,column=1).value =str(line)


new.save(dest_filename)
new.close()
