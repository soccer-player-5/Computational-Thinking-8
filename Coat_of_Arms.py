# Section 1 - Your code
from utils import *
set_background("bridge_beach")

s1 = create_sprite("golden", 200, -175)
s2 = create_sprite("us_flag", 200, 200)
s3 = create_sprite("shield", 285, -75)
s4 = create_sprite("soccerball", 100, -110)

message1 = create_sprite("alien",-300,200)
message1.color("red")
message1.write("Sloane",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-310,150)
message2.color("black")
message2.write("Warrior",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()