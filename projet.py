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



list_rect = convert_sorted_to_object_list(triHauteur(donnees))

#infiniteConteneur = test.FBS(convert_sorted_to_object_list(triHauteur(donnees)), 10,10)# on appelle la methode FBS du fichier test

infinite_cont = test.handle_infinite_strip(list_rect)

tested = test.etage_to_cont(infinite_cont)




if __name__ == '__main__':
    for box in tested:
        for obj in box.list_contain:
            print(obj)
        print('\n')
