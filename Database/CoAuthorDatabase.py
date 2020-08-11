import sqlite3
import csv
from time import time

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

def CreateTable(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='CoAuthor' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE CoAuthor
    (src  INT                NOT NULL,
    dst   INT                NOT NULL,
    Multiplicity        INT  NOT NULL);''')
    print("CoAuthor Database Table Created")

def DisplayCoAuthor(Cursor):
    CoAuthors = Cursor.execute("SELECT src,dst,Multiplicity FROM CoAuthor")
    print("Displaying CoAuthor Data............")
    for CoAuthor in CoAuthors:
        print("____________________________________________________________________")
        print("SOURCE:\t\t\t%d"%CoAuthor[0])
        print("DESTINATION:\t\t%d"%CoAuthor[1])
        print("MULTIPLICITY:\t\t%d"%CoAuthor[2])

def Check(Cursor, src, dst):
    sql = "SELECT src, dst FROM CoAuthor WHERE src=%d AND dst=%d"
    Node1 = Cursor.execute(sql%(src, dst))
    if(Node1):
        return 1
    Node2 = Cursor.execute(sql%(dst, src))
    if(Node2):
        return 2
    return -1

def Update(Connection, Cursor, Source, Destination):
    query = "SELECT src,dst,Multiplicity FROM CoAuthor WHERE src=%d AND dst=%d"
    update = "UPDATE CoAuthor\
            SET Multiplicity=%d \
                WHERE src=%d AND dst=%d"
    Node1 = Cursor.execute(query%(Source, Destination))
    row = Node1.fetchone()
    if row is not None:
        Multiplicity = int(row[2])
        Cursor.execute(update%((int(Multiplicity + 1), Source, Destination)))
        Connection.commit()
        return
    Node2 = Cursor.execute(query%(Destination, Source))
    row = Node2.fetchone()
    if row is not None:
        Multiplicity = int(row[2])
        Cursor.execute(update%((int(Multiplicity + 1), Source, Destination)))
        Connection.commit()
        return
    Insert(Connection, Cursor, Source, Destination)

def Insert(Connection, Cursor, Source, Destination):
    Multiplicity = 1
    Cursor.execute("INSERT INTO CoAuthor (src , dst , Multiplicity) \
        VALUES(?, ?, ?)", (Source , Destination , Multiplicity))
    Connection.commit()

def main():
    Connection = sqlite3.connect("Connection.db")
    Cursor = Connection.cursor()
    CreateTable(Cursor)
    filename = '../Data/CoAuthors.csv'
    with open(filename , 'r') as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        for row in reader:
            Source = int(row[0])
            Destination = int(row[1])
            Update(Connection, Cursor, Source, Destination)
            count += 1
            if count == 100000:
                break
    Connection.commit()
    DisplayCoAuthor(Cursor)
    Connection.close()

if __name__ == "__main__":
    start = time()
    main()
    end = time()
    TotalTime(start, end)