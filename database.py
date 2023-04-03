import pymysql
from pymysql.cursors import Cursor

connection = pymysql.connect(host='127.0.0.1', user='root', passwd='2003', database='syllabus_management_system')
cur = connection.cursor()
con = connection


def create_cursor():
    return connection.cursor()


def cursor_fetch_all(cursor: Cursor):
    row_headers = [x[0] for x in cursor.description]
    values = cursor.fetchall()
    data = []
    for result in values:
        data.append(dict(zip(row_headers, result)))
    return data


def find_match_query(criteria: str):
    return f'%{criteria}%'
