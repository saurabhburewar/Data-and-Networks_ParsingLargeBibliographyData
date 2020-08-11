import csv
from time import time
import sqlite3
import math

def TotalTime(start, end):
    second = end - start
    hour = second // 3600
    second -= hour * 3600
    minutes = second // 60
    second -= minutes * 60
    second = second // 1
    print("___________________Time Taken______________________")
    print("Hour\t:\t\t%d"%hour)
    print("Minutes\t:\t\t%d"%minutes)
    print("Seconds\t:\t\t%d"%second)
    print("____________________________________________________")

def nCr(n,r):
    if(n < r):
        return 0
    f = math.factorial
    return f(n) // f(r) // f(n-r) 

def CreateTable(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='AuthorPaper' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE AuthorPaper
    (ID INT PRIMARY KEY NOT NULL,
    PublishedYear   TEXT NOT NULL,
    Authors         INT NOT NULL,
    Pairs           INT NOT NULL);''')
    print("AuthorPaper Database Table Created")

def Check(Cursor, Id):
    Entry = Cursor.execute("SELECT ID FROM AuthorPaper WHERE ID=%d"%Id)
    if Entry.fetchone() is None:
        return False
    return True

def Update():
    pass

def Insert(Cursor, Id, PublishedYear, Authors, Pairs):
    if(Check(Cursor, Id)):
        return
    Cursor.execute("INSERT INTO AuthorPaper (ID, PublishedYear , Authors , Pairs) \
        VALUES(%d , %s , %d , %d)" % (Id , PublishedYear , Authors , Pairs))

def DisplayAuthorPaper(Cursor):
    Entries = Cursor.execute("SELECT * FROM AuthorPaper")
    print("Displaying Author Paper Connection Data................")
    for Entry in Entries:
        print("__________________________________________________________")
        print("Paper Id:\t\t\t%d"%Entry[0])
        print("Published Year:\t\t\t%s"%Entry[1])
        print("Number of Authors:\t\t%d"%Entry[2])
        print("Total Co_author Pairs:\t\t%d"%Entry[3])

def main():
    Connection = sqlite3.connect("Connection.db")
    Cursor = Connection.cursor()
    CreateTable(Cursor)
    temp = 0
    with open('../Data/AuthorPaperConnections.csv' , 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if(temp != 0):
                temp -= 1
                continue
            PaperId = int(row[1])
            PublishedYear = str(row[2][0:4])
            Authors = int(row[4])
            Combinations = int(nCr(Authors , 2))
            Insert(Cursor,PaperId,PublishedYear,Authors,Combinations)
            temp = Authors - 1
    Connection.commit()
    DisplayAuthorPaper(Cursor)
    Connection.close()

if __name__=="__main__":
    start = time()
    main()
    end = time()
    TotalTime(start, end)