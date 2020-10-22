#!/usr/bin/env python3

import cgi
import sqlite3
from json import JSONEncoder
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
with sqlite3.connect(db_path) as conn:
	cursor = conn.cursor()

receive = cgi.FieldStorage()
region = receive.getvalue("region")

cursor.execute("SELECT id, town as value FROM towns WHERE region=?", (region,))
data = cursor.fetchall()

print('Content-Type: application/json\n\n')
print(JSONEncoder().encode(data))

