import AuthorDatabase
import AuthorPaperDatabase
import CoAuthorDatabase
import PaperDatabase

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

def main():
    AuthorDatabase.main()
    print("Author Database complete")
    AuthorPaperDatabase.main()
    print("AuthorPaper Database complete")
    PaperDatabase.main()
    print("Paper Databse complete")

if __name__=="__main__":
    start = time()
    main()
    end = time()
    TotalTime(start, end)