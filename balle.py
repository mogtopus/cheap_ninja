from math import pi as PI
from random import randint as random
class Balle:
    highscore = open('score.txt',"a") 
    XMAX = 750
    YMAX = 500
    gamestate = 1
    score = 0
    def __init__(self , type , option = None , x = None , y = None):
        """
        a partir du type de la balle l init assigne a l objet les attribus necessaires a son fonctionnement (vitesse postion couleur etc)
        une option est utilisee pour certains types de balle pour preciser d ou ces derniers apparaissent
        """

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
            self.vy = random(-7 , -2)
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


    def gravity(self):              #crée un effet de gravité et de lourdeur à la balle
        self.deplace()
        self.vy = self.vy + 0.07    #augmentation de la vitesse de la balle

        if self.x - self.ray <= 0:  #condition si la balle dépasse le côté droite, elle va s'arrêter de bouger puis perdre de la vitesse 
            self.x = 0 + self.ray   
            self.vx = -self.vx #-0.2
        elif Balle.XMAX <= self.x + self.ray:
            self.x = Balle.XMAX - self.ray
            self.vx = -self.vx #+ 0.2


        if Balle.YMAX <= self.y + self.ray:   #condition si la balle dépasse de la fenêtre en bas, elle va aussi s'arrêter puis perdre de la vitesse
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
        """
        gere les petites balles blanches qui rebondissent sur les murs

        si la balle touche un bord de l ecran ou sort de l ecran on la repositionne a une position valide et on inverse sa vitesse x ou y
        pour lui faire changer de direction
        """
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
        """
        balle bleue
        """
        def helice(x = 0 , y = 0):
            """
            dessine l ellipse au milieu de la balle
            """
            fill(250,100,100)
            ellipse(x , y , self.diam , self.diam/5)

        def helice_tournante():
            """
            fait tourner l helice en faisant une translation et une rotation de la matrice

            phase de deplacement puis phase de rotation
            """
            pushMatrix()
            translate(self.x , self.y)
            rotate(PI* self.cycle/2000 * self.z)
            helice()
            popMatrix()
            self.z = self.z+1         

        if self.y > Balle.YMAX/2:
            '''
            deplacemen tant que la balle n a pas atteint la destination
            '''
            self.deplace()
            self.affiche()
            helice(self.x , self.y)
        else : 
            '''
            deplacement termine on fait maintenant tourner l helice
            '''
            self.affiche()
            helice_tournante()

        
    def piegee(self):
        """
        balle rouge piegee
        """
        def dessine():
            """
            dessinee a partir de 16 triangles en rotation 
            le cycle et ajoute a chaque rotation afin de produire l effet 'organique', la modification de sa valeur change la vitesse de rotation
            ainsi que la vitesse de l effet de la balle
            """
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
        """
        meme deplacements que pour la balle qui bouncy
        """
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
        if self.type != 'piegee' and self.type != 'tournante':
            Balle.score = Balle.score + 1
            
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
        stroke(0)  
        fill(self.r , self.g , self.b)
        circle(self.x , self.y , self.diam)
