import xlrd
import mysql.connector
book = xlrd.open_workbook("/home/kingston-machismo/Documents/mySQL.xls")
sheet = book.sheet_by_name("Sheet1")

database = mysql.connector.connect(
    host="localhost",
    user="kingston-machismo",
    passwd="AbcD123#",
    database="dbms"
)

cursor = database.cursor()
query = """INSERT into Publisher (Pid, Pname) VALUES (%d, %s)"""

for r in range(1, sheet.nrows):
    Pid = sheet.cell(r, 0).value
    Pname = sheet.cell(r, 1).value

    values = (int(Pid), Pname)
    cursor.execute(query, values)

cursor.close()
database.commit()
database.close()
print("Data entered")