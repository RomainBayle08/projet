import json as j
import random

HEIGHT = 10
WIDTH = 10

with open("donnee_rect.json", "r") as fichier:
    # Charger les données depuis le fichier JSON
    donnees = j.load(fichier)


class box:
    H = 0
    W = 0
    list_rect = None

    def __init__(self, h, w):
        self.H = h
        self.W = w
        self.list_rect = []

    def add(self, etage,rect):
        self.list_rect.append((etage, rect))


class rect:
    h = 0
    w = 0

    def __init__(self, h, w):
        self.h = h
        self.w = w

    def to_string(self):
        return " h: "+str(self.h)+" w: "+str(self.w)


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


def to_list_rect(sortedList: list) -> list:
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


def printBoxes(donnees: list):
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
    list_rect: list = to_list_rect(
        triHauteur(donnees))  # trie les donnees par hauteur de maniere decroissante
    finiteConteneur: list = FBS(list_rect)  # on appelle la methode FBS du fichier test
    for box in finiteConteneur:  # affichage des conteneurs
        for obj in box.list_rect:
            print(obj[1],rect.to_string())
        print('\n')  # saut de ligne


def FBS(list_rect):
    cloned_list_rect = list_rect.copy()
    infinite_cont = infinite_strip(cloned_list_rect)
    boxes = to_boxes(infinite_cont)
    opti = BF_box_algo(boxes)
    return opti


"""
            INFINITE STRIP
"""


def infinite_strip(list_rect):  # retourne un conteneur (Box)
    etage = 0
    inf_box = box(1000, WIDTH)

    while len(list_rect) > 0:
        current = list_rect.pop(0)
        etage = BF_w_algo(current, inf_box, etage)
    return inf_box


"""

        ALGOS POUR LA MEILLEUR SELECTION PAR RAPPORT A LA LARGEUR 
"""


def BF_w_algo(current, conteneur, etage):
    remaing_W = 10  # compteur de place restante

    if etage == 0:  # si on est sur le premier etage
        if conteneur.list_rect:  # si on a deja des elements
            for obj in conteneur.list_rect:  # on calcul l'espace residuel
                remaing_W = remaing_W - obj[1].w #Changement ICI
        if remaing_W < current.w:  # si on a pas de place on passe a l'etage suivant ( le 1 )
            etage = etage + 1
        conteneur.add(etage,current)  # on ajoute le bloc courant a l'etage souhaiter #Changement ICI
        return etage

    else:  # si on est au 2eme étage ou plus
        highest_floor = conteneur.list_rect[len(conteneur.list_rect) - 1][0]
        res_space = res_w_space(conteneur)
        selected_etage = -1
        for etage in res_space:
            if etage[1] >= current.w:
                selected_etage = etage[0]
                break
        if selected_etage != -1:
            conteneur = insert_in_floor(current, conteneur, selected_etage)
            return highest_floor
        else:
            highest_floor += 1
            conteneur.add(highest_floor, current)#Changement ICI
            return highest_floor


def res_w_space(box):  # on regarde par etage l'espace residuel
    flors_res_w = []
    current_etage = 0
    residual_width = 10
    for rect in box.list_rect:
        if rect[0] > current_etage:
            flors_res_w.append((current_etage, residual_width))
            current_etage = rect[0]
            residual_width = 10
        residual_width -= rect[1].w #Changement ICI
    flors_res_w.append((current_etage, residual_width))
    flors_res_w.sort(key=lambda x: x[1]) #Changement ICI
    return flors_res_w


def insert_in_floor(rect, box, etage):
    for i in range(len(box.list_rect)):
        current = box.list_rect[i]
        if current[0] > etage:
            box.list_rect.insert(i, (etage, rect)) #Changement ICI
            break
    return box


"""
        ALGOS POUR LA MEILLEUR SELECTION PAR RAPPORT A LA HAUTEUR 

"""


def to_boxes(infinite_box):  # transforme juste les etage de la box infini en box independante
    list_box = []
    current_etage = 0
    current_cont = box(HEIGHT, WIDTH)
    remaing_h = 0
    for obj in infinite_box.list_rect:
        if obj[0] > current_etage:
            remaing_h = 10 - current_cont.list_rect[0][1].h
            list_box.append((remaing_h, current_cont))
            current_cont = box(HEIGHT, WIDTH)
            current_etage = obj[0]
        current_cont.add(0, obj[1])
    remaing_h = 10 - current_cont.list_rect[0][1].h
    list_box.append((remaing_h, current_cont))
    return list_box


def BF_box_algo(list_box):  # prend la liste retourner par etage_to_count et optimise l'espace
    list_opti_box = []  #Changement ICI
    sort_list_box = sorted(list_box, key=lambda x: x[0]) # on cree une list trier des espace residuel H croissant

    while len(list_box) > 0: # pour chaque box
        current = list_box.pop(0)
        box = current[1]
        box_remaing_h = current[0]
        for cont in sort_list_box: # on regarde tous les conteneur
            if cont[0] + box_remaing_h == 10: # si ils peuvent fusionner
                box = fusion_boxes(box, cont[1]) # on les fusions
                sort_list_box.remove(cont) # on retire les box des lists
                list_box.remove(cont) # pareil
                break
        sort_list_box.remove(current)# pareil
        list_opti_box.append(box) # on ajoute la box a la lis t#Changement ICI
    return list_opti_box  #Changement ICI



def fusion_boxes(box1, box2):
    highest_etage_b1 = box1.list_rect[len(box1.list_rect) - 1][0] + 1
    for rect in box2.list_rect:
        box1.list_rect.append((rect[0] + highest_etage_b1, rect[1]))#Changement ICI
    return box1


"""
            ALGOS POUR LA LOCAL SEARCH 
"""


def WB_calcul(box):
    alpha = 5
    somme_h_w_box = 0
    nb_element = len(box.list_rect)
    nb_total_rect = len(donnees)
    for rect in box.list_rect:
        somme_h_w_box += (rect[1].h * rect[1].w)
    return alpha * (somme_h_w_box / (HEIGHT * WIDTH)) - (nb_element / nb_total_rect)


def weakest_bin(list_box):#Changement ICI
    weakest = None
    for cont in list_box:#Changement ICI
        if weakest is None:
            weakest = cont
            weakest_quant = WB_calcul(weakest)
        else:
            bin_quantity = WB_calcul(cont)
            if bin_quantity < weakest_quant:
                weakest = cont
                weakest_quant = bin_quantity
    return weakest



def local_search(list_cont):
    wb = weakest_bin(list_cont)

    while True:
        list_cont.remove(wb)  # on enleve la weakest bin de la liste

        list_rect = box_to_rect(
            list_cont)  # on cree un nouvelle lsit de rect sans ceux de la weakest bin

        if not wb.list_contain:  # si la weakest bin est vide on en prend une autre
            wb = weakest_bin(list_cont)

        len_weakest = len(wb.list_contain)  # on sauvegarde la taille initial de la WB

        for rect in wb.list_contain:  # on passe tous les element de la WB
            list_rect.append(rect[1])  # on ajoute l'element courant a la liste MAJ
            new_list_cont = FBS(list_rect)  # on fait le FBS sur cette liste
            if len(new_list_cont) == len(list_cont):  # si l'element est rentré la list_cont deviens la list_cont MAJ
                list_cont = new_list_cont
                wb.list_contain.remove(rect)  # et on enleve l'element de la WB
            else:
                list_rect.remove(rect[1])
        if len_weakest == len(wb.list_contain):  # si la WB n'a pas bougé on sort
            list_cont.append(wb)  # dans ce cas on remet la WB dans la list
            break

    return list_cont

def box_to_rect(list_cont):
    list_rect = []
    for box in list_cont:
        for rect in box.list_rect:
            list_rect.append(rect[1])
    return list_rect

"""
            ALGO SHAKING ( en cours ) 
"""

# def shacking(list_cont , k ):


# def remove_selected_for_list(list):


def select_random_rect(list_cont, k):
    list_rect = box_to_rect(list_cont)
    nb_rect = len(list_rect)
    selected_rect = []
    for i in range(k):
        selected_rect.append(list_rect[random.randint(0, nb_rect)])
    return selected_rect



"""
    METHODE GLOBAL 

"""

def bvns(donnees_de_base):
    données_trie_cast = to_list_rect(triHauteur(donnees_de_base))
    result_FBS = FBS(données_trie_cast)
    result_local_search = local_search(result_FBS)
    return result_local_search




if __name__ == '__main__':
    lc = bvns(donnees)
    for box in lc :
        for rect in box.list_contain:
            print (rect[0],rect[1].to_string())
        print("\n")