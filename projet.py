import json as j

import test


"""class box():
    w : int
    h : int
    def __init__(self, witdh, height):
        self.w = witdh
        self.h = height
      
H : int
W : int
H, W = 10, 10 #définition de la hauteur et largeur des boites"""

with open("donnee_rect.json", "r") as fichier:
    # Charger les données depuis le fichier JSON
    donnees = j.load(fichier)
   
def fusion(l1,l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0]["h"] >= l2[0]["h"]:
        return [l1[0]] + fusion(l1[1:], l2)
    else:
        return [l2[0]] + fusion(l1,l2[1:])

def triHauteur(l):
    if len(l) == 1:
        return l
    else:
        return fusion(triHauteur(l[:len(l)//2]) , triHauteur(l[len(l)//2:]))
 
#donnees = triHauteur(donnees)
#print(donnees)
#print(len(donnees))

def convert_sorted_to_object_list(sortedList): # on converti la list trier en une list d'objet Rect
    listRect = []
    for dic in sortedList:
        current = test.rect(dic['h'], dic['w'])
        listRect.append(current)
    return listRect





list_rect = convert_sorted_to_object_list(triHauteur(donnees))

infiniteConteneur = test.FBS(convert_sorted_to_object_list(triHauteur(donnees)),10,10) # on appelle la methode FBS du fichier test




if __name__ == '__main__':
    for box in infiniteConteneur:
        for obj in box.list_contain:
            print(obj)
        print('\n')