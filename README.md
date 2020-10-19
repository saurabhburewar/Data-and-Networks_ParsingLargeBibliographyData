# ParsingLargeBibliographyData

## Introduction

The focus of the project will be on two parts: parsing the data (from MEDLINE database), and the analysis of the parsed data. 

The data set, produced by National Library of Medicine (NLM), USA, is baseline set of all the MEDLINE publication records in the field of medical science. It is accessible through the PubMed engine. The data is in xml format and will be parsed into csv format by extracting certain details like co-authorship graphs.

## Requirements

Python 3.6 or above.

For Parser, all libraries are default python3 libraries except for requests. Make sure to install it.

For Database and analysis, make sure these libraries are installed, snap-stanford (link below), pandas, numpy, matplotlib.

Snap.py: https://snap.stanford.edu/snappy/

## Parser

The Parser can be launched through "/Parser/main.py". It downloads the data which is then parsed into csv files. These csv files files will be stored at "/Data".

## Analysis

The data can be analysed by creating a database from the csv files and then plotting distributions.
The database can be created through "Database and analysis/Database.py" and "Database and analysis/CoAuthorDatabase.py".
For the distributions, "Database and analysis/CoAuthorPlot.py" and "Database and analysis/AuthorPaperDistribution.py"

### CSV Analysis

This is another way of analysing where the system analyses data and plots a co-author network from the co-authors.csv file. There is no need to create a database in this case.
This can be done through "CSVAnalysis/plot.py"
