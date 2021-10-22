from balle import *
from menu import *
import time

def setup():
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    #liste_jeu(les_balles)
    
les_balles = [Balle(4) , Balle(5)]





mouse = False

precedent = False
b = 0

def move_mouse():
    pass

def draw():

    background(0,0,0)
    global les_balles , precedent
    if mousePressed:
        if precedent == False:
            precedent = True
            mouse = True
        else:
            mouse = False   
    else:
        precedent = False
        mouse = False

    for balle in les_balles:
        balle.anime(les_balles, mouse , mouseX , mouseY)
