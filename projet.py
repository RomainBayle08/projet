import json as j


HEIGHT , WIDTH = 10


with open("donnee_rect.json", "r") as fichier:
    # Charger les données depuis le fichier JSON
    donnees = j.load(fichier)

class box:
    H = 0
    W = 0
    list_contain = None

    def __init__(self, h, w):
        self.H = h
        self.W = w
        self.list_contain = []


    def add(self, etage, h, w):
        self.list_contain.append((etage, h, w))


class rect:
    h = 0
    w = 0

    def __init__(self, h, w):
        self.h = h
        self.w = w


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
    resultat = []
    i = j = 0

    while i < len(l1) and j < len(l2):
        if (l1[i]['h'], l1[i]['w']) >= (l2[j]['h'], l2[j]['w']):
            resultat.append(l1[i])
            i += 1
        else:
            resultat.append(l2[j])
            j += 1

    resultat.extend(l1[i:])
    resultat.extend(l2[j:])

    return resultat






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
        current: rect = rect(dic['h'], dic['w'])
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
    finiteConteneur: list = FBS(list_rect)  # on appelle la methode FBS du fichier test
    for box in finiteConteneur:  # affichage des conteneurs
        for obj in box.list_contain:
            print(obj)
        print('\n')  # saut de ligne






def FBS(list_rect):
    infinite_cont = infinite_strip(list_rect)
    to_etage = etage_to_cont(infinite_cont)
    opti = best_fit_cont_algo(to_etage)
    return opti



def infinite_strip(list_rect):# retourne un conteneur (Box)
    etage = 0
    conteneur = box(1000,WIDTH)

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
            for obj in conteneur.list_contain: # on calcul l'espace residuel
                remaing_W = remaing_W - obj[2]
        if remaing_W < current.w: # si on a pas de place on passe a l'etage suivant ( le 1 )
            etage = etage + 1
        conteneur.add(etage, current.h,current.w) # on ajoute le bloc courant a l'etage souhaiter
        return etage

    else:  # si on est au 2ieme etage ou plus
        for i in range(len(conteneur.list_contain)): # on passe tous les "rect" deja placer
            current_rect = conteneur.list_contain[i]
            if current_rect[0] > etage_to_check:  # si on change d'etage
                if remaing_W >= current.w: # si suffisament de place pour l'object courant a l'etage n-1
                    conteneur.list_contain.insert(i, (etage_to_check, current.h, current.w)) # on l'ajoute a l'indice actuel
                    is_fited = True # on dit que le bloc a été placer
                    break
                etage_to_check = current_rect[0] # vu qu'on a changer d'etage l'etage actuel deviens l'etage a l'indice i
                remaing_W = 10 # on remet a 0 le compteru de place restante
            remaing_W -= current_rect[2] # on soustrait la largeur du "rect" actuel au compter
        etage_to_check += 1
        if not is_fited:
            conteneur.add(etage_to_check,current.h,current.w) # si l'objet courant n'a pas pu etre placer il est placer dans un nouvel etage d'ou le etage_to_check +1
        return etage_to_check


def etage_to_cont(infinite_cont): # transforme juste les etage de la box infini en box independante
    list_cont = []
    current_etage = 0
    current_cont = box(HEIGHT, WIDTH)
    remaing_h = 0
    for obj in infinite_cont.list_contain:
        if obj[0] > current_etage  :
            remaing_h = 10- current_cont.list_contain[0][1]
            list_cont.append((remaing_h, current_cont))
            current_cont = box(HEIGHT, WIDTH)
            current_etage = obj[0]
        current_cont.add(0,obj[1],obj[2])
    return list_cont


def best_fit_cont_algo(list_cont): # prend la liste retourner par etage_to_count et optimise l'espace
    list_opti_cont=[]
    remaing_h_current_cont = 0
    while len(list_cont) > 0: # on passe tous les conteneur de la list
        cont_obj= list_cont.pop(0)
        remaing_h_current_cont = cont_obj[0]
        current_cont = cont_obj[1]
        for cont in list_cont: # pour chaque cont on regarde les cont qu'on a pas encore vu
            if 10-cont[0] <= remaing_h_current_cont: # si l'espace residuel est bon
                last_plus_grand_etage = current_cont.list_contain[len(current_cont.list_contain)-1][0] # on ajoute les valeurs de ce cont au cont courrant a un etage superieur
                for obj in cont[1].list_contain:
                    current_cont.add(last_plus_grand_etage+1,obj[1],obj[2])
                list_cont.remove(cont)
                break
        list_opti_cont.append(current_cont)
    return list_opti_cont


def local_search_calcul(box):
    alpha = 5
    somme_h_w_box = 0
    nb_element = len(box.list_contain)
    nb_total_rect = len(donnees)
    for rect in box.list_contain:
        somme_h_w_box+=(rect.w*rect.h)
    return alpha*(somme_h_w_box/(HEIGHT*WIDTH))-(nb_element/nb_total_rect)

def weakest_bin(list_cont):
    weakest = None
    for cont in list_cont:
        if weakest is None:
            weakest = cont
            weakest_quantity = local_search_calcul(weakest)
        else:
            bin_quantity = local_search_calcul(cont)
            if bin_quantity < weakest_quantity:
                weakest = cont
                weakest_quantity = bin_quantity
    return weakest

def local_search(list_cont):
    weakest = weakest_bin(list_cont)
    while True:
        if weakest.nb_items() == 0:
            list_cont.remove(weakest)
            weakest = weakest_bin(list_cont)
        size_weakest = len(weakest.items)
        for item in weakest.list_contain:
            for cont in list_cont:
                if cont != weakest:
                    result = FBS(cont.items + [item])
                    if len(result) == 1:
                        list_cont.remove(cont)
                        list_cont.apppend(result[0])
                        weakest.items.remove(item)
                        """ for shelf in weakest.shelves:
                            if item in shelf.items:
                                shelf.items.remove(item)
                                if len(shelf.items) == 0:
                                    weakest.shelves.remove(shelf)
                                break
                        break"""
        if len(weakest.items) == size_weakest:
            break


if __name__ == '__main__':
    printConteneurs(10,10,donnees)
