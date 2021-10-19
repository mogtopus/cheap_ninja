from balle import *

def setup():
    size(Balle.XMAX,Balle.YMAX)
    frameRate(60)
    background(0,0,0)

test = Balle(Balle.XMAX/2 , Balle.YMAX , 0 , -10 , 100 , 100,150,200)
    
def draw():
    global test
    test.special()
