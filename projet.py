import json as j

import test
from test import *


class box():
    w: int
    h: int

    def __init__(self, witdh, height):
        self.w = witdh
        self.h = height


with open("donnee_rect.json", "r") as fichier:
    # Charger les données depuis le fichier JSON
    donnees = j.load(fichier)


def triHauteur(donnees: list) -> list:
    donneeTrieHauteur: list = []
    while donnees != []:
        max: dict = donnees[0]
        for i in donnees:
            if max["h"] < i["h"]:
                max = i
        donneeTrieHauteur.append(max)
        donnees.remove(max)
    return donneeTrieHauteur


def convert_sorted_to_object_list(sortedList): # on converti la list trier en une list d'objet Rect
    listRect = []
    for dic in sortedList:
        current = test.rect(dic['h'], dic['w'])
        listRect.append(current)
    return listRect


infiniteConteneur = test.FBS(convert_sorted_to_object_list(triHauteur(donnees))) # on appelle la methode FBS du fichier test




if __name__ == '__main__':
   for obj in infiniteConteneur.list_contain:
       print(obj)