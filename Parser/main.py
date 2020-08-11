import xml.etree.ElementTree as ET 
import csv
from time import time
import gzip
import os

import OperationHandler
import parser

def main():
    AuthorId = 0
    PaperId = 0
    Completed = 0
    DataBase = []
    TempDataBase = []
    OperationHandler.initials(DataBase,TempDataBase)
    AuthorId, PaperId, Completed= OperationHandler.PrevData(AuthorId , PaperId , Completed)
    for Index in range(5):
        if(Index <= Completed):
            continue
        FileName  = 'pubmed20n' + format(Index,'04d') + '.xml.gz'
        OperationHandler.Download(FileName) 
        File = gzip.open(FileName , 'r')
        Root = ET.parse(File).getroot()
        CoAuthorList = []
        AuthorPaperConnection = []
        Paper = []
        AuthorId,PaperId = Parse(Root,AuthorId,PaperId,DataBase,TempDataBase,CoAuthorList,AuthorPaperConnection,Paper)
        
        Completed += 1
        History = [AuthorId , PaperId , Completed]
        OperationHandler.WriteData(History , CoAuthorList , AuthorPaperConnection , Paper)
        OperationHandler.UpdateDataBase(DataBase , TempDataBase)
        print("file %d completed"%Completed)
        os.remove(FileName)


if __name__ == "__main__":
    StartTime = time()
    main()
    StopTime = time()
    OperationHandler.TotalTime(StartTime , StopTime)