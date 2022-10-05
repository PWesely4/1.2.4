import turtle as trtl
import random as rand
wn = trtl.Screen()
painter = trtl.Turtle()

door = 10
barrier = 40
painter.speed(speed=0)
x = 1
space = 1
painter.setheading(90)
painter.pensize(4)
painter.penup()
while x < 26:#qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
  wall_length = space*20
  if x > 4:
    painter.pendown()  
    # randomize location of doors and barriers in wall
    door = rand.randint(80, (wall_length - 80))
    barrier = rand.randint(80, (wall_length - 80))
  else: print("hi")
  #draw door
  painter.forward(door)
  painter.penup()
  painter.forward(25)
  if x > 4:
    painter.pendown()  
  else: print("hi")
  painter.forward(barrier)
  #draw barrier?
  painter.left(90)
  painter.forward(39)
  painter.penup()
  painter.back(39)
  painter.right(90)
  painter.pendown()
  #draw maze
  painter.forward(wall_length)
  painter.left(90)
  x += 1
  space += 1
wn.mainloop()
