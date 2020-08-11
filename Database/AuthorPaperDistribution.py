import sqlite3
from time import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def TotalTime(start, end):
    total = end - start
    hours = total // 3600
    total -= hours * 3600
    mins = total // 60
    total -= mins * 60
    #total = total // 1
    print("Total time taken:")
    print("Hour:\t\t\t%d" %hours)
    print("Minutes:\t\t%d" %mins)
    print("Seconds:\t\t%d" %total)

def GetDistribution(Author, Max):
    ds = [0 for i in range(1000)]
    index = [i for i in range(1000)]
    for i in range(len(Author)):
        ds[Author[i][0]] += 1
    #df = pd.DataFrame(ds)
    plt.plot(index , ds)
    plt.show()
    plt.savefig("Distribution.png")


def AuthorPaperStats():
    conn = sqlite3.connect("Connection.db")
    sql = "SELECT Authors FROM AuthorPaper"
    cursor = conn.execute(sql)
    Authors = []
    for Author in cursor:
        Authors.append(Author)
    conn.close()
    Authors.sort()
    GetDistribution(Authors, Authors[len(Authors)-1])

def main():
    AuthorPaperStats()

if __name__=="__main__":
    main()   