import csv
from time import time
import sqlite3

total = 0

def TotalTime(start, end=time()):
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

def CreateTable(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Author' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE Author
    (ID INT PRIMARY KEY     NOT NULL,
    Name            TEXT    NOT NULL,
    Start           INT     NOT NULL,
    Latest          INT     NOT NULL,
    PaperCount      INT     NOT NULL);''')
    print("Author Database Table Successfully Created")

def FileScanned(Command, Completed = -1):
    if(Command):
        pass
    pass

def Check(Cursor, Id):
    Author = Cursor.execute("SELECT ID FROM Author WHERE ID=%d"%Id)
    if Author.fetchone() is None:
        return False
    return True

#def Update():
#    pass

def Insert(Cursor, Id, Name, Start=0, Latest=0, PaperCount=0):
    if(Check(Cursor,Id)):
        return
    global total
    print("inserting.......%d"%total)
    Cursor.execute("INSERT INTO Author (ID, Name, Start, Latest, PaperCount) \
        VALUES(?, ?, ?, ?, ?)" ,(Id , Name, Start, Latest, PaperCount))
    total += 1
    #print(Id,Name)
    #print("____________________")

def DisplayAuthors(Cursor):
    Authors = Cursor.execute("SELECT ID,NAME FROM Author")
    print("\nDisplaying Author Data..........")
    for Author in Authors:
        print("_____________________________________________")
        print("ID\t:\t\t%d"%int(Author[0]))
        print("Name\t:\t\t%s"%str(Author[1]))
    print("_____________________________")
    print(total)

def main():
    Connection = sqlite3.connect("FileData.db")
    Cursor = Connection.cursor()
    CreateTable(Cursor)
    index = 'a'
    for i in range(27):
        filename = '../Data/AuthorDetails_'+index+'.csv'
        if(i == 26):
            filename = '../Data/AuthorDetails_others.csv'
        with open(filename , 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                author_id = int(row[0])
                name = str(row[1])
                Insert(Cursor , author_id , name)
        index = chr(ord(index) + 1)
    Connection.commit()
    DisplayAuthors(Cursor)
    Connection.close()

if __name__=="__main__":
    start = time()
    main()
    end = time()

    TotalTime(start,end)
