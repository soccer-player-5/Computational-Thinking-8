import turtle, math, time, random
from utils import *



set_background("space")


message_sprite = create_sprite("alien", -300,200)
message_sprite.hideturtle()

lives = 4
stars = 0

# Section 2: define controls for s1
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)


window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []

s1 = create_sprite("rocket",0,-200)

# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    message_sprite.clear()
    message_sprite.write(f"Lives: {lives}\nStar: {stars}",font=("Arial",15,"normal"))
    message_sprite.color("white")
    
    # if you die to many times you lose, and if you get a number of stars you win
    if i % 100 == 0:
        x = random.randint(-300,300)
        s2 = create_sprite("asteroid", x, 400)
        s2.setheading(270)
        sprite_list.append(s2)
        def move_down():
            x = s2.xcor() - 3
            y = s2.ycor() 
            s2.goto(x,y)
    
    

    for s2 in sprite_list:
        s2.forward(5)

        if get_distance(s1, s2) < 100:
            lives -= 1
            s2.hideturtle()
            sprite_list.remove(s2)

    if lives <= 0:
        print("You lose")
        dog = create_sprite("alien", -300,0)
        dog.hideturtle()
        dog.color("white")
        dog.write("You Lose!",font = ("Arial", 100, "normal"))
        dog.hideturtle()
        window.update()
        time.sleep(2)
        break

    if i % 100 == 0:
        x = random.randint(-300,300)
        s3 = create_sprite("star", x, 400)
        s3.setheading(270)
        sprite_list.append(s3)
    

    for s3 in sprite_list:
        s3.forward(5)

        if get_distance(s1, s3) < 100:
            stars += 1
            s3.hideturtle()
            sprite_list.remove(s3)

    if stars >= 20:
        print("You win")
        dog = create_sprite("alien", -300,0)
        dog.hideturtle()
        dog.color("white")
        dog.write("You Win!",font = ("Arial", 100, "normal"))
        dog.hideturtle()
        window.update()
        time.sleep(2)
        break
        

    



    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")