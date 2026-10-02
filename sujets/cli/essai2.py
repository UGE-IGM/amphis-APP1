import sys

with open(sys.argv[1]) as f:
    mots = f.read().split()
    for mot in mots:
        print(mot)