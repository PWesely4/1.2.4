from shutil import move
import turtle as trtl
import random as rand
wn = trtl.Screen()
painter = trtl.Turtle()
maze_runner = trtl.Turtle()

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
    door = rand.randint(20, ((space*20) - 80))
    barrier = rand.randint(40, ((space*20) - 80))
    print(door)
    painter.pendown()  
  #draw door
  if x > 4:
    painter.forward(door)
    painter.penup()
    painter.forward(30)
    painter.pendown()  
    painter.forward(100-(door))
  else:
    painter.forward(door)
    painter.penup()
    painter.forward(30)
    painter.forward(100-(door))
  #draw barrier
  painter.forward(barrier)
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

def GoUp():
    maze_runner.setheading(90)
    maze_runner.forward(5)
def GoDown():
    maze_runner.setheading(270)
    maze_runner.forward(5)
def GoLeft():
    maze_runner.setheading(180)
    maze_runner.forward(5)
def GoRight():
    maze_runner.setheading(0)
    maze_runner.forward(5)
def move_runner():
    maze_runner.forward(5)

wn.onkeypress(GoUp,"w")
wn.onkeypress(GoDown,"s")
wn.onkeypress(GoLeft,"a")
wn.onkeypress(GoRight,"d")
wn.onkeypress(move_runner,"g")
wn.listen()

wn.mainloop()