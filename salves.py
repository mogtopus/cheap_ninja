from balle import *
niv_1 = [[Balle('tournante') , Balle('piegee') , Balle('piegee') , Balle('sinus' , 'right') , Balle('sinus' , 'left') , Balle('gravity' , 'left') , Balle('gravity' , 'right') , Balle('tournante') , Balle('gravity' , 'right') , Balle('tournante')] , 3]
niv_2 = [Balle(4) , Balle(4), Balle(4) , Balle(4) , Balle(4) , Balle(1 , 'left'), ]
niv_3 = [[Balle(1 , 'right') , Balle(1,'left') , Balle(1,'left') , Balle(1,'left')] , 5]

salve = []
nb_balles_min = 0

def init(liste , niveau):
    global salve , nb_balles_min
    nb_balles_min = niveau[1]
    salve = niveau [0][:]
    for i in range (4):
        liste.append(salve.pop())
        


def ajoute_balles(liste):
    global salve , nb_balles_min
    if len(liste) <= nb_balles_min and salve != []:
        for i in range (2):
               liste.append(salve.pop())

def verifie_vide(liste):
    for i in liste:
        if i.type != 'piegee':
            return False
    return True

def update_liste(liste):
    global salve
    if salve == [] and verifie_vide(liste):
        print('gagne')
