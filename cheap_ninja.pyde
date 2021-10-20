from balle import *
from menu import *

def setup():
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    liste_jeu(les_balles)
    
les_balles = []

def liste_jeu(liste):
<<<<<<< HEAD
    liste.append(Balle(Balle.XMAX/2 , 400 , 0 , -4 , 200 , 100,150,200 , 4))
=======
    liste.append(Balle(Balle.XMAX/2 , 400 , 0 , -5 , 100 , 100,150,200 , 1))
    liste.append(Balle(Balle.XMAX/2 , 200 , 0 , 0 , 100 , 100,150,200 ,2 ))

>>>>>>> c328b2d0961de280119da253a78f34612b4194d6

mouse = False
def mouse():
    global temp_mouse
    if mousePressed:
        if temp_mouse == True:
            return False
        else:
            temp_mouse = True
            return True
    else:
        temp_mouse = False
        return False
    
def draw():
    global les_balles , temp_mouse
    for balle in les_balles:
        balle.anime(les_balles , mouse() , mouseX , mouseY)
        
def mousePressed():
    global mouse
    
