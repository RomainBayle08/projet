import json as j

class box():
    w : int
    h : int
    def __init__(self, witdh, height):
        self.w = witdh
        self.h = height


with open("donnee_rect.json", "r") as fichier:
    # Charger les données depuis le fichier JSON
    donnees = j.load(fichier)


def triHauteur(donnees : list) -> list :
    donneeTrieHauteur :list = []
    while donnees != []:
        max :dict = donnees[0]
        for i in donnees:
            if max["h"] < i["h"]:
                max = i
        donneeTrieHauteur.append(max)
        donnees.remove(max)
    return donneeTrieHauteur

        
print(triHauteur(donnees))