# UND-PostGres-DM
Udacity Nano Degree Post Gres Datamodelling

This README file includes the project description, the database design, ETL process description and the Project Repository files.

**Project description:** {{This is well written, and gives a gist of what to be expected.}}

A startup called **Sparkify** wants to analyze the data they've been collecting on songs and user activity from their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
To acheive this objective we will create a database schema and ETL pipeline to help with  this analysis. 

**Database design:**  {{Describe the schema, you should lay down what are the tables (fact and dimension tables) clearly. Mention, the purpose for each of them.}}



**ETL Process:** This section describes the processing of the logs and creating different tables so that analytical queries can be run on them. It also describes, which directories has what kind of data and how are you extracting and transforming it.


**Project Repository files:** {{This section describes what files are for which purpose in the project}}


**How To Run the Project:** This describes the steps to run the project




The project build will be in two stages in steps 1 and 2 below. The third point below is just a utility of answering analytical questions / queries once the star schema is populated with data from the json files.

1. Model and build the star schema in Postgres database.

2. Build an ETL pipeline to load the data in the json files to the schema that was created in step 1.

3. Run analytical queries against the database that has been populated with user and song data and metadata.


In order to have a graduated build and unit test the  model and etl build programs two jupyter notebooks test.ipynb and etl.ipynb are provided with a build and execute framework with python code that needs to be detailed.

This helps to test the program logic with a few records which later can include managing the full list of files.


The create_tables.py is the master program containing the funtion main and has the program logic to create the tables using DDL and Query definitions sql_queries.py file

The etl.py file contains the program logic and python code to execute the data pipeline that transfers data in json files to the star schema created earlier.

SQL queries can then be created and tested in the file test.ipynb for analytical queries that need to be answered.
