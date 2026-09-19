"""CSD-310 Module 7 - Movies: Update & Deletes"""

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


def show_films(cursor, title):
    cursor.execute("""
        SELECT film_name AS Name,
               film_director AS Director,
               genre_name AS Genre,
               studio_name AS Studio
        FROM film
        INNER JOIN genre
            ON film.genre_id = genre.genre_id
        INNER JOIN studio
            ON film.studio_id = studio.studio_id
    """)

    films = cursor.fetchall()

    print("\n-- {} --".format(title))

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name: {}".format(film[2]))
        print("Studio Name: {}\n".format(film[3]))


db = None
cursor = None

try:
    # Connect to the movies database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Display current films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film
    cursor.execute("""
        INSERT INTO film(
            film_name,
            film_releaseDate,
            film_runtime,
            film_director,
            studio_id,
            genre_id
        )
        VALUES(
            'The Martian',
            '2015',
            144,
            'Ridley Scott',
            (SELECT studio_id
             FROM studio
             WHERE studio_name = '20th Century Fox'),
            (SELECT genre_id
             FROM genre
             WHERE genre_name = 'SciFi')
        )
    """)

    db.commit()

    # Display films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien to Horror
    cursor.execute("""
        UPDATE film
        SET genre_id = (
            SELECT genre_id
            FROM genre
            WHERE genre_name = 'Horror'
        )
        WHERE film_name = 'Alien'
    """)

    db.commit()

    # Display films after update
    show_films(
        cursor,
        "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror"
    )

    # Delete Gladiator
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)

    db.commit()

    # Display films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


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