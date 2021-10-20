from math import pi as PI
class Balle:

    XMAX = 750
    YMAX = 500

    def __init__(self , x , y , vx , vy , diam , r , g , b , type):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.diam = diam
        self.r = r
        self.g = g
        self.b = b
        self.ray = diam/2
        self.z = 0
        self.cycle = 1000
        self.type = type  #1: gravity 2: sinus 3: bounce 4: special

    def gravity(self):
        self.vy = self.vy + 0.15
        self.efface()
        self.deplace()
        self.affiche()
        

    def sinus(self):
        circle(self.x,self.y+cos(self.z)*20,50)
        self.x = self.x+1
        self.z = self.z+0.1
        if self.z > 2*PI:
            self.z=0
    

    def bounce(self):
        self.efface()
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


    

    def special(self , liste):
        def fokin_small_circle(x = 0 , y = 0):
            fill(250,100,100)
            ellipse(x , y , self.diam , self.diam/5)

        def fokin_twisty_mothafuka():
            pushMatrix()
            translate(self.x , self.y)
            rotate(PI/self.cycle * self.z)
            fokin_small_circle()

            popMatrix()

            self.z = 1 if self.z == self.cycle * 2 else self.z + 1
            self.cycle = self.cycle - 50
            if self.cycle < 50:
                self.cycle = 2000
                self.efface()
                liste.remove(self)
                liste.append(Balle(self.x , self.y , 7 , 7 , self.diam/2 , self.r , self.g , self.b , 3))
                liste.append(Balle(self.x , self.y , 7 , -7 , self.diam/2 , self.r , self.g , self.b , 3))
                liste.append(Balle(self.x , self.y , -7 , 7 , self.diam/2 , self.r , self.g , self.b , 3))
                liste.append(Balle(self.x , self.y , -7 , -7 , self.diam/2 , self.r , self.g , self.b , 3))


        if self.y > Balle.YMAX/2:
            self.efface()
            self.deplace()
            
            self.affiche()
            fokin_small_circle(self.x , self.y)
        else : 
            self.efface()
            self.affiche()
            fokin_twisty_mothafuka()

        

    def anime(self , liste):
        if self.type == 1:
            self.gravity()
        elif self.type == 2:
            self.sinus()
        elif self.type == 3:
            self.bounce()
        else:
            self.special(liste)
    

    def est_dans(self):
        pass


    def deplace(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy     
    

    def efface(self):
        fill(0,0,0)
        circle(self.x , self.y , self.diam+1)


    def affiche(self):
        fill(self.r , self.g , self.b)
        circle(self.x , self.y , self.diam)
