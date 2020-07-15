
#%%

# Read CSV

import os

# Set working directory for any computer/os - do this later

#%%

# Read CSV

import csv

# Change this string to include wd later

csvfile = 'C:/Users/cluel/Documents/GitHub/Consumer-Complaints-Erika-Jacobs-Insight-App/input/complaints.csv'

file = open(csvfile, "r")
data = list(csv.reader(file))

rowcount = len(data)-1

#%%
# Get list of Column Names (Header)
# Make dictionary of rows with index as key
# Within row, make dictionary of columns with header as key

row_dict = {}
column_list = []

# Column Names
for header in data[0]:  
    column_list.append(header)
    
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
        
        # Make Company Lower Case
        if column == 'Company':
            row_dict[row][column] = row_dict[row][column].lower()
            continue
            
        # Make Year Field
        if column == "Date received":
            from datetime import datetime
            dateyear = datetime.strptime(row_dict[row][column], '%Y-%m-%d')
            year = dateyear.year
            row_dict[row]['Year']=year
            continue
        
        # Double Quote Product (Because CSV)
        if column == 'Product' and ',' in row_dict[row][column]:
            row_dict[row][column] = '"'+row_dict[row][column]+'"' 
            continue
        
        else:
            continue
        
#%%

# Add Sorted Fields

ProdYearSetList = {}

for row in range(rowcount):
    Product = row_dict[row]['Product']
    Year = row_dict[row]['Year']
    
    if row == 0:
        ProdYearSetList = {(Product, Year)}
    else:
        ProdYearSetList.add((Product, Year))

print(ProdYearSetList)
        
# Do a set for these two and sort first
# financial product (Use Product Field - Find Distinct)
# year (Date received - use datetime)

# SORTED BY
# product (alphabetically)
# year (ascending)

#%%
            
# Add Other Fields

# the total number of complaints (sum will be row count minus header)
# number of companies receiving a complaint (Count Distinct Company)
# highest percentage of complaints directed at a single company (rounded whole number).
         
#%%
        
# Create Final Dictionary

'''
OUTPUT SHOULD BE:
Credit reporting, credit repair services, or other personal consumer reports 2019 3 2 66.6%
Credit reporting, credit repair services, or other personal consumer reports 2020 1 1 100%
Debt Collection 2019 1 1 100%
'''

#%%

# Write Report - Ideas

file = open(csv, "wt")
file.write(data)
file.close()

file.writerow(ROWLIST)

# FINAL PRODUCT: report.csv