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
    while len(list_rect)> 0:
        current = list_rect.pop(0)
        best_fit_width_algo(list_rect, current, conteneur, etage)
        etage += 1

    return conteneur

def best_fit_width_algo(list_rect, current, conteneur, etage):
    conteneur.add(etage, current.h, current.w)
    remaing_W = conteneur.W - current.w

    while remaing_W > 0:
        min = findMinWidth(list_rect)
        if remaing_W - min.w < 0:
            break
        else:
            conteneur.add(etage, min.h, min.w)
            remaing_W -= min.w

def findMinWidth(listRect):
    min_rect = test.rect(1000000, 1000000)
    for r in listRect:
        if r.w < min_rect.w:
            min_rect = r
    listRect.remove(min_rect)
    return min_rect


















list_rect = convert_sorted_to_object_list(triHauteur(donnees))

#infiniteConteneur = test.FBS(convert_sorted_to_object_list(triHauteur(donnees)), 10,10)# on appelle la methode FBS du fichier test

infinite_cont = infinite_strip(list_rect)

etage_to_cont = test.etage_to_cont(infinite_cont)

#best_fit_strip_test = test.best_fit_strip_algo(etage_to_cont)




if __name__ == '__main__':

    for rect in infinite_cont.list_contain:
        print(rect)
