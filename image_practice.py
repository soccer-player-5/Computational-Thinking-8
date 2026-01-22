# Section 1 - Your code
from utils import *
set_background("field")


s2 = create_sprite("cavalier", -100, -100)
s2 = create_sprite("golden", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("blue")
message1.write("Dogs at a park",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()