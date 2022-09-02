from lib2to3.pgen2.token import RIGHTSHIFT
from turtle import *

#we want to paint a house

#step 1: draw a squar
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(150, 150)
pendown()

width(5)
color("black")
left(120)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

penup()
goto(175, 195)
pendown()

forward(50)

penup()
goto(195, 175)
pendown()

right(90)
forward(50)

penup()
goto(50, 200)
pendown()

forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

penup()
goto(50, 175)
pendown()

left(90)
forward(50)

penup()
goto(25, 195)
pendown()

left(90)
forward(50)

exitonclick()
