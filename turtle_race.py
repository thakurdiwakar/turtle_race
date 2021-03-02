import turtle
from random import *
from turtle import *

penup()
goto(-140,140) #positioning the pen

for sp in range(15): #loop for creating the lines labelled with numbers
  speed(10)
 #setting the speed
  write(sp)
 #writing the int
  right(90)
 #setting right at 90 degrees
  forward(10)
 #forward at 10 units
  pendown()
 #ready to draw
  forward(150)
 #forward at 150 units
  penup()
 #not ready to draw
  backward(160)
 #back at 160 units
  left(90)
 #left set at 90 degrees
  forward(20)
 #forward at 20 units


kaif = Turtle() #inheriting the turtle
kaif.color('yellow') #setting the color to green for the first turtle
kaif.shape('turtle') #setting the shape to "turtle"
kaif.penup() #not ready to draw
kaif.goto(-160,100) #positioning the turtle
kaif.pendown() #ready todraw


hrithik = Turtle() #inheriting another turtle
hrithik.color('black') #setting the color og the turtle to red
hrithik.shape('turtle') #declaring the shape of the turtle to "turtle"
hrithik.penup() #not ready to dra
hrithik.goto(-160,80) #positioning
hrithik.pendown() #ready to draw

diwVar = Turtle() #inheriting the last turtle
diwVar.color('blue') #setting the color of the turtle as "blue"
diwVar.shape('turtle') #declaring the shape of the turtle
diwVar.penup() #not ready to draw
diwVar.goto(-160,60) #positioning
diwVar.pendown() #ready

for turn in range(100): #loop for the racew
  kaif.forward(randint(1,5)) #setting the speed randomly with the "random" module
  hrithik.forward(randint(1,5)) #setting the speed randomly with the "random" module
  diwVar.forward(randint(1,5)) #setting the speed randomly with the "random" module

turtle.done()
