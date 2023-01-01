import csv
from linked_list_hashtable_class import *

file_path = "database.csv"

def makeLinkedHashTable():
    hashtable_size = 800000
    return LinkedListHashTable(hashtable_size)

def readDatabaseLinked(x):
    with open(file_path,"r") as database:
        csvreader,c,p = csv.reader(database),0,0
        
        for rows in csvreader:
            if p % 130000 == 0 or p % 400000 == 0:
                print("========================")
                print("Reading Database ("+str(int((p/400000)*100))+"%)")

            p+=1
            c = 1 if c==0 else x.insert([int(rows[0])] + rows[1:])
                
    print("========================")
