class Balle:
    XMAX = 750
    YMAX = 500
    def __init__(self , x , y , vx , vy , diam , r , g , b):
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
        
    def gravity(self):
        pass
        
    def sinus(self):
        circle(self.x,self.y+cos(self.z)*20,50)
        self.x = self.x+1
        self.z = self.z+0.1
        if self.z > 2*PI:
            self.z=0
    
    def bounce(self):
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
        self.efface()
        self.deplace()
        self.affiche()
    
    def anime(self):
        pass
    
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
