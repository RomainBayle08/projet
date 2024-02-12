import json as j

import test

with open("donnee_rect.json", "r") as fichier:
    # Charger les données depuis le fichier JSON
    donnees = j.load(fichier)


def fusion(l1: list, l2: list) -> list:
    """
    DESCRIPTION
    Fusionne deux listes de dictionnaires de maniere recursive de maniere decroissante par hauteur.

    ------------------------------------

    ENTREE
    l1: list -> Premiere liste de dictionnaire
    l2: list -> Seconde liste de dictionnaire

    ------------------------------------

    SORTIE
    Liste de dictionnaires
    """
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0]["h"] >= l2[0]["h"]:
        return [l1[0]] + fusion(l1[1:], l2)
    else:
        return [l2[0]] + fusion(l1, l2[1:])


def triHauteur(l) -> list:
    """
    DESCRIPTION
    Fonction de trie fusion d'une liste de dictionnaire

    ------------------------------------

    ENTREE
    l: list -> Liste de dictionnaire à trier

    ------------------------------------

    SORTIE
    Liste de dictionnaire tiee
    """
    if len(l) == 1:
        return l
    else:
        # trie de manière recursive la liste en utilisant la fonction fusion sur les demies listes.
        return fusion(triHauteur(l[:len(l) // 2]), triHauteur(l[len(l) // 2:]))


def convert_sorted_to_object_list(sortedList: list) -> list:
    """
    DESCRIPTION
    Fonction de conversion d'une liste de dictionnaire en liste d'objet 'rect'

    ------------------------------------

    ENTREE
    sortedList: list -> Liste de dictionnaire

    ------------------------------------

    SORTIE
    Liste d'objet 'rect'
    """
    listRect: list = []
    for dic in sortedList:  # convertir chaque dictionnaire en objet 'rect'
        current: test.rect = test.rect(dic['h'], dic['w'])
        listRect.append(current)
    return listRect


def printConteneurs(w: int, h: int, donnees: list):
    """
    DESCRIPTION
    Procedure qui cree, rempli et affiche le contenu des conteneurs

    ------------------------------------

    ENTREE
    w: int -> Largeur des conteneurs
    h: int -> Hauteur des conteneurs

    ------------------------------------

    SORTIE
    donnees: list -> liste de dictionnaires
    """
    list_rect: list = convert_sorted_to_object_list(
    triHauteur(donnees))  # trie les donnees par hauteur de maniere decroissante
    finiteConteneur: list = test.FBS(list_rect, w, h)  # on appelle la methode FBS du fichier test
    for box in finiteConteneur:  # affichage des conteneurs
        for obj in box.list_contain:
            print(obj)
        print('\n')  # saut de ligne



def infinite_strip(list_rect):# retourne un conteneur (Box)
    etage = 0
    conteneur = test.box(1000,10)

    while len(list_rect)>0:
        current = list_rect.pop(0)
        etage = best_fit_width_algo(current, conteneur, etage)
    return conteneur

def best_fit_width_algo(current, conteneur, etage):
    remaing_W = 10 # compteur de place restante
    etage_to_check = 0 # etage parcours
    is_fited = False   # l'objet courrant ( current) a été placer

    if etage == 0:  # si on est sur le premier etage
        if conteneur.list_contain: # si on a deja des elements
            for rect in conteneur.list_contain: # on calcul l'espace residuel
                remaing_W = remaing_W - rect[2]
        if remaing_W < current.w: # si on a pas de place on passe a l'etage suivant ( le 1 )
            etage = etage + 1
        conteneur.add(etage, current.h,current.w) # on ajoute le bloc courant a l'etage souhaiter
        return etage

    else:  # si on est au 2ieme etage ou plus
        for i in range(len(conteneur.list_contain)): # on passe tous les "rect" deja placer
            rect = conteneur.list_contain[i]
            if rect[0] > etage_to_check:  # si on change d'etage
                if remaing_W >= current.w: # si suffisament de place pour l'object courant a l'etage n-1
                    conteneur.list_contain.insert(i, (etage_to_check, current.h, current.w)) # on l'ajoute a l'indice actuel
                    is_fited = True # on dit que le bloc a été placer
                    break
                etage_to_check = rect[0] # vu qu'on a changer d'etage l'etage actuel deviens l'etage a l'indice i
                remaing_W = 10 # on remet a 0 le compteru de place restante
            remaing_W -= rect[2] # on soustrait la largeur du "rect" actuel au compter
        etage_to_check += 1
        if not is_fited:
            conteneur.add(etage_to_check,current.h,current.w) # si l'objet courant n'a pas pu etre placer il est placer dans un nouvel etage d'ou le etage_to_check +1
        return etage_to_check
















list_rect = convert_sorted_to_object_list(triHauteur(donnees))

#infiniteConteneur = test.FBS(convert_sorted_to_object_list(triHauteur(donnees)), 10,10)# on appelle la methode FBS du fichier test

infinite_cont = infinite_strip(list_rect)

#etage_to_cont = test.etage_to_cont_raw(infinite_cont)


#opti = test.etage_to_opti_cont(etage_to_cont)
#best_fit_strip_test = test.best_fit_strip_algo(etage_to_cont)




if __name__ == '__main__':

    for rect in infinite_cont.list_contain:
        print(rect)
    print('\n')
