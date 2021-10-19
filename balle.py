class Balle:
    XMAX = 500
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
        
    def gravity(self):
        pass
        
    def sinus(self):
        pass
    
    def bounce(self):
        #if self.x 
        pass
    
    def anime(self):
        pass
    
    def est_dans(self):
        pass

    def deplace(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy     

    def affiche(self):
        fill(self.r self.g , self.b)
        circle(self.x , self.y , self.diam)
