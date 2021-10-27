import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

x = -150
y = -150

num_floors = 21
floor = 0

while floor < num_floors:
  painter.penup()
  painter.goto(x, y)
  painter.pendown()
  painter.color("pink")
  y = y + 5
  rem = floor % 6
  if (rem > 2):
    painter.color("black")
  painter.stamp()
  floor = floor + 1
  painter.pendown()
  painter.forward(50)

x = -75
y = -150

num_floors = 21
floor = 0

while floor < num_floors:
  painter.penup()
  painter.goto(x, y)
  painter.color("black")
  y = y + 5
  rem = floor % 6
  if (rem > 2):
    painter.color("red")
  painter.stamp()
  floor = floor + 1

  painter.pendown()
  painter.forward(50)



x = 0
y = -150

num_floors = 21
floor = 0

while floor < num_floors:
  painter.penup()
  painter.goto(x, y)
  painter.pendown()
  painter.color("yellow")
  y = y + 5
  rem = floor % 6
  if (rem > 2):
    painter.color("black")
  painter.stamp()
  floor = floor + 1
  painter.pendown()
  painter.forward(50)


wn = trtl.Screen()
wn.mainloop()