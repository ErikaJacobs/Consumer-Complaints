
#%%
import os

wd = str(os.path.dirname(os.path.realpath(__file__)))

if '/src/' in wd:
    wd = wd.replace('/src/','')

if '/src' in wd:
    wd = wd.replace('/src','')

# Read CSV

import csv

csvfile = wd+'/input/complaints.csv'

file = open(csvfile, "r")
data = list(csv.reader(file))

rowcount = len(data)-1

#%%
# Get list of Column Names (Header)
# Make dictionary of rows with index as key
# Within row, make dictionary of columns with header as key

row_dict = {}

# Column Names
column_list = data[0]
    
for row in data:
    
    if data.index(row) == 0:
        continue
    
    else:
        rowindex = data.index(row)-1
        row_dict[rowindex] = {}
        
        for column in row:
            columnindex = row.index(column)
            header = column_list[columnindex]
            row_dict[rowindex][header] = column
            
#%%
# Cleaning

for row in range(rowcount):
    
    for column in column_list:
        
        # Make Company and Product Lower Case
        if column == 'Company' or column == 'Product':
            row_dict[row][column] = row_dict[row][column].lower()
            
        # Make Year Field
        if column == "Date received":
            from datetime import datetime
            dateyear = datetime.strptime(row_dict[row][column], '%Y-%m-%d')
            year = dateyear.year
            row_dict[row]['Year']=year
            continue
        
        # Double Quote Product (Because CSV)
        if column == 'Product' and ',' in row_dict[row][column]:
            row_dict[row][column] = row_dict[row][column].replace("'", '"')
            continue
        
        else:
            continue
        
#%%

# Add Sorted Fields
# By Product Alphabetically
# By Year Ascending

for row in range(rowcount):
    Product = row_dict[row]['Product']
    Year = row_dict[row]['Year']
    
    if row == 0:
        ProdYearSet = {(Product, Year)}
    else:
        ProdYearSet.add((Product, Year))

ProdYearSetList = list(ProdYearSet)
ProdYearSetList.sort()

# Create Final Dictionary

finalrowcnt = len(ProdYearSetList)
final_csv = {}

for tup in ProdYearSetList:
    tupindex = ProdYearSetList.index(tup)
    final_csv[tupindex] = {}
    final_csv[tupindex]['Product'] = tup[0]
    final_csv[tupindex]['Year'] = tup[1]

#%%

# Add Remaining Columns
    
for rows in range(finalrowcnt):
    y = final_csv[rows]['Year']
    p = final_csv[rows]['Product']
    
    # Total Number of Complaints
    
    NumComplaints = 0

    for row in range(rowcount):
        
        if p == row_dict[row]['Product'] and y == row_dict[row]['Year']:
            NumComplaints = NumComplaints+1
    
    final_csv[rows]['Number of Complaints'] = NumComplaints
    
    # Number of Companies Receiving Complaint
    
    compDict = {}
    
    for row in range(rowcount):
        
        if p == row_dict[row]['Product'] and y == row_dict[row]['Year']:
            c = row_dict[row]['Company']
            
            if c not in compDict.keys():
                compDict[c]=1
            else:
                compDict[c]=compDict[c]+1
    final_csv[rows]['Number of Complaint Companies']=len(list(compDict.keys()))
    
    # Highest Percentage of Complaints
    
    compList = []
    for key in list(compDict.keys()):
        compList.append(compDict[key])
    
    percent = round(max(compList)/sum(compList)*100)
    final_csv[rows]['Highest Complaint Percentage'] = percent

#%%

# Write Report - Ideas

file = wd+'/output/report.csv'

fieldnames = ['Product', 'Year', 'Number of Complaints', 'Number of Complaint Companies', 'Highest Complaint Percentage']

with open(file, 'w', newline='') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames = fieldnames)

    #write.writeheader()
    
    for rows in range(finalrowcnt):
        write.writerow({fieldnames[0]: final_csv[rows][fieldnames[0]], 
        fieldnames[1]: final_csv[rows][fieldnames[1]],
        fieldnames[2]: final_csv[rows][fieldnames[2]],
        fieldnames[3]: final_csv[rows][fieldnames[3]],
        fieldnames[4]: final_csv[rows][fieldnames[4]]})

# %%
