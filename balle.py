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
        
    def gravity(self):
        pass
        
    def sinus(self):
        pass
    
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
        
        self.deplace()
        self.affiche()
    
    def anime(self):
        pass
    
    def est_dans(self):
        pass

    def deplace(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy     

    def affiche(self):
        fill(self.r , self.g , self.b)
        circle(self.x , self.y , self.diam)
