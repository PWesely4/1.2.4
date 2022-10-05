import turtle as trtl
wn = trtl.Screen()
painter = trtl.Turtle()


painter.speed(speed=0)
x = 1
space = 1
painter.setheading(90)
painter.pensize(4)
painter.penup()
while x < 26:
  if x > 4:
    painter.pendown()  
  else: print("hi")
  #draw door
  painter.forward(10)
  painter.penup()
  painter.forward(25)
  if x > 4:
    painter.pendown()  
  else: print("hi")
  painter.forward(40)
  #draw barrier
  painter.left(90)
  painter.forward(39)
  painter.penup()
  painter.back(39)
  painter.right(90)
  painter.pendown()
  #draw maze
  painter.forward(space*20)
  painter.left(90)
  x += 1
  space += 1
wn.mainloop()
