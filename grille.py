import fltk

largeur_fenetre = 500
hauteur_fenetre = 500
nombre_lignes = 10
nombre_colonnes = 10
hauteur_ligne = hauteur_fenetre / nombre_lignes
largeur_colonne = largeur_fenetre / nombre_colonnes
    
def dessine_quadrillage():
    for i in range(1, nombre_lignes):
        y = i * hauteur_ligne
        fltk.ligne(0, y, largeur_fenetre, y)
    for i in range(1, nombre_colonnes):
        x = i * largeur_colonne
        fltk.ligne(x, 0, x, hauteur_fenetre)

if __name__ == "__main__":
    fltk.cree_fenetre(largeur_fenetre, hauteur_fenetre)
    dessine_quadrillage()
    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        if tev == 'Quitte':
            break
        elif tev == 'ClicGauche':
            xs, ys = fltk.abscisse(ev), fltk.ordonnee(ev)
            numero_ligne = ys // hauteur_ligne
            numero_colonne = xs // largeur_colonne
            print(f"ligne {numero_ligne}, colonne {numero_colonne}")
        fltk.mise_a_jour()
    fltk.ferme_fenetre()
