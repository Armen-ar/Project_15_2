import sqlite3

with sqlite3.connect("animal.db") as connection:

    cursor = connection.cursor()
    query = """
        SELECT *
        FROM cats
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
