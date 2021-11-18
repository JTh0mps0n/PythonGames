import turtle


# onGround = True
# velocity = 0

def dinosaurGame():
    print("Launching Dinosaur Game")
    global quit
    quit = False
    highScore = 0
    # window
    window = turtle.Screen()
    window.title("Dinosaur Game")
    window.bgcolor("white")
    window.setup(width=1200, height=900)
    window.tracer(0)

    # cursor
    cursor = turtle.Turtle()
    cursor.penup()
    cursor.setundobuffer(4)


    while not quit:
        global onGround
        global velocity
        global resume

        onGround = True
        velocity = 0
        gravity = 0
        accel = -.00015
        obsSpeed = -1.4
        obsAccel = -.00005
        score = 0


        window.clear()
        window.tracer(0)

        #dinosaur
        dino = turtle.Turtle()
        dino.shape("square")
        dino.color("black")
        dino.penup()
        dino.goto(-450, -90)



        #floor
        floor = turtle.Turtle()
        floor.penup()
        floor.shape("square")
        floor.color("grey")
        floor.shapesize(70)
        floor.goto(0, -800)


        #obstacles
        obstacles = []
        obs1 = turtle.Turtle()
        obs1.shapesize(5)
        obs1.shape("square")
        obs1.color("red")
        obs1.penup()
        obs1.goto(700, -50)
        obstacles.append(obs1)

        window.listen()
        window.onkeypress(jump, "space")
        window.onkey(quitGame, 'q')
        gameOver = False



        while not gameOver:
            window.update()

            #update score
            score += 1
            if(score % 100 == 0):
                #cursor.undo()
                cursor.undo()
                # cursor.setpos(400, 400)
                # cursor.write("HIGH SCORE: " + str(highScore), font=15)
                cursor.setpos(400, 380)
                cursor.write("SCORE: " + str(score), font=15)


            #move obstacles and check for collisions
            obsSpeed += obsAccel
            for i in range(len(obstacles)):
                currObs = obstacles[i]
                currObs.setx(currObs.xcor() + obsSpeed)

                if(currObs.xcor() < -1400):
                    currObs.setx(700)
                dinoSize = dino.turtlesize()
                obsSize = currObs.turtlesize()
                dinoRadius = dinoSize[0]
                obsRadius = obsSize[0]
                radii = (obsRadius + dinoRadius) * 10
                distance = currObs.distance(dino.xcor(), dino.ycor())
                #print(radii, distance)
                if(radii >= distance):
                    gameOver = True

            #gravity
            if onGround == False:
                gravity += accel
                velocity += gravity
                #print(velocity)
                dino.sety(dino.ycor() + velocity)

            #dino bounds
            if dino.ycor() < -90:
                #print("resetting")
                gravity = 0
                onGround = True
                dino.sety(-90)

        #cursor.undo()
        cursor.undo()
        if (score > highScore):
            highScore = score
            cursor.setpos(400, 360)
            cursor.write("NEW HIGH SCORE!!!", font=50)

        cursor.setpos(400, 400)
        cursor.write("HIGH SCORE: " + str(highScore), font=15)
        cursor.setpos(100, 100)
        cursor.write("PRESS SPACEBAR TO CONTINUE", font=15)
        cursor.setpos(100, 0)
        cursor.write("PRESS Q TO QUIT", font=15)
        cursor.setpos(400, 380)
        cursor.write("SCORE: " + str(score), font=15)

        resume = False
        while not resume:
            window.update()
    window.bye()




def jump():
    #print("jump!")
    global velocity
    global onGround
    global resume
    resume = True
    if(onGround):
        velocity = 2.2
        onGround = False

def quitGame():
    print("Quitting Dinosaur Game")
    global quit
    global resume
    resume = True
    quit = True