from math import pi as PI
from random import randint as random
class Balle:

    XMAX = 750
    YMAX = 500
    gamestate = 1
    def __init__(self , type , option = None , x = None , y = None):
        #########################################
        #GROS CHANGEMENT SI VOUS TROUVEZ CA MOCHE DITES MOI ET ON LE RETIRE
        #l objectif est de simplifier la creation des balles
        ###########################################

        self.type = type
        if self.type == 'gravity': #gravity
            self.diam = 80
            self.ray = self.diam/2
            if option == 'right':
                self.x = random(Balle.XMAX/ 2 , Balle.XMAX)
                self.vx = -3
            else:
                self.x = random(0 , Balle.XMAX/ 2)
                self.vx = 3
            self.y = Balle.YMAX
            self.vy = random(-6 , -4)
            self.r , self.g , self.b = 50 , 50, 200

        elif self.type == 'sinus': #sinus
            self.diam = 50
            self.y = Balle.YMAX / 2
            self.z = 0
            self.ray = self.diam/2
            self.vy = 0
            if option == 'right':
                self.x = Balle.XMAX
                self.vx = -3
            else:
                self.x = 0
                self.vx = 3
            self.r , self.g , self.b = 200 , 50, 200
        
        elif self.type == 'bouncy': # bouncy
            self.x = x
            self.y = y
            self.diam = 60
            self.ray = self.diam/2
            if option == "top_r":
                self.vx = 5
                self.vy = -5
            elif option == 'top_l':
                self.vx = -5
                self.vy = -5
            elif option == 'bottom_r':
                self.vx = 5
                self.vy = 5
            else : 
                self.vx = -5
                self.vy = 5
            self.r , self.g , self.b = 255 , 255 , 255

        elif self.type == 'tournante': #tournante
            self.diam = 100
            self.ray = self.diam/2
            self.cycle = 0
            self.x = random(0 + self.diam*2 , Balle.XMAX - self.diam*2)
            self.y = Balle.YMAX
            self.vx = 0
            self.vy = -5
            self.r , self.g , self.b = 0 , 0, 255
            self.z = 0

        else: #piegee
            self.x = random(0 , Balle.XMAX)
            self.y = random(0 , Balle.YMAX)
            self.vx = random(-10 , 10)
            self.vy = random(-10 , 10)
            self.diam = random(70 , 100)
            self.ray = self.diam/2
            self.r , self.g , self.b = 255 , 0 , 0
            self.cycle = 0


    def gravity(self):
        self.deplace()
        self.vy = self.vy + 0.07

        if self.x - self.ray <= 0:
            self.x = 0 + self.ray
            self.vx = -self.vx #-0.2
        elif Balle.XMAX <= self.x + self.ray:
            self.x = Balle.XMAX - self.ray
            self.vx = -self.vx #+ 0.2


        if Balle.YMAX <= self.y + self.ray:
            self.y = Balle.YMAX -self.ray
            self.vy = -self.vy #+0.2
        self.affiche()
        

    def sinus(self):
        self.deplace()
        if self.z >= 2*PI:
            self.z=0
        self.vy=sin(self.z) * 5
        self.z = self.z+ PI/10

        if self.x -self.ray < 0:
            self.x = 0 + self.ray
            self.vx = -self.vx
        elif Balle.XMAX < self.x + self.ray :
            self.x = Balle.XMAX - self.ray
            self.vx = -self.vx
        self.affiche()
    

    def bounce(self):
        self.deplace()
        if self.x - self.ray <= 0:
            self.x = 0 + self.ray
            self.vx = -self.vx
        elif Balle.XMAX <= self.x + self.ray:
            self.x = Balle.XMAX - self.ray
            self.vx = -self.vx

        if self.y - self.ray <= 0 :
            self.y = 0 + self.ray
            self.vy = -self.vy
        elif Balle.YMAX <= self.y + self.ray:
            self.y = Balle.YMAX -self.ray
            self.vy = -self.vy
        self.affiche()


    

    def tournant(self):
        def helice(x = 0 , y = 0):
            fill(250,100,100)
            ellipse(x , y , self.diam , self.diam/5)

        def helice_tournante():
            pushMatrix()
            translate(self.x , self.y)
            rotate(PI* self.cycle/2000 * self.z)
            helice()
            popMatrix()
            self.z = self.z+1         

        if self.y > Balle.YMAX/2:
            self.deplace()
            self.affiche()
            helice(self.x , self.y)
        else : 
            self.affiche()
            helice_tournante()

        
    def piegee(self):
        def dessine():
            noStroke()
            fill(self.r , self.g , self.b)
            pushMatrix()
            translate(self.x , self.y)
            rotate(self.cycle)
            for i in range(16):
                rotate(PI/8 + self.cycle/10)
                triangle(0 - self.ray , 0  , 0 + self.ray , 0 , 0 , self.ray)
            popMatrix()
            stroke(0)
            self.cycle = self.cycle + PI/300
            if self.cycle >= 4*PI:
                self.cycle = 0

        self.deplace()
        if self.x - self.ray <= 0:
            self.x = 0 + self.ray
            self.vx = -self.vx
        elif Balle.XMAX <= self.x + self.ray:
            self.x = Balle.XMAX - self.ray
            self.vx = -self.vx

        if self.y - self.ray <= 0 :
            self.y = 0 + self.ray
            self.vy = -self.vy
        elif Balle.YMAX <= self.y + self.ray:
            self.y = Balle.YMAX -self.ray
            self.vy = -self.vy
        dessine()

    def anime(self , liste , click , mx , my):
        if self.type == 'gravity':
            self.gravity()
        elif self.type == 'sinus':
            self.sinus()
        elif self.type == 'bouncy':
            self.bounce()
        elif self.type == 'tournante':
            self.tournant()
        else : self. piegee()

        if click and self.est_dans(mx , my):
            if self.type != 'tournante':
                self.dead(liste)
            else:
                self.cycle = self.cycle + 150
                if self.cycle > 600:
                    self.dead(liste)

    def dead(self , liste):
        liste.remove(self)
        if self.type == 'tournante':
            liste.append(Balle('bouncy' , 'top_r' , self.x + self.ray , self.y - self. ray))
            liste.append(Balle('bouncy' , 'top_l' , self.x -self.ray , self.y - self.ray))
            liste.append(Balle('bouncy' , 'bottom_r' , self.x + self.ray , self.y + self.ray))
            liste.append(Balle('bouncy' , 'bottom_l' , self.x -self.ray , self.y +self.ray))
        elif self.type == 'piegee':
            Balle.gamestate = 0



    def est_dans(self , x , y):
        def distance(x2 , y2):
            return ((x2 - self.x)**2 + (y2 - self.y)**2)**0.5
        return distance(x ,  y) <= self.ray


    def deplace(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy     


    def affiche(self):
        noStroke()  
        fill(self.r , self.g , self.b)
        circle(self.x , self.y , self.diam)
