""" import statements """
import mysql.connector
from mysql.connector import errorcode

from dotenv import dotenv_values


# using our .env file
secrets = dotenv_values(".env")


""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "port": int(secrets["PORT"]),
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}


db = None

try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config)

    print(
        "\n  Database user {} connected to MySQL on host {} with database {}".format(
            config["user"],
            config["host"],
            config["database"]
        )
    )

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    if db is not None and db.is_connected():
        db.close()
