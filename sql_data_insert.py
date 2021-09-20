import mysql.connector as m
import pandas as pd

mydb = m.connect(host="localhost", user="kingston-machismo", passwd="AbcD123#", database="dbms")

mycursor = mydb.cursor()

# mycursor.execute("create table SIULibrary(Slid int primary key, Lname varchar(30) not null, Location varchar(20) not null, Noofbranches int default '1')")
query = "insert into SIULibrary(Slid, Lname, Location, Noofbranches) values(%d, %s, %s, %d)"
inputData = pd.read_excel("D:\\sql_input_data.xlsx")
data = inputData.values.tolist()
tup = tuple()
lst = list()
for i in data:
    lst.append(tuple(i))
mycursor.executemany(query, lst)
# mycursor.executemany("select * from flights")