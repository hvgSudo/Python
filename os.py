import os
import datetime
os.remove(input("Enter the file you want to remove with extension: "))
os.rename(input("Enter the old name: "), input("Enter the new name: "))
print("Existence of file is "+ os.path.exists(input("Enter the file name: ")))
print("The size of the given file is "+ os.path.getsize(input("Enter the file name whose size is to be found: ")))
timestamp = os.path.getmtime(input("Enter the name of the file to get the time the file was last modified: "))
a = datetime.datetime.fromtimestamp(timestamp)
print(a +" in the format YYYY-MM-DD")
print(os.path.abspath(input("Enter the file name to get the current location of the file: ")))
print("Current directory: "+ os.getcwd())
os.chdir(os.mkdir(input("Enter the name of the new directory: ")))
print("Current directory: "+ os.getcwd())

#Directory won't be removed if it is not empty

os.rmdir(input("Enter the name of the directory you want to remove: "))
print("Current directory: "+ os.getcwd())
c = input("Enter the directory: ")
print(os.listdir(c))
for name in os.listdir(c):
  fullname = os.path.join(c, name)
  if os.path.isdir(fullname):
    print("{} is a directory".format(fullname))
  else:
    print("{} is a file".foramt(fullname))