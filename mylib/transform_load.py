"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
# import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/alcohol.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    # print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)
    conn = sqlite3.connect('alcoholDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS alcoholDB")
    c.execute("""
              CREATE TABLE alcoholDB (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    country TEXT, 
                    beer_sevrings INTEGER,
                    spirit_servings INTEGER,
                    wine_servings INTEGER,
                    total_pure_alcohol
                  )
              """)
    #insert
    c.executemany("""
                  INSERT INTO alcoholDB (
                        country, 
                        beer_sevrings,
                        spirit_servings,
                        wine_servings,
                        total_pure_alcohol
                      ) 
                      VALUES (?, ?, ?, ?, ?)
                  """, 
                  payload)
    conn.commit()
    conn.close()
    return "alcoholDB.db"

