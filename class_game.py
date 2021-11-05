# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "red"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 15, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle()
spot.fillcolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)

score_writer = trtl.Turtle()
score_writer.pu()
score_writer.goto(280, 280)
score_writer.hideturtle()

counter =  trtl.Turtle()
counter.penup()
counter.goto(-280,280)
counter.pendown()
counter.hideturtle()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up!", font=font_setup)
    spot.hideturtle
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----game functions--------

colors = ["red", "blue", "black", "purple", "green"]
def change_color():
  new_color = rand.choice(colors)
  spot.fillcolor(new_color)
  spot.stamp
  
sizes = ["1", "2", "3", "4", "5"]
def change_size():
  new_size = rand.choice(sizes)
  spot.shapesize(new_size)

spot.speed(0)
def spot_clicked(x, y):
  global timer_up
  if timer_up == False:
    change_position()
    update_score()
    change_color()
    change_size()
  else:
    spot.hideturtle()
def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.penup()
  spot.goto(new_xpos,new_ypos)
  spot.pendown()

def update_score():
  global score
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write(score, font=font_setup)

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("orange")
wn.mainloop()
