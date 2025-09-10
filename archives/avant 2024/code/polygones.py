# tracé de polygones
from fltk import *


if __name__ == "__main__":

    polygone_courant = []
    polygones = []

    cree_fenetre(1000, 800)
    while True:
        efface('ligne_temp')
        if polygone_courant:
            x, y = abscisse_souris(), ordonnee_souris()
            xd, yd = polygone_courant[-1]
            ligne(xd, yd, x, y, couleur='blue', tag='ligne_temp')
        mise_a_jour()
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == 'Quitte':
            break
        elif tev == 'ClicGauche':
            xn, yn = abscisse(ev), ordonnee(ev)
            polygone_courant.append((xn, yn))
            if len(polygone_courant) > 1:
                xp, yp = polygone_courant[-2]
                ligne(xp, yp, xn, yn)
        elif tev == 'ClicDroit':
            if len(polygone_courant) > 1:
                x0, y0 = polygone_courant[0]
                xd, yd = polygone_courant[-1]
                ligne(x0, y0, xd, yd)
                polygones.append(polygone_courant)
                polygone_courant = []

    ferme_fenetre()
