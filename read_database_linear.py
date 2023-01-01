import csv
from linear_hashtable_class import *

file_path = "database.csv"

def makeLinearHashTable():
    hashtable_size = 800000
    return LinearHashTable(hashtable_size)

def readDatabaseLinear(x):
    with open(file_path,"r") as database:
        csvreader = csv.reader(database)
        c = 0
        p = 0
        for rows in csvreader:
            if p % 130000 == 0 or p % 400000 == 0:
                print("========================")
                print("Reading Database ("+str(int((p/400000)*100))+"%)")

            p+=1
            c = 1 if c==0 else x.insert([int(rows[0])] + rows[1:])
                
    print("========================")
