from menu import *
from balle import *
from salves import *
def setup():
    global les_balles
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    init(les_balles)
timer = 0
les_balles = []
gamestate = 0
mouse = False
precedent = False


def draw():
    global gamestate , les_balles , precedent , timer
    update_liste()
    ajoute_balles(les_balles)

    if mousePressed:
        if precedent == False:
            precedent = True
            mouse = True
        else:
            mouse = False   
    else:
        precedent = False
        mouse = False
        
    if Balle.gamestate == 0:
        background(0,0,0)
        
        
        for balle in les_balles:
            balle.anime(les_balles, mouse , mouseX , mouseY)
    elif Balle.gamestate == 2:
        background(255,0,0)
    
    
    timer = timer + 1
