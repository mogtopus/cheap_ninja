from balle import *
from menu import *
import time

def setup():
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    liste_jeu(les_balles)
    
les_balles = []

def liste_jeu(liste):
    liste.append(Balle(Balle.XMAX/2 , 400 , 0 , -4 , 100 , 100,150,200 , 4 , 1))
    liste.append(Balle(Balle.XMAX/2 , 400 , 0 , -5 , 100 , 100,150,200 , 1 , 1))
    liste.append(Balle(Balle.XMAX/2 , 200 , 0 , 0 , 100 , 100,150,200 ,2 , 1))



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
        print(mouse)
        balle.anime(les_balles, mouse , mouseX , mouseY)
        print(mouse)
