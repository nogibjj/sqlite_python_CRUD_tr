"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
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
    conn = sqlite3.connect('alcoholDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS alcoholDB")
    c.execute("""
              CREATE TABLE GroceryDB (
                    id PRIMARY KEY AUTOINCREMENT,
                    country TEXT, 
                    beer_sevrings INTEGER,
                    spirit_servings INTEGER,
                    wine_servings INTEGER,
                    total_pur_alcohol
                  )
              """)
    #insert
    c.executemany("""
                  INSERT INTO alcoholDB (
                        country, 
                        beer_sevrings,
                        spirit_servings,
                        wine_servings,
                        total_pur_alcohol
                      ) 
                      VALUES (?, ?, ?, ?, ?)
                  """, 
                  payload)
    conn.commit()
    conn.close()
    return "alcoholDB.db"

