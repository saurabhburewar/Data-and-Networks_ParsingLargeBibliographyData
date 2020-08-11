import csv
from time import time
import sqlite3

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

def FileScanned(Command, Completed = -1):
    if(Command):
        pass
    pass

def CreateTable(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Paper' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE Paper
    (ID INT PRIMARY KEY     NOT NULL,
    Title            TEXT    NOT NULL,
    Published         INT  NOT NULL,
    Updated           INT  NOT NULL);''')
    print("Paper Database Table Successfully Created")

def Check(Cursor, Id):
    Paper = Cursor.execute("SELECT ID FROM PAPER WHERE ID=%d"%Id)
    if Paper.fetchone() is None:
        return False
    return True

def update():
    pass

def Insert(Cursor, Id, Title, Published, Updated):
    if(Check(Cursor, Id)):
        return
    Cursor.execute("INSERT INTO Paper (ID, Title, Published, Updated) \
        VALUES(?, ?, ?, ?)" ,(Id , Title , Published , Updated))

def DisplayPapers(Cursor):
    Papers = Cursor.execute("SELECT ID,Title,Published,Updated FROM Paper")
    print("\nDisplaying Paper Data..........")
    for Paper in Papers:
        print("_____________________________________________")
        print("ID\t:\t\t%d"%int(Paper[0]))
        print("Title\t:\t\t%s"%str(Paper[1]))
        print("Published Date :\t%s"%str(Paper[2]))
        print("Update Date :\t\t%s"%str(Paper[3]))

def main():
    Connection = sqlite3.connect("FileData.db")
    Cursor = Connection.cursor()
    CreateTable(Cursor)
    filename = '../Data/PaperDetails.csv'
    with open(filename , 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            paper_id = int(row[0])
            title = str(row[3])
            published = int(row[2][0:4])
            updated = int(row[1][0:4])
            Insert(Cursor, paper_id, title, published, updated)
    Connection.commit()
    DisplayPapers(Cursor)
    Connection.close()

if __name__=="__main__":
    start = time()
    main()
    end = time()
    TotalTime(start, end)