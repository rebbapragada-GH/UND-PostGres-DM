###################################################################################################
# Import psycopg2 library for establishing connection with the database                           #
# Import functions from sql_queries.py file. This dependency is quite important.                  #
#                                                                                                 #
###################################################################################################
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    
    # - Create and connect to the sparkifydb 
    # - Returns the connection and cursor to sparkifydb
    
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
   
    #Drops each table one by one 
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    
    #Creates all the tables one by one  
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    
    ##- Calls the function create_database() which handles below steps
      
        #-- Drops database (if already exists) and Creates the sparkify database. 
    
        #-- Establishes a connection with the sparkify database and gets a cursor handle to it.  
    
        #-- Drops all the tables to make sure program doesnt fail when running multiple times.  
    
        #-- Creates all tables required for the star schema. 
    
        #-- Finally, closes the connection after table creation. 
   
    
    # Establish connection, create database, get a cursor / handle to the database and return it for further dropping the tables and 
    # to create the tables.
    
    cur, conn = create_database()
    
    # Drop the tables if they already eixst by passing the cursor and database connection
    
    drop_tables(cur, conn)
    
    #create star schema tables by passing the cursor and database connection
    create_tables(cur, conn)
    
    # close the database connection once the DDL is complete.

    conn.close()


if __name__ == "__main__":
    main()