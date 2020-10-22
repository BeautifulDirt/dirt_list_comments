#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import html
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
with sqlite3.connect(db_path) as con:
        cursor = con.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Ваши комментарии</title>
	    <style>
	    .data {
		font-size: 9pt;
		}
	    </style>
        </head>
        <body>""")

print("<div align='center'  style='font-size: 35pt'>Все комментарии</div><br>")
print("<form method='GET' action='../comment.html'><button>Добавить свой комментарий</button></form><br><hr>")
for row in cursor.execute("SELECT * FROM comments ORDER BY `id` DESC"):
    print("<div style='font-size: 15pt'> {}".format(row[1]))
    print(" {}".format(row[2]))
    print(" {}</div>".format(row[3]))
    print("<div class='data'>{}".format(row[6]))
    print(" {}</div>".format(row[7]))
    print("<div class='data'>{}</div>".format(row[4]))
    print("<div class='data'>{}</div>".format(row[5]))
    print("<h1>{}</h1>".format(row[8]))
    print("<form method='POST 'name='form' action='/cgi-bin/delete.py'><button value='{}' name='ID'>Удалить</button></form>".format(row[0]))
    print("<hr>")

print("""</body>
        </html>""")
con.commit()
con.close()


