import sqlite3
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

def get_stats(lis,message):
    print(message)
    lis.sort()
    n = len(lis)
    print(n)
    print("Min:\t\t\t%d"%lis[0])
    print("Max :\t\t\t%d"%lis[n-1])
    mean = 0
    for x in lis:
        mean += x
    mean /= n
    print("Mean :\t\t\t%f"%mean)
    if(n%2 == 0):
        n = n//2    
        print("Median:\t\t\t%f"%((lis[n]+lis[n-1])/2))
    else:
        print("Median :\t\t\t%f"%lis[n//2])
    print("_________________________________________________________________")

def AuthorPaperStats():
    conn = sqlite3.connect("Connection.db")
    sql = "SELECT Authors,Pairs FROM AuthorPaper"
    cursor = conn.execute(sql)
    Authors = []
    Papers = []
    for Author,Paper in cursor:
        Authors.append(Author)
        Papers.append(Paper)
    conn.close()
    mean1 = median1 = max1 = min1 = 0
    mean2 = median2 = max2 = min2 = 0
    get_stats(Authors, "Author per Paper stats:")
    get_stats(Papers, "CoAuthor statistics:")

def MultiplicityStats():
    conn = sqlite3.connect("Connection.db")
    sql = "SELECT Multiplicity FROM CoAuthor WHERE Multiplicity >= 1"
    cursor = conn.execute(sql)
    Multiplicity = []
    for weight in cursor:
        Multiplicity.append(weight)
    conn.close()
    get_stats(Multiplicity, "Multiplicity Stats:")

def main():
    AuthorPaperStats()
    MultiplicityStats()

if __name__=="__main__":
    start = time()
    main()
    end = time()
    TotalTime(start, end)
