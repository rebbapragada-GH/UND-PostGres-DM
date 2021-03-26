'''
##########################################################################################################
* Import all important libraries for handling files (os), dataframes(pandas),copy files (psycopg2) etc                           
* Import functions from sql_queries.py file. This dependency is quite important.                  
* Author: Ramakrishna Rebbapragada :: File Name: etl.py
* Creation Date: Mar-15-2021
* Updation Date: Mar-26-2021:  Added docstring comments after project review 
##########################################################################################################
'''
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

## PROCESS SONG FILES 
def process_song_file(cur, filepath):
 
    ''' 
    This function does the following:
    *   1) processes the song data JSON files. 
    *   2) reads the JSON files into a pandas dataframe. 
    *   3) inserts data into song_table and artist_table for the specified fields.
    '''   

    # open song file
    df = pd.read_json(filepath, lines=True)
    # insert song data into song table 
    # just the first record from the songs table 
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]    
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    # inserts the first record from the artists dimension table 
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0]
    cur.execute(artist_table_insert, artist_data)

## PROCESS LOG FILES 
    
def process_log_file(cur, filepath):
    '''
    This function does the following: 
    1) Process the log data JSON files. 
    2) Read the JSON files into a pandas dataframe.
    3) Converts the timestamp column data type to datetime. 
    4) enters data into the time_table, user_table and songplay_table with the filtered field.
    
    Desccription of Arguments Passed:
       -1-> cur:      Database cursor. 
       -2-> filepath: Data files location
    '''
    # open log file and assign it to a dataframe
    df = pd.read_json(filepath, lines=True)
    # filter songs dataframe by NextSong 
    df = df[(df['page'] == 'NextSong')]
    # convert timestamp column to datetime type
    t = pd.to_datetime(df['ts'], unit='ms')
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    # insert  records into time table
    # split time into its subcomponents
    time_data = pd.concat([df['ts'], t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.weekday], axis = 1)
    #assign column labels
    column_labels = ('timestamp', 'hour', 'day', 'week of year', 'month', 'year', 'weekday')
    time_df = pd.DataFrame(data = time_data.values, columns = column_labels)
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))
    # load data to user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    # insert records into user table
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)
    # insert  records into songplay table
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables to filter the query
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        # insert songplay record
        songplay_data = (index, row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)

                 
def process_data(cur, conn, filepath, func):
    '''
    * The function processes all data files within the specified location (argument: filepath). 
    * It applies an iterative loop to load each data file in a loop  in json format into the sparkifydb database
    '''    
    # get all files matching .json extension from the directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    # get total number of files found
    num_files = len(all_files)
    #print to the output file found
    print('{} files found in {}'.format(num_files, filepath))
    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))
        
        
def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    # process all song data first
    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    # proess all log data next
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)
    #close the connection
    conn.close()
if __name__ == "__main__":
    main()