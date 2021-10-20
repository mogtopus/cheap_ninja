from balle import *

def setup():
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    liste_jeu(les_balles)
    
les_balles = []

def liste_jeu(liste):
    liste.append(Balle(Balle.XMAX/2 , 400 , 0 , -5 , 100 , 100,150,200 , 1))


def draw():
    global les_balles
    for balle in les_balles:
        balle.anime(les_balles)
