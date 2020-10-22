#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import html
import sqlite3
import os.path

form = cgi.FieldStorage()
ID = form.getvalue('ID')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
cursor.execute("DELETE FROM comments where id=?",(ID,))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Удалить комментарий</title>
        </head>
        <body>""")

print("<p>Комментарий удален</p>")
print("<form action='/cgi-bin/view.py'><button>Просмотреть все комментарии</button></form>")
print("""</body>
        </html>""")

con.commit()
con.close()

