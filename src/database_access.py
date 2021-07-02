import mysql.connector
from mysql.connector import MySQLConnection, errors
from mysql.connector.cursor import MySQLCursorDict, MySQLCursor
import os

def _get_mysql_connection() -> MySQLConnection:
    """ Reads the environment variables to long into the database and returns the db connection 
    """
    DB_USER: str = os.environ.get('DB_USER')
    DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
    DB_DATABASE: str = os.environ.get('DB_DATABASE')
    DB_HOST: str = os.environ.get('DB_HOST')
    connection: MySQLConnection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    return connection

_connection: MySQLConnection = _get_mysql_connection()

def get_highest_scores(count=10):
    """ Returns an array of the highest high score rows
    """
    cursor: MySQLCursorDict = _connection.cursor(dictionary=True)

    query = """
        SELECT initials, score FROM high_score
        ORDER BY score DESC
        LIMIT %(count)s
    """
    params = {
        "count": count,
    }

    cursor.execute(query, params=params)
    result_set_list = cursor.fetchall()

    cursor.close()
    return result_set_list

def insert_high_score(score: int, initials: str) -> bool:
    """ Inserts a score into the database, returns if row(s) were affected
    """
    cursor: MySQLCursor = _connection.cursor()
    
    query = """
        INSERT INTO high_score
        (score, initials)
        VALUES
        (%(score)s, %(initials)s)
    """
    params = {
        "score": score,
        "initials": initials,
    }

    affected_row_count = 0
    
    try:
        cursor.execute(query, params=params)
        affected_row_count = cursor.rowcount
    except errors.Error as e:
        print(e, flush=True)
    
    cursor.close()

    return affected_row_count > 0


if __name__ == '__main__':
    get_highest_scores()
    _connection.close()