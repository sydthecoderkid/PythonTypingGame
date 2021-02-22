import pygame
import GameClass
from pygame.locals import *

GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()


thisfont = pygame.font.Font('freesansbold.ttf', 30)


global textchanged

global screen


textchanged = False

def mainFunc():
    pygame.init()
    global textchanged
    global screen
    textchanged = False
    size = width, height = 800, 500
    FMX = 55 #First message X value
    FMY = 200 #First message Y value
    screen = pygame.display.set_mode(size) #Sets size of screen.

     

    FirstMessage = thisfont.render("Hello! Welcome to my typing game.", True, RED) #First two displayed messages.
    SecondMessage = thisfont.render("Click anywhere to continue!", True, RED)
    Word = thisfont.render("", True, RED) #Init as empty- is the word that will be displayed on screen.
    Message = thisfont.render("", True, RED)  # Init as empty- is the word that will be displayed on screen.
    ClickForNext = thisfont.render("", True, RED)  # Init as empty- is the word that will be displayed on screen.


    background = BLACK #Sets the background to black.
    gameStarted = False #initalizes the gameStarted variable.

    wordselected = False

    typedword = ""

    numberwrong = 0
    while True:
        for event in pygame.event.get():
            screen.fill(background)
            screen.blit(FirstMessage, (FMX, FMY))  # Aligns text for first message.
            screen.blit(SecondMessage, (55, 245))  # Aligns text for second message.
            screen.blit(Word, (295, 245)) #Aligns text for third message
            screen.blit(Message,(50, 325))
            screen.blit(ClickForNext, (200, 390))  # Aligns text for third message



            if event.type == MOUSEBUTTONDOWN and gameStarted is False:
                FirstMessage = changeText("Starting Game! Click to generate a word..")
                SecondMessage = changeText("")
                FMY = 40  # Move the first message upwards on the screen.
                gameStarted = True

            elif event.type == MOUSEBUTTONDOWN and gameStarted is True and wordselected is False:
                typedword = ""
                FirstMessage = changeText("Type it as fast as you can!")
                Message = changeText("")

                ClickForNext = changeText("")
                word = GameClass.chooseWord() #Actual word text
                Word = changeText(word) #Word display onscreen
                wordselected = True
                index = 0
                start_time = pygame.time.get_ticks()

            if event.type == KEYDOWN and wordselected is True and index <= len(word):


                if event.key != pygame.key.key_code("return"):
                    currletter = pygame.key.name(event.key)
                    typedword += currletter

                if index == len(word)-1:
                   totalTime = (pygame.time.get_ticks() - start_time) / 1000
                   celebrationtext = checkTotal(word, typedword, totalTime, numberwrong)
                   Message = changeText(celebrationtext)
                   wordselected = False
                   ClickForNext = changeText("Click to generate a new word!")


                else:
                    index += 1

            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pygame.display.update()


def changeText(text):
    surface = thisfont.render(text, True, RED) #changes the text of the surface parameter .
    global  textchanged
    textchanged = True
    return surface



def checkTotal(word, typedword, totaltime, numberwrong):
    if word == typedword.upper():
        celebrationtext = "You got it right! Done in : " + str(totaltime) + " Seconds."
    else:
        celebrationtext = "You got it wrong. You wrote: " + typedword
    return celebrationtext



