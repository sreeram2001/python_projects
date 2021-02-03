# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:50:05 2021

@author: SREERAM S
"""

from prettytable import PrettyTable
table = PrettyTable()    #creating table

#adding elemets in row
table.field_names = ["Name", "Number", "Age", "Gender"]
table.add_row(["Sreeram", 57, 19, "Male"])
table.add_row(["John", 69, 25, "Male"])
table.add_row(["Jane El", 24, 18, "Female"])
table.add_row(["David", 4, 23, "Male"])
table.add_row(["Nancy", 9, 19, "Female"])

#adding a column 
table.add_column("Donation($)",[12, 20, 150, 46, 19])
print(table)

print(table.get_string(fields=["Name", "Gender"])) #specific 

#styling text to left
table.align = "l"

print(table.get_string(sortby="Donation($)"))

from prettytable import from_csv
with open('E:/study_material/CIR/ECE_companies.csv', 'r') as fp:
    mytable = from_csv(fp)
    
    
    