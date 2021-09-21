# This script works well on debugger but it faces segmentation error while executing
# via terminal.
# This script was developed using VS Code and its run and debug function proved 
# beneficial to run it.
import mysql.connector as m

mydb = m.connect(host="localhost", user="kingston-machismo", passwd="AbcD123#", database="dbms")

mycursor = mydb.cursor()

# Method 1 using pandas 

import pandas as pd
# query = "insert into SIULibrary(Slid, Lname, Location, Noofbranches) values(%d, %s, %s, %d)"
# mycursor.execute(query)
inputData = pd.read_excel("/mnt/d/sql_input_data.xlsx")
data = inputData.values.tolist() 
lst = list() 
for i in data:
    lst.append(tuple(i))
query = "insert into employee(Empid, Empname, Email, Salary, Lid) values (%s, %s, %s, %s, %s)"
mycursor.executemany(query, lst)
mydb.commit()
mydb.close()


# Method 2 using xlrd

'''
import xlrd
l=list()
loc = ("/mnt/d/sql_input_data.xls")
a = xlrd.open_workbook(loc)
sheet = a.sheet_by_index(0)
sheet.cell_value(0, 0)
for i in range(1, 11):
    l.append(tuple(sheet.row_values(i)))

q = "insert into ILibrary(Lid, Lname, city, Area, Slid) values (%s, %s, %s, %s, %s)"
mycursor.executemany(q, l)
mydb.commit()
mydb.close()
'''