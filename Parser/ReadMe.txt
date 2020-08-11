This part of the project consists of parsing the medline bibligraphy data.

To start parsing =>
**Run the main.py file 

Rest of the operations like downloading the pubmed data from their site and 
parsing it will be done by system.
There are three modules created based on their functionalities.
1> main.py module:
        This module is the core of the parsing program.It handles calling appropriate functions 
        from other modules to parse the data

2> parser.py module:
        This module consits of the parsing code where data is extracted from xml.gz files
        with use of Xpath like queries

3> OperationHandler.py:
        As the name suggests this module consits of every operation other than core parsing.
        It consits of download function which automatically downloads files from 
        nlm site through request object.
        It also has methods to create the files and also initialize and update the dictionaries
        used for holding author data to avoid clashing of author ids
