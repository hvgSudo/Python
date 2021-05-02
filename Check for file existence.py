import os
from os import path
def main():
    print(os.name)
    print(os.path)
    print("Item exists: ",str(os.path.exists("D:\ad.txt")))
    print("Item is a file: ",str(os.path.isfile("D:\ad.txt")))

if __name__=="__main__":
    main()
