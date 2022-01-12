#!/usr/bin/python

import pymysql

con = pymysql.connect(
    host='localhost', 
    user='root',
    password='', 
    db='buah')

try:

    with con.cursor() as cur:

        cur.execute('SELECT VERSION()')

        version = cur.fetchone()

        print(f'Database version: {version[0]}')

finally:

    con.close()