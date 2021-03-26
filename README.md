# UND-PostGres-DM
                                                 ** Udacity Nano Degree Postgres Datamodelling Project**


**Project description:** 

A startup called **Sparkify** wants to analyze the data they've been collecting on songs and user activity from their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
To acheive this objective we will create a database schema and ETL pipeline that populates the schema with the data to help with  this analysis. 

**Database design:**  {{Describe the schema, you should lay down what are the tables (fact and dimension tables) clearly. Mention, the purpose for each of them.}}

The database schema consists of the following **Fact Table**

   **SONGPLAYS** - stores records in log data associated with song plays i.e. records with page NextSong having the following column definitions
  
               songplay_id serial PRIMARY KEY
               start_time timestamp NOT NULL REFERENCES **time**(start_time)
               user_id text NOT NULL REFERENCES **users**(user_id)
               level varchar
               song_id text REFERENCES **songs**(song_id)
               artist_id text REFERENCES **artists**(artist_id)
               session_id text
               location varchar
               user_agent varchar

The database schema consists of the following **Dimension Tables**

**USERS**  - stores users in the app that can access the songs and having the following column definitions:
  
               user_id text PRIMARY KEY
               first_name varchar
               last_name varchar
               gender varchar
               level varchar 

**SONGS**  -stores  songs in music database and having the following column definitions:

               song_id text PRIMARY KEY
               title varchar
               artist_id text
               year int
               duration numeric

**ARTISTS** - storing artists in music database containing the following column definitions:
               artist_id text PRIMARY KEY
               name varchar NOT NULL
               location varchar
               latitude float
               longitude float

**TIME** - storing timestamps of records in songplays broken down into specific time units like weekday, year, month, week, hour, day, time etc, containing the following column definitions:
               start_time timestamp PRIMARY KEY
               hour int
               day int
               week int
               month int
               year int
               weekday varchar


The following **ERD Diagram** explains the star schema relationships between the Fact and Dimension tables.

![ER-Diagram](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/33760/1616254201/Song_ERD.png)

**ETL Process:** This section describes the processing of the logs and creating different tables so that analytical queries can be run on them. It also describes, which directories has what kind of data and how are you extracting and transforming it.



**Project Repository files:** {{This section describes what files are for which purpose in the project}}


**How To Run the Project:** {{This describes the steps to run the project}}




The project build will be in two stages in steps 1 and 2 below. The third point below is just a utility of answering analytical questions / queries once the star schema is populated with data from the json files.

1. Model and build the star schema in Postgres database.

2. Build an ETL pipeline to load the data in the json files to the schema that was created in step 1.

3. Run analytical queries against the database that has been populated with user and song data and metadata.


In order to have a graduated build and unit test the  model and etl build programs two jupyter notebooks test.ipynb and etl.ipynb are provided with a build and execute framework with python code that needs to be detailed.

This helps to test the program logic with a few records which later can include managing the full list of files.


The create_tables.py is the master program containing the funtion main and has the program logic to create the tables using DDL and Query definitions sql_queries.py file

The etl.py file contains the program logic and python code to execute the data pipeline that transfers data in json files to the star schema created earlier.

SQL queries can then be created and tested in the file test.ipynb for analytical queries that need to be answered.
