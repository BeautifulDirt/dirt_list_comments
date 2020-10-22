#!/usr/bin/python3
# coding: utf-8
import cgi
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice

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

with open('../img_result.png', 'wb') as g:
    img.save(g)

with open('../key.txt', 'w') as k:
    k.write(str(key))