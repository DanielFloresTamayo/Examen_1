# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:21:03 2017

@author: 22B
"""

from turtle import*
import time
import turtle

t = turtle.Pen()

turtle.setup(640,480)
wn=turtle.Screen()
wn.bgcolor("red")


wn.title("Estrella de Puntas")
a=int(input("ingrese un numero de lados:"))
print(a)
for x in range (1,6):
    t.pencolor("black")
    t.pensize(4)
    t.forward(100)
    an=90/a
    ang=90 - an
    t.left(ang)
turtle.getscreen()._root.mainloop()
exit()


       

