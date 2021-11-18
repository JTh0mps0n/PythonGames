import turtle
import os


global onGround
global velocity

def dinosaurGame():
    onGround = True
    velocity = 0
    dy = -1
    print("Launching Dinosaur Game")

    #window
    window = turtle.Screen()
    window.title("Dinosaur Game")
    window.bgcolor("white")
    window.setup(width=1200, height=900)
    window.tracer(0)

    #dinosaur
    dino = turtle.Turtle()
    dino.shape("square")
    dino.color("black")
    dino.penup()
    dino.goto(-450, -90)
    print(dino.width())


    #floor
    floor = turtle.Turtle()
    floor.penup()
    floor.shape("square")
    floor.color("grey")
    floor.shapesize(70)
    floor.goto(0, -800)

    window.listen()
    window.onkeypress(jump, "space")
    gameOver = False

    while not gameOver:
        window.update()

        #gravity
        print(onGround)
        if not onGround:
            velocity -= 1
            print(velocity)
            dino.sety(dino.ycor() + velocity)

        #dino bounds
        if dino.ycor() < -100:
            onGround = True
            dino.sety(-90)
        #print(dino.pos())

def jump():
    print("jump!")
    velocity = 10
    onGround = False