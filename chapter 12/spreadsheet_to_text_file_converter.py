import openpyxl
import sys
import os
import glob



sourcefilename = os.path.basename(sys.argv[1]) # pass file name in command line


sourcefilename_split = sourcefilename.split('.')
print('Opening workbook: %s' %(sourcefilename))
wb = openpyxl.load_workbook(sourcefilename)
ws1 = wb.active


temp = []
for row in ws1.rows:
    # Append a list of column values
    temp.append( [cell.value for cell in row])

print(temp[0]) #print header row


for i in range(ws1.max_column):
    with open(f'{sourcefilename_split[0]}_{temp[0][i]}.txt','w') as file_object: #gets header from first row
        for l in temp[1:]:
            file_object.write(f'{l[i]} \n')
print('Done')


