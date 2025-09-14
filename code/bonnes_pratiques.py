# En tête de fichier : documentation du module
"""
Module peu intéressant mais bien structuré.
Auteur : anonyme.
"""

# Imports
from foo import bar, baz
import mymodule

# Définition de variables globales (au moins les constantes !)
largeur_fenetre = 800
hauteur_fenetre = 600


# Définitions de fonctions et classes
def f1(a, b, c):
    """Renvoie un truc."""
    res = bar(a, b, c)
    return baz(res)


def main():
    print(f1(mymodule.myconstant))


# Fin de fichier : programme principal
if __name__ == "__main__":
    main()
