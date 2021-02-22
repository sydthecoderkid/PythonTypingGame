import pygame
import GameMain
import random
from pygame.locals import *

global font

mainGame = GameMain


def chooseWord():
    words= ["CAT", "DOG", "ANIMAL", "ELEPHANT", "JUMP", "RODEO", "MAGNIFY", "ALLIGATOR", "ACCOLADES", "CELEBRATION", "GYMNASTICS", "UNIVERSITY"
            "LAUDED", "ACHIEVEMENTS", "BOBSLED", "BARBORUS", "STARSTRUCK", "IPHONE", "TATTOO", "HEADPHONES", "EARBUDS", "FALLOUT", "FRONTIER", "OVERTLY", "PSUEDO", "FLAGRANT"]

    return words[random.randint(0, len(words)-1)]



