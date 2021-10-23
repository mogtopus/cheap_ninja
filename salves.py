from balle import *
niv_1 = [Balle(4) , Balle(5) , Balle(5) , Balle(2 , 'right') , Balle(2 , 'left') , Balle(1 , 'left') , Balle(1 , 'right') , Balle(4) , Balle(1 , 'right') , Balle(4)]
niv_2 = [Balle(4) , Balle(4), Balle(4) , Balle(4) , Balle(4)]


salve = []

def init(liste):
    global salve
    salve = niv_1 [:]
    for i in range (4):
        liste.append(salve.pop())
        


def ajoute_balles(liste ):
    global salve
    if len(liste) <= 4:
        for i in range (2):
               liste.append(salve.pop())
               

        
def update_liste():
    global salve
    if salve == []:
        print('niv+')
        salve = niv_2
