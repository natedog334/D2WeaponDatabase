from typing import Tuple
import psycopg2
import os
from enum import Enum

class SortBy(Enum):
    NAME = 0
    ARTIST = 1
    GENRE = 2
    RELEASE_YEAR = 3


# noinspection PyMethodMayBeStatic
class DatabaseService(object):

    def sample_query(self, name):
        recipt = ("""
            SELECT name FROM  MPH_TEST 
            WHERE name ='{name}'
        """.format(name=name))
        print(recipt)
        return exec_fetchall(recipt)

def exec_fetchone(query: str):
    try:
        params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': os.getenv('PASSWORD'),
            'host': 'localhost'
        }

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        row = cur.fetchone()
        conn.close()
        return row
    except Exception as e:
        print(f"Connection failed: {e}")
        return False


def exec_fetchall(query: str):
    try:
        params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': os.getenv('PASSWORD'),
            'host': 'localhost'
        }

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Connection failed: {e}")
    return False


def exec_status(query: str) -> bool:
    try:
        params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': os.getenv('PASSWORD'),
            'host': 'localhost'
        }
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        try:
            conn.commit()
            conn.close()
            return True
        except:
            print("commit error")
            conn.close()
            return False
    except Exception as e:
        print(f"Exception: {e}")
    return False