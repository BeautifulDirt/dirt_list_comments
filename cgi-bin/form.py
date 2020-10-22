#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import html
import sqlite3
import os.path
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice

key_captcha = ''
form = cgi.FieldStorage()
lastname = form.getvalue("lastname")
firstname = form.getvalue("firstname")
middlename = form.getvalue("middlename","")
region = form.getvalue("region","")
town = form.getvalue("selectTowns","")
phone = form.getvalue("phone","")
email = form.getvalue("email","")
textArea = form.getvalue("textArea")
captcha = form.getvalue("key_captcha")

with open('./key.txt', 'r') as k:
    key_captcha = k.read()

a = randint(1,30)
b = randint(1,20)
c = randint(1,10)
key = a+b*c
text = str(a)+'+'+str(b)+'*'+str(c)
   
img = Image.new('RGB', (200,60), 0xffffff )
draw = ImageDraw.Draw(img)
    
for i in range(40):
    draw.line( [(randint(0,200),randint(0,60)),(randint(0,200),randint(0,60))], randint(0, 0xffffff), 1)
    
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 40)
draw.text( (5,5), text, 0, font)

with open('./img_result.png', 'wb') as g:
    img.save(g)

with open('./key.txt', 'w') as p:
    p.write(str(key))

if int(key_captcha)==int(captcha):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")
    with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
    cursor.execute("INSERT INTO comments (lastname, firstname, middlename, region, town, phone, email, comment) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(lastname, firstname, middlename, region, town, phone, email, textArea))

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Добавить комментарий</title>
            </head>
            <body>""")

    print("<p>Комментарий принят</p>")
    print("<form action='/cgi-bin/view.py'><button>Просмотреть все комментарии</button></form>")
    print("""</body>
            </html>""")

    con.commit()
    con.close()
else:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Добавить комментарий</title>
            </head>
            <body>""")

    print("<p>Неправильно введен ответ на captcha!</p>")
    print("<form action='/cgi-bin/view.py'><button>Просмотреть все комментарии</button></form>")
    print("""</body>
            </html>""")

