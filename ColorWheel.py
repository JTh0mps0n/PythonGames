import pygame
import random

def colorWheel():
    pygame.init()
    window = pygame.display.set_mode([700, 1000])
    pygame.display.set_caption("Color Wheel")


    wheel = pygame.image.load("Wheel.png")
    global wheelRect
    wheelRect = wheel.get_rect()
    wheelRect.width = 30
    wheelRect.height = 30
    wheel = pygame.transform.rotate(wheel, 45)
    wheelRect = wheel.get_rect()
    wheelRect.x = 90
    wheelRect.y = 500


    global yellow
    global cyan
    global pink
    global purple
    global colorDict
    yellow = (246, 223, 14)
    cyan = (52, 228, 244)
    pink = (252, 4, 131)
    purple = (140, 20, 252)
    background = (37, 0, 83)
    colorDict = {0:yellow, 1:cyan, 2:pink, 3:purple}


    global wheelColor
    wheelColor = yellow
    global wheelRot
    wheelRot = 0

    score = 0
    highscore = 0

    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont("Arial", 30)
    playAgain = True
    while playAgain:
        score = 0

        wheel = resetWheel(wheel, wheelRot)
        wheelRot = 0
        wheelColor = colorDict[wheelRot]

        ballColor = yellow
        ballRect = pygame.rect.Rect(350, 0, 20, 20)
        speed = 3
        acceleration = 0.0025
        alpha = 255
        keepRunning = True
        givenInput = False
        while keepRunning:
            window.fill(background)

            #update ball position
            ballRect.y += speed
            speed += acceleration

            text = myfont.render("Score: " + str(score), False, (255, 255, 255))
            window.blit(text, (530, 50))
            text = myfont.render("Highscore: " + str(highscore), False, (255, 255, 255))
            window.blit(text, (530, 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepRunning = False
                    playAgain = False
                    givenInput = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        wheel = rotateWheel(wheel, 90)
                    if event.key == pygame.K_LEFT:
                        wheel = rotateWheel(wheel, -90)

            if ballRect.y >= 550 and ballRect.y <= 625:
                if ballColor != wheelColor:
                    #print("game over, Score: {}".format(score))
                    keepRunning = False

            if ballRect.y >= 625:
                alpha = alpha - 10
                if alpha < 0:
                    alpha = 0

            if ballRect.y >= 775:
                score += 1
                ballRect.y = -50
                alpha = 255
                ballColor = colorDict[random.randint(0, 3)]


            window.blit(wheel, wheelRect)
            pygame.draw.circle(window, pygame.Color(ballColor[0], ballColor[1], ballColor[2], alpha), (ballRect.x, ballRect.y), ballRect.width)
            pygame.display.update()

            clock.tick(60)

        if score > highscore:
            highscore = score
            text = myfont.render("New High Score!", False, (255, 255, 255))
            window.blit(text, (250, 150))

        while not givenInput:

            endText = myfont.render("Game Over", False, (255, 255, 255))
            window.blit(endText, (250, 200))
            endText = myfont.render("Press SPACE to Continue", False, (255, 255, 255))
            window.blit(endText, (250, 250))
            endText = myfont.render("Press Q to Quit", False, (255, 255, 255))
            window.blit(endText, (250, 300))
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playAgain = False
                    givenInput = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        givenInput = True
                    elif event.key == pygame.K_q:
                        playAgain = False
                        givenInput = True

    pygame.quit()



def rotateWheel(wheel, angle):
    global wheelRect
    global wheelRot
    global wheelColor
    global colorDict
    wheel = pygame.transform.rotate(wheel, -angle)
    wheelRect = wheel.get_rect()
    wheelRect.x = 90
    wheelRect.y = 500
    wheelRot = (wheelRot + (angle // 90)) % 4
    wheelColor = colorDict[wheelRot]
    return wheel

def resetWheel(wheel, wheelRot):
    #print(wheelRot)
    return rotateWheel(wheel, 360 - wheelRot * 90)
