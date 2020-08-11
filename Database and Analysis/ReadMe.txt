This part of the project consists of modules which are used to build databases
and create networks from the data obtained from parsing.

To build databse of Author,Author Paper and paper
**Run Database.py file
Or the files can be run individually

There are four separate independent and two analysis modules for building database of corresponding files.
1> AuthorDatabase.py:
        This file is used to build database from author csv files obtained after parsing 
        the xml pubmed data. 

2> AuthorPaperDatabase.py:
        As the name suggests this file is used to build database from author paper 
        connection data obtained after parsing pubmed data. 

3> PaperDatabase.py:
        This file is used to build database from paper csv file obtained after parsing. 

4> CoAuthorDatabase.py:
        This file is the most important one and also the most time consuming + resource heavy
        It builds database from co_author csv file and involves updating a node information 
        multiplicity between two authors. 
        Running this file is useful if you are dealing with relatively small data. 

5> DatabaseStats.py:
        This file retrieves information from database and after doing certain operations
        displays stats of author paper connection, multiplicity and co_authors.

6> CoAuthorPlot.py:
        This file is used to build a CoAuthorship network with help of snap library
        It retrieves information from CoAuthor database and builds a TNEANet graph from
        obtained data and saves it to data.dot file. After obtaining data.dot file we can 
	obtain image by running graphviz command on it in terminal. 

7> AuthorPaperDistribution.py:
        This file is used to plot distribution of authors per paper
        It takes data from AuthorPaperDatabse and then with help of 
        matplotlib plots the distribution.
        
