import sqlite3
import snap 
import csv
import math

#__________________________Additional________Utililties______________________________________#

def nCr(n,r):
    if(n < r):
        return 0
    f = math.factorial
    return f(n) // f(r) // f(n-r) 

#__________________________Node Database Operations_________________________________________#

def CreateNodeTable(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='NODES' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE NODES
    (ID INT PRIMARY KEY  NOT NULL,
    AUTHOR_ID       INT         NOT NULL,
    STARTED         INT         NOT NULL,
    LATEST          INT         NOT NULL,
    PAPER_COUNT     INT         NOT NULL);''')
    print("NODE TABLE CREATED")

def CreateEdgeTable(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='EDGES' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE EDGES
    (ID INT PRIMARY KEY NOT NULL,
    src   INT          NOT NULL,
    dst    INT          NOT NULL,
    multiplicity    INT NOT NULL,
    start_year         INT NOT NULL,
    latest_year          INT NOT NULL);''')
    print("EDGE TABLE CREATED")

def InsertNode(conn , NodeId , AuthorId , StartYear , LatestRelease , PaperCount):
    conn.execute("INSERT INTO NODES (ID, AUTHOR_ID , STARTED , LATEST , PAPER_COUNT) \
        VALUES(%d , %d , %d , %d , %d)" % (NodeId , AuthorId , StartYear , LatestRelease , PaperCount))

def update_node():
    pass

def select_node():
    pass

def ShowNodeDatabase(Connection):
    cursor = Connection.execute("SELECT AUTHOR_ID , STARTED , LATEST , PAPER_COUNT from NODES")
    for row in cursor:
        print("ID:\t\t\t%d" % row[0])
        print("Start Year:\t\t%d" % row[1])
        print("Latest Release:\t\t%d" % row[2])
        print("Papers Written:\t\t%d" % row[3])
        print("_______________________________________________________________________")

def NodeDatabase(Graph):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    CreateNodeTable(cursor)
    #insert nodes
    for NI in Graph.Nodes():
        NodeId = NI.GetId()
        AuthorId = Graph.GetIntAttrDatN(NodeId , "author_id")
        StartYear = Graph.GetIntAttrDatN(NodeId , "start_year")
        LatestYear = Graph.GetIntAttrDatN(NodeId , "latest_year")
        PaperCount = Graph.GetIntAttrDatN(NodeId , "paper_count")
        InsertNode(cursor, NodeId, AuthorId, StartYear, LatestYear, PaperCount)
    connection.commit()
    #show_node_database(connection)
    connection.close()
    
#_________________________EDGE DATABASE OPERATIONS__________________________________________#

def InsertEdge(cursor , EdgeId , Source , Destination , Multiplicity , StartYear , LatestRelease):
    cursor.execute("INSERT INTO EDGES (ID, src , dst , multiplicity , start_year , latest_year) \
        VALUES(%d , %d , %d , %d , %d , %d)" % (EdgeId , Source , Destination , Multiplicity , StartYear , LatestRelease))


def update_edge():
    pass

def select_edge():
    pass

def ShowEdgeDatabase(Connection):
    cursor = Connection.execute("SELECT src,dst,multiplicity,start_year,latest_year from EDGES")
    for row in cursor:
        print("SOURCE:\t\t\t%d"%row[0])
        print("DESTINATION:\t\t%d"%row[1])
        print("MULTIPLICITY:\t\t%d"%row[2])
        print("Start Year:\t\t%d"%row[3])
        print("Latest Release:\t\t%d"%row[4])
        print("_________________________________________________________________________________")

def EdgeDatabase(Graph):
    Connection = sqlite3.connect("test.db")
    Cursor = Connection.cursor()
    CreateEdgeTable(Cursor)
    #insert nodes
    temp = 0
    for EI in Graph.Edges():
        EdgeId = EI.GetId()
        Source = EI.GetSrcNId()
        Destination = EI.GetDstNId()
        if(Destination == temp):
            continue
        temp = Source
        Multiplicity = Graph.GetIntAttrDatE(EdgeId , "Multiplicity")
        StartYear = Graph.GetIntAttrDatE(EdgeId , "start_year")
        LatestRealease = Graph.GetIntAttrDatE(EdgeId , "latest_year")
        InsertEdge(Cursor, EdgeId, Source, Destination, Multiplicity, StartYear, LatestRealease)
    Connection.commit()
    #ShowEdgeDatabase(Connection)
    Connection.close()

def build_CoAuthor_database(Graph):
    NodeDatabase(Graph)
    EdgeDatabase(Graph)


#___________________Author Paper Connection Database Builder________________________________#

def create_authpap_table(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='AuthorPaper' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE AuthorPaper
    (ID INT PRIMARY KEY NOT NULL,
    PublishedYear   INT NOT NULL,
    Authors         INT NOT NULL,
    Combinations    INT NOT NULL);''')
    print("AuthorPaper TABLE CREATED")

def insert_authpap(Cursor , PaperId , PublishedYear , Authors , Combinations):
    Cursor.execute("INSERT INTO AuthorPaper (ID, PublishedYear , Authors , Combinations) \
        VALUES(%d , %d , %d , %d)" % (PaperId , PublishedYear , Authors , Combinations))

def ShowAuthorPaperDatabase(Connection):
    cursor = Connection.execute("SELECT ID,PublishedYear,Authors,Combinations FROM AuthorPaper")
    for row in cursor:
        print("Paper Id:\t\t\t%d"%row[0])
        print("Published Year:\t\t\t%d"%row[1])
        print("Number of Authors:\t\t%d"%row[2])
        print("Total Co_author Pairs:\t\t%d"%row[3])
        print("______________________________________________________________________________")

def build_authpap_database():
    Connection = sqlite3.connect("test.db")
    Cursor = Connection.cursor()
    create_authpap_table(Cursor)
    temp = 0
    with open('../Data/AuthorPaperConnections.csv' , 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if(temp != 0):
                temp -= 1
                continue
            PaperId = int(row[1])
            PublishedYear = int(row[2][0:4])
            Authors = int(row[4])
            Combinations = int(nCr(Authors , 2))
            insert_authpap(Cursor,PaperId,PublishedYear,Authors,Combinations)
            temp = Authors - 1
    Connection.commit()
    #ShowAuthorPaperDatabase(Connection)
    Connection.close()


#__________________________________Author Database Builder__________________________________#

def create_author_table(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Author' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE Author
    (ID INT PRIMARY KEY     NOT NULL,
    Name            TEXT    NOT NULL);''')
    print("Author TABLE CREATED")

def insert_author(Cursor , author_id , name):
    Cursor.execute("INSERT INTO Author (ID, Name) \
        VALUES(? , ?)" ,(author_id , name))

def ShowAuthorDatabase(Connection):
    cursor = Connection.execute("SELECT ID,Name FROM Author")
    for row in cursor:
        print("Author Id:\t\t\t%d"%row[0])
        print("Author Name:\t\t\t%s"%row[1])
        print("______________________________________________________________________________")

def build_author_database():
    Connection = sqlite3.connect("CSV.db")
    Cursor = Connection.cursor()
    create_author_table(Cursor)
    index = 'a'
    for i in range(26):
        filename = '../Data/AuthorDetails_'+index+'.csv'
        with open(filename , 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                author_id = int(row[0])
                name = str(row[1])
                insert_author(Cursor , author_id , name)
        index = chr(ord(index) + 1)
    with open('../Data/AuthorDetails_others.csv' , 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            author_id = int(row[0])
            name = str(row[1])
            insert_author(Cursor , author_id , name)
    Connection.commit()
    #ShowAuthorDatabase(Connection)
    Connection.close()    


#__________________________________Paper Database Builder___________________________________#

def create_paper_table(Cursor):
    Cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Paper' ''')
    if(Cursor.fetchone()[0] == 1):
        return
    Cursor.execute('''CREATE TABLE Paper
    (ID INT PRIMARY KEY     NOT NULL,
    Title            TEXT    NOT NULL,
    Released        TEXT NOT NULL,
    Updated         TEXT NOT NULL);''')
    print("Paper TABLE CREATED")

def insert_paper(Cursor , paper_id , title, released, updated):
    Cursor.execute("INSERT INTO Paper (ID, Title, Released, Updated) \
        VALUES(?, ?, ?, ?)" ,(paper_id , title , released , updated))

def ShowPaperDatabase(Connection):
    cursor = Connection.execute("SELECT ID,Title,Released,Updated FROM Paper")
    for row in cursor:
        print("Paper Id:\t\t\t%d"%row[0])
        print("Paper Title:\t\t\t%s"%row[1])
        print("Released On:\t\t\t%s"%row[2])
        print("Updated On:\t\t\t%s"%row[3])
        print("______________________________________________________________________________")

def build_paper_database():
    Connection = sqlite3.connect("CSV.db")
    Cursor = Connection.cursor()
    create_paper_table(Cursor)
    temp = 0
    with open('../Data/PaperDetails.csv' , 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            paper_id = int(row[0])
            name = str(row[3])
            released = str(row[1])
            updated = str(row[2])
            insert_paper(Cursor , paper_id , name, released, updated)
    Connection.commit()
    #ShowPaperDatabase(Connection)
    Connection.close()