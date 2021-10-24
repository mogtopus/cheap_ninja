from balle import *
niv_1 = [Balle(4) , Balle(5) , Balle(5) , Balle(2 , 'right') , Balle(2 , 'left') , Balle(1 , 'left') , Balle(1 , 'right') , Balle(4) , Balle(1 , 'right') , Balle(4)]
niv_2 = [Balle(4) , Balle(4), Balle(4) , Balle(4) , Balle(4) , Balle(1 , 'left'), ]
#niv_1 = [Balle(1 , 'right') , Balle(1,'left') , Balle(1,'left') , Balle(1,'left')]

salve = []

def init(liste , niveau):
    global salve
    salve = niveau [:]
    for i in range (4):
        liste.append(salve.pop())
        


def ajoute_balles(liste):
    global salve
    if len(liste) < 4 and salve != []:
        for i in range (2):
               liste.append(salve.pop())

def verifie_vide(liste):
    for i in liste:
        if i.type != 5:
            return False
    return True


def update_liste(liste , niveau):
    global salve
    print(salve)
    if salve == [] and verifie_vide(liste):
        print('niv+')
        init(liste,niv_2)
        
