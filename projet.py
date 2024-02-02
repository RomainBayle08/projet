import json as j

class box():
    w : int
    h : int
    def __init__(self, witdh, height):
        self.w = witdh
        self.h = height
      
H : int
W : int
H, W = 10, 10 #définition de la hauteur et largeur des boites

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
 
donnees = triHauteur(donnees)
print(donnees)
print(len(donnees))
