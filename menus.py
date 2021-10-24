from balle import *
import os
def gameover():
    background(255,0,0)
    textAlign(CENTER, CENTER)
    textSize(30)
    fill(0)
    text('GAME OVER' , Balle.XMAX/2 , 20)
    if button('menu' ,Balle.XMAX/2 , Balle.YMAX/2 , 100 , 50 , 255 , 255 , 255):
        Balle.gamestate = 1
    if button('exit' , Balle.XMAX/2 , Balle.YMAX/2 + 100 , 100 , 50 , 255 , 255 , 255):
        exit()
      
def regles():
    a = open('regles.txt')
    background(0)
    textAlign(LEFT, TOP)
    textSize(20)
    fill(255)
    text(a.read() , 0 , 0)
    
def victoire():
    background(0,200,100)
    print('caca')
    textAlign(CENTER, TOP)
    textSize(20)
    fill(255)
    if Balle.score > int(Balle.highscore.read()):
        Balle.highscore.write(Balle.score)
    Balle.highscore.close()
        
    text("bravo vous avez reussi ce niveau" , Balle.XMAX/2 , 0)
    if button('menu' ,Balle.XMAX/2 , Balle.YMAX/2 , 100 , 50 , 255 , 255 , 255):
        Balle.gamestate = 1
    if button('exit' , Balle.XMAX/2 , Balle.YMAX/2 + 100 , 100 , 50 , 255 , 255 , 255):
        exit()
      
def button(texte , x , y , size_x , size_y , r , g , b):
    fill(r , g , b)
    noStroke()
    if x - size_x/2 < mouseX and mouseX < x + size_x/2:
        if y - size_y/2 < mouseY and mouseY < y + size_y/2:
            stroke(0)
            if mousePressed:
                return True
    rect(x - size_x/2 , y -size_y/2 , size_x , size_y)
    textAlign(CENTER, CENTER)
    textSize(10)
    fill(0)
    text(texte , x , y)

def menu():
    background(0,0,0)
    if button("Jouer au jeu",275,200,200,100,255,255,255):
        alle.gamestate = 1
