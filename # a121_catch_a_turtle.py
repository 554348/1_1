# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
spot = trtl.Turtle()

#-----game configuration-----
spot_color = "red"

#-----initialize turtle-----
spot.speed(0)
spot.fillcolor(spot_color)
spot.begin_fill()
spot.circle(20)
spot.end_fill()


def change_position():
  new_xpos = rand.randint(1, 50)
  new_ypos = rand.randint(1, 50)
  spot.setposition(new_xpos, new_ypos)

def spot_clicked(x,y):
  print(change_position)



#-----game functions--------
spot.onclick(spot_clicked)
#-----events----------------
wn = trtl.Screen()
wn.mainloop()