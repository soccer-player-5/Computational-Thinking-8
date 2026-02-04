import turtle, time, random
from utils import *

# Section 1 - setup
set_background("flowerfield")

# starting values
flower = 0
bouquet = 0
cost = 10

# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()




# this creates flowers when you press the space key

def make_flower ():
    global flower
    flower += 1
    x = random.randint (-250,250)
    y = random.randint (-250,200)
    f1 = create_sprite ("flower",x,y)
    time.sleep(0.1)
    f1.hideturtle()

window.onkeypress(make_flower, "space")
message_sprite.hideturtle()

# this creates a bouquet when the flowers are greater than the cost when you press the 'b' key

def make_bouquet():
    global bouquet, flower, cost
    if flower >= cost:
        bouquet += 1
        flower -= cost
        x = -365 + 120*bouquet
        y = -250
        cost = 2*cost
        create_sprite ("bouquet",x,y)

window.onkeypress(make_bouquet, "b")





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    if i % 50 == 0:
        if bouquet == 1:    
            flower += 1
        elif bouquet == 2:
            flower += 2
        elif bouquet == 3:
            flower += 3
        elif bouquet == 4:
            flower += 4
        elif bouquet == 5:
            flower += 5
    message_sprite.clear()
    message_sprite.write(f"Flower: {flower}\nCost: {cost}\nBouquet: {bouquet}",font=("Arial",15,"normal"))
    # TODO - put any automatic actions here

    # to show that you won the game, this makes a message appear on the screen when you get 5 bouquets
    if bouquet == 5:
        print("player 1 wins!")
        message1 = create_sprite("hiddengrass",-140,0)
        message1.color("blue")
        message1.write("You Win!",font = ("Arial", 40, "normal"))
        message1.hideturtle()

    time.sleep(0.01)
    window.update()