from balle import *

def setup():
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)
    noStroke()
test = Balle(250,250 , 5,5 , 20 , 100,150,200)
    
def draw():
    global test
    test.bounce()
