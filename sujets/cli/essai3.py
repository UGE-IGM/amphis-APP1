import sys

if len(sys.argv) < 3:
    print("Usage : python essai3.py mot nom_fichier")
    sys.exit()

mot_a_chercher = sys.argv[1]
nom_fichier = sys.argv[2]

with open(nom_fichier) as f:
    for ligne in f:
        if mot_a_chercher in ligne:
            print(ligne)


    