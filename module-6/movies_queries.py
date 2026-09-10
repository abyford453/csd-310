"""CSD-310 Module 6 - Movies: Table Queries"""

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values


# Load database credentials from the Module 5 .env file
secrets = dotenv_values("../module-5/.env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "port": int(secrets["PORT"]),
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

db = None
cursor = None

try:
    # Connect to the movies database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1 - Studio records
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()

    for studio in studios:
        print("Studio ID: {}".format(studio[0]))
        print("Studio Name: {}\n".format(studio[1]))

    # Query 2 - Genre records
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()

    for genre in genres:
        print("Genre ID: {}".format(genre[0]))
        print("Genre Name: {}\n".format(genre[1]))

    # Query 3 - Movies with a runtime less than two hours
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("""
        SELECT film_name, film_runtime
        FROM film
        WHERE film_runtime < 120
    """)

    films = cursor.fetchall()

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Runtime: {}\n".format(film[1]))

    # Query 4 - Film names and directors grouped by director
    print("\n-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director
    """)

    directors = cursor.fetchall()

    for director in directors:
        print("Film Name: {}".format(director[0]))
        print("Director: {}\n".format(director[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    if cursor is not None:
        cursor.close()

    if db is not None and db.is_connected():
        db.close()
