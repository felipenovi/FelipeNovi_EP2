# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:35:44 2015

@author: Felipe
"""

import turtle

forca = turtle.Turtle()  # Cria um objeto "desenhador"
forca.hideturtle
forca.speed(2)  # velocidade do desenho
forca.penup()       
forca.setpos(-250,0)
forca.pendown()
forca.color("yellow")
    
for i in range(1):
    forca.forward(100)
    forca.left(180)  
    forca.forward(50) 
    forca.right(90)
    forca.forward(220)
    forca.right(90)
    forca.forward(100)
    forca.right(90)
    forca.forward(30)
#final do desenho da forca
