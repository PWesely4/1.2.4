import turtle as trtl
import random as rand
wn = trtl.Screen()
painter = trtl.Turtle()


door = 1
barrier = 1
painter.speed(speed=0)
x = 1
space = 1
painter.setheading(90)
painter.pensize(4)
painter.penup()
while x < 22:
  space += 1
  if x > 4:
    door = rand.randint(40, ((space*20) - 80))
    barrier = rand.randint(40, ((space*20) - 80))
    print(door)
    painter.pendown()  
  else: print("hi")
  #draw door
  painter.forward(door)
  painter.forward(100-(door))
  painter.penup()
  painter.forward(30)
  if x > 4:
    painter.pendown()  
  else: print("hi")
  painter.forward(barrier)
  #draw barrier
  painter.left(90)
  painter.forward(59)
  painter.penup()
  painter.back(59)
  painter.right(90)
  painter.pendown()
  #draw maze
  painter.forward(space*10)
  painter.forward((space*20)-barrier)
  painter.left(90)
  x += 1

wn.mainloop()
