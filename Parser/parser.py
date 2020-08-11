from itertools import combinations
import OperationHandler

def GetAuthors(Article, AuthorId, DataBase, TempDataBase, NameList):
    for AuthorList in Article.findall('AuthorList'):               
        for Author in AuthorList.findall('Author'):
            if(Author[0].text is not None):
                Name = Author[0].text
            ForeName = Author.find('ForeName')
            print(type(Name))  
            if ForeName is not None:
                Name += ForeName.text
            AuthorId+=1
            if(OperationHandler.UpdateId(Name , DataBase , TempDataBase , AuthorId)):          
                AuthorId -= 1                
            NameList.append(OperationHandler.GetId(Name , DataBase , TempDataBase))
    return AuthorId 

def Parse(Root,AuthorId, PaperId, DataBase, TempDataBase, CoAuthorList, AuthPaperConnection, Paper):
    print("Parsing..........")
    for PubMedArticle in Root.findall('PubmedArticle'):
        for MedLineCitation in PubMedArticle.findall('MedlineCitation'):
            for Article in MedLineCitation.findall('Article'):
                PaperId += 1
                title = Article.find('ArticleTitle').text
                Date = MedLineCitation.find('DateRevised')
                MedLineDate = Date[0].text + '-' + Date[1].text + '-' + Date[2].text
                NameList = []
                AuthorId = GetAuthors(Article, AuthorId, DataBase, TempDataBase, NameList)
                NameCombinations = combinations(NameList,2)
                for i in list(NameCombinations):
                    CoAuthorList.append([i[0],i[1], Article.find('Journal/JournalIssue/PubDate')[0].text])   

                for i in range(len(NameList)):
                    AuthPaperConnection.append([NameList[i],PaperId, Article.find('Journal/JournalIssue/PubDate')[0].text,i+1,len(NameList)])
                        
                Paper.append([PaperId,MedLineDate, Article.find('Journal/JournalIssue/PubDate')[0].text,title])
    return [AuthorId, PaperId]
    