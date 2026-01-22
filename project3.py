import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 200
x2 = -300
y2 = 100
x3 = -300
y3 = -75
x4 = -300
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("cartoonfield")
t1 = create_sprite("dogrunning1",x1,y1)
t2 = create_sprite("dogrunning2",x2,y2)
t3 = create_sprite("dogrunning3",x3,y3)
t4 = create_sprite("dogrunning4",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(49):
# dog 1 will most likely win but sometimes the number is low so will not always win
    x1 += random.randint(5,20)
# dog 2 will always loose
    x2 += 10
# dog 3 will sometimes win depending on the random speed set for dog 1 and 4
    x3 += 12
# dog 4 will sometimes win but not likely
    x4 += random.randint(1,20)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# #TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
# this makes a message appear on the screen and terminal that player 1 wins in blue text:
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
    message1 = create_sprite("hiddengrass",-200,0)
    message1.color("blue")
    message1.write("Player 1 wins!",font = ("Arial", 40, "normal"))
    message1.hideturtle()
# this makes a message appear on the screen and terminal that player 2 wins in red text:
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
    message1 = create_sprite("hiddengrass",-200,0)
    message1.color("red")
    message1.write("Player 2 wins!",font = ("Arial", 40, "normal"))
    message1.hideturtle()
# this makes a message appear on the screen and terminal that player 3 wins in yellow text:
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
    message1 = create_sprite("hiddengrass",-200,0)
    message1.color("yellow")
    message1.write("Player 3 wins!",font = ("Arial", 40, "normal"))
    message1.hideturtle()
# this makes a message appear on the screen and terminal that player 4 wins in purple text:
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    print("player 4 wins!")
    message1 = create_sprite("hiddengrass",-200,0)
    message1.color("purple")
    message1.write("Player 4 wins!",font = ("Arial", 40, "normal"))
    message1.hideturtle()

turtle.exitonclick()