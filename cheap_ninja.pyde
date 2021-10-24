from menus import *
from balle import *
from salves import *
def setup():
    global les_balles
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    init(les_balles , niv_1)
timer = 0
les_balles = []
gamestate = 0
mouse = False
precedent = False

def update_souris():
    global mouse , precedent
    if mousePressed:
        if precedent == False:
            precedent = True
            mouse = True
        else:
            mouse = False   
    else:
        precedent = False
        mouse = False

def draw():
    global gamestate , les_balles , precedent , timer , niveau
    update_liste(les_balles)
    ajoute_balles(les_balles)

    update_souris()
    if Balle.gamestate == 0:
        #menu()
        gameover()       
        
    elif Balle.gamestate == 1:
        background(0,0,0)    
        for balle in les_balles:
            
            balle.anime(les_balles, mouse , mouseX , mouseY)
    
    elif Balle.gamestate == 2:
        gameover()
         
    elif Balle.gamestate == 3:
        regles()
    elif Balle.gamestate == 4:
        victoire()
    timer = timer + 1
