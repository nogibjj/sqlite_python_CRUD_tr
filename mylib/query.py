"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def create_record(
    country, beer_sevrings, spirit_servings, wine_servings, total_pure_alcohol
):
    """create example query"""
    conn = sqlite3.connect("alcoholDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO alcoholDB 
        (country, beer_sevrings, spirit_servings, wine_servings, total_pure_alcohol) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (country, beer_sevrings, spirit_servings, wine_servings, total_pure_alcohol),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""INSERT INTO alcoholDB VALUES (
                {country}, 
                {beer_sevrings},
                {spirit_servings},
                {wine_servings},
                {total_pure_alcohol});"""
    )


def read_data():
    """read data"""
    conn = sqlite3.connect("alcoholDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM alcoholDB")
    data = c.fetchall()
    log_query("SELECT * FROM alcoholDB;")
    return data


def update_record(
            record_id,
            country, 
            beer_sevrings,
            spirit_servings,
            wine_servings,
            total_pure_alcohol
):
    """update example query"""
    conn = sqlite3.connect("alcoholDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE alcoholDB 
        SET country=?, 
        beer_sevrings=?, 
        spirit_servings=?, 
        wine_servings=?, 
        total_pure_alcohol=?
        WHERE id=?
        """,
        (
            country, 
            beer_sevrings,
            spirit_servings,
            wine_servings,
            total_pure_alcohol,
            record_id
        ),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""UPDATE alcoholDB SET 
        country={country}, 
        beer_sevringst=
        {beer_sevrings},
        spirit_servings={spirit_servings}, 
        wine_servings={wine_servings}, 
        total_pure_alcohol={total_pure_alcohol},
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("alcoholDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM alcoholDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    log_query(f"DELETE FROM alcoholDB WHERE id={record_id};")
