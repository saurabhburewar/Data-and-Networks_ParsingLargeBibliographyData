import os
import csv
import requests

def TotalTime(StartTime , StopTime):
    Seconds = StopTime - StartTime
    Hours = Seconds // 3600
    Seconds -= Hours * 3600
    Minutes = Seconds // 60
    Seconds -= Minutes * 60
    Seconds = Seconds // 1
    print("Time Taken")
    print("Hours   : \t\t%d"%Hours)
    print("Minutes : \t\t%d"%Minutes)
    print("Seconds : \t\t%d"%Seconds)

def Download(FileName):
    url = "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/" + FileName
    print("Downloading_________%s"%FileName)
    with open(FileName , "wb") as file:
        r = requests.get(url)
        file.write(r.content)

def CreateBase(DataBase,TempDataBase):
    for i in range(27):
        DataBase.append({})
        TempDataBase.append({})

def Write(filename , mode , lists , message):
    with open(filename , mode) as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in lists:
            csv_writer.writerow(row)
    print(message)

def WriteCsv(TempDataBase):
    Index = 'a'
    for i in range(26):
        FileName = '../Data/AuthorDetails_' + Index + '.csv'
        with open(FileName , 'a+') as csvfile:
            writer = csv.writer(csvfile)
            for key , value in TempDataBase[i].items():
                writer.writerow([value,key])
        Index = chr(ord(Index) + 1)
    with open('../Data/AuthorDetails_others.csv' , 'a+') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in TempDataBase[26].items():
            writer.writerow([value , key])

def PrevData(AuthorId , PaperId , Completed):
    with open('../Data/ids.csv' , 'r+') as csv_file:
        CsvReader = csv.reader(csv_file)
        for row in CsvReader: 
            AuthorId = int(row[0])
            PaperId = int(row[1])    
            Completed = int(row[2])
    print("Hii starting from  ",end = "  ")
    print(Completed)    
    return [AuthorId , PaperId , Completed]

def CreateFiles():
    if not os.path.isdir('../Data'):
        os.mkdir('../Data')
    Index = 'a' 
    for i in range(26):
        FileName = '../Data/AuthorDetails_' + Index + '.csv'
        with open(FileName , 'a+') as csvfile:
            csv_writer = csv.writer(csvfile)
        Index = chr(ord(Index) + 1)
    with open('../Data/AuthorDetails_others.csv' , 'a+') as csvfile:
        csv_writer = csv.writer(csvfile)
    with open('../Data/ids.csv' , 'a+') as csvfile:
        csv_writer = csv.writer(csvfile)

def EmptyTemp(TempDataBase):
    for temp in TempDataBase:
        temp.clear()

def Restore(DataBase):
    Index = 'a'
    for i in range(26):
        FileName = '../Data/AuthorDetails_' + Index + '.csv'
        with open(FileName , 'r+') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                DataBase[i][row[0]] = row[1] 
    with open('../Data/AuthorDetails_others.csv' , 'a+') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            DataBase[26][row[0]] = row[1]

def GetId(Name , DataBase , TempDataBase):
    c = Name[0].lower()
    if(len(c) > 1):
        Index = 26
    else:    
        Index = int(ord(c) - ord('a'))
    if((Index < 0) or (Index >= 26)):
        Index = 26
    if Name in TempDataBase[Index].keys():
        return TempDataBase[Index][Name]
    else:
        return DataBase[Index][Name]

def UpdateId(Name , DataBase ,TempDataBase , AuthorId):
    #print(Name)
    c = Name[0].lower()
    if(len(c) > 1):
        Index = 26
    else:    
        Index = int(ord(c) - ord('a'))
    if((Index < 0 ) or (Index >= 26)):
        Index = 26
    if ((Name not in TempDataBase[Index].keys()) and (Name not in DataBase[Index].keys())):
        TempDataBase[Index][Name] = AuthorId

def AppendData(DataBase , TempDataBase):
    for i in range(27):
        DataBase[i].update(TempDataBase[i])

def WriteData(History , CoAuthorList , AuthorPaperConnection , Paper):
    with open('../Data/ids.csv' , 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(History)
    Write('../Data/CoAuthors.csv' , 'a+' , list(CoAuthorList) , "Co_author Completed")
    Write('../Data/AuthorPaperConnections.csv' , 'a+' , list(AuthorPaperConnection) , "Author Paper Connection Update Completed")
    Write('../Data/PaperDetails.csv' , 'a+' , list(Paper) , "Paper update completed")

def UpdateDataBase(DataBase , TempDataBase):
    WriteCsv(TempDataBase)
    AppendData(DataBase , TempDataBase)
    EmptyTemp(TempDataBase)

def initials(DataBase , TempDataBase):
    CreateFiles()
    CreateBase(DataBase,TempDataBase)
    Restore(DataBase)

