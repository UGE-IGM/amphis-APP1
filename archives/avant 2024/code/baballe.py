import fltk
from random import uniform


def somme_vecteurs(v1, v2):
    a, b = v1
    c, d = v2
    return [a + c, b + d]

    
def produit_scalaire(v, m):
    a, b = v
    return [a * m, b * m]


def dessine(mobile):
    pos, vit = mobile
    a, b = pos
    fltk.cercle(a, b, 10)


def deplace(mobile):
    pos, vit = mobile
    mobile[0] = somme_vecteurs(pos, vit)


def scene1():
    """Je veux une balle qui se déplace à une vitesse constante
    dans une direction fixe (aléatoire).
    """
    mobile = [[300, 300], [uniform(-2, 2), uniform(-2, 2)]]
    
    fltk.cree_fenetre(600, 600)

    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'Quitte':
            break
    
        fltk.efface_tout()
        dessine(mobile)
        deplace(mobile)
        fltk.mise_a_jour()

    fltk.ferme_fenetre()

scene1()