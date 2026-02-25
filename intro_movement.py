import time, turtle, random
from utils import *
# Section 1: Setup
set_background("canvas")
s1 = create_sprite("pencil",0,-200)
s2 = create_sprite("highlighter, 0,-200")

# Section 2: define controls for s1
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)


#drawing and erasing controls for s1:
def draw():
    s1.pendown()
window.onkeypress(draw, "i")

def stop_drawing():
    s1.penup()
window.onkeypress(stop_drawing, "k")

def erase():
    s1.clear()
window.onkeypress(erase, "j")

def reset():
    s1.goto(0,0)
window.onkeypress(reset, "l")



#colors:
def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "1")

def orange_pen():
    s1.color("blue")
window.onkeypress(orange_pen, "2")

def yellow_pen():
    s1.color("blue")
window.onkeypress(yellow_pen, "3")

def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "4") 

def blue_pen():
    s1.color("blue")
window.onkeypress(blue_pen, "5")

def purple_pen():
    s1.color("blue")
window.onkeypress(purple_pen, "6")


window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

#define controls for s2:
def move_up():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)

#drawing and erasing controls for s2:
def draw():
    s2.pendown()
window.onkeypress(draw, "7")

def stop_drawing():
    s2.penup()
window.onkeypress(stop_drawing, "8")

def erase():
    s2.clear()
window.onkeypress(erase, "9")

def reset():
    s2.goto(0,0)
window.onkeypress(reset, "0")


#colors for s2:
def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "z")

def orange_pen():
    s1.color("blue")
window.onkeypress(orange_pen, "x")

def yellow_pen():
    s1.color("blue")
window.onkeypress(yellow_pen, "c")

def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "v") 

def blue_pen():
    s1.color("blue")
window.onkeypress(blue_pen, "b")

def purple_pen():
    s1.color("blue")
window.onkeypress(purple_pen, "n")


window.onkeypress(move_up, "t")
window.onkeypress(move_down, "g")
window.onkeypress(move_left, "f")
window.onkeypress(move_right, "h")

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()