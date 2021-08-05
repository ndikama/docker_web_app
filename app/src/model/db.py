from abc import ABC

# pip install mysql-connector-python
import mysql.connector


class DB(ABC):
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='beer',
        port=3306
    )

    @staticmethod
    def connect():
        try:
            cursor = DB.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as e:
            print(e)
