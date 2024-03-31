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






"""
            INFINITE STRIP
"""


def infinite_strip(list_rect):  # retourne un conteneur (Box)
    etage = 0
    inf_box = box(1000, WIDTH)
    res_w_space =[]

    while len(list_rect) > 0:
        current = list_rect.pop(0)
        etage = BF_w_algo(current, inf_box, etage,res_w_space)
    return inf_box


"""

        ALGOS POUR LA MEILLEUR SELECTION PAR RAPPORT A LA LARGEUR 
"""

def find_best(liste , value):
    n = len(liste)
    # Cas où la première valeur est supérieure ou égale à res_w
    if liste[0][1] >= value:
        return liste[0]
    # Cas où la dernière valeur est inférieure à res_w
    if liste[n - 1][1] < value:
        return (-1,-1)  # Aucune valeur trouvée

    gauche, droite = 0, n - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu][1] < value:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return liste[gauche] if gauche < n else (-1,-1)  # Si gauche dépasse la longueur de la liste, aucun élément trouvé


def insert_in_floor(rect, box, etage):
    for i in range(len(box.list_rect)):
        current = box.list_rect[i]
        if current[0] > etage:
            box.list_rect.insert(i, (etage, rect)) #Changement ICI
            break
    return box

def update_res(res_w_space , floor , remain):
    # Trouver l'indice du tuple à mettre à jour
    index = -1
    for i, tuple_ in enumerate(res_w_space):
        if tuple_[0] == floor:
            index = i
            break

    # Mettre à jour le tuple
    if index != -1:
        res_w_space[index] = (floor, remain)
        # Déplacer le tuple vers sa position correcte dans la liste triée
        while index > 0 and res_w_space[index][1] < res_w_space[index - 1][1]:
            res_w_space[index], res_w_space[index - 1] = res_w_space[index - 1], res_w_space[index]
            index -= 1
        while index < len(res_w_space) - 1 and res_w_space[index][1] > res_w_space[index + 1][1]:
            res_w_space[index], res_w_space[index + 1] = res_w_space[index + 1], res_w_space[index]
            index += 1



def BF_w_algo(current, box, etage,res_w_space):
    if etage == 0:  # si on est sur le premier etage
        if not res_w_space:  # si on a deja des elements
            res_w_space.append((etage,WIDTH))
        if res_w_space[etage][1] < current.w:  # si on a pas de place on passe a l'etage suivant ( le 1 )
            etage = etage + 1
            res_w_space.append((etage,WIDTH-current.w))
        else:
            res_w_space[etage] = (etage,res_w_space[etage][1]-current.w)
        box.add(etage, current)  # on ajoute le bloc courant a l'etage souhaiter
        return etage

    else:  # si on est au 2eme étage ou plus
        highest_floor = box.list_rect[len(box.list_rect) - 1][0]
        best = find_best(res_w_space, current.w)
        best_floor = best[0]
        if best_floor != -1:
            remaing = best[1]-current.w
            if best_floor == highest_floor:
                box.add(highest_floor,current)
            else:
                insert_in_floor(current,box,best_floor)

            update_res(res_w_space,best_floor,remaing)
        else:
            highest_floor+=1
            box.add(highest_floor,current)
            res_w_space.append((highest_floor,WIDTH-current.w))
            update_res(res_w_space, highest_floor, WIDTH-current.w)
        return highest_floor





"""

            FBS

"""

def FBS(list_rect):
    infinite_cont = infinite_strip(list_rect.copy())
    boxes = to_boxes(infinite_cont)
    opti = BF_box_algo(boxes)
    return opti


"""
        ALGOS POUR LA MEILLEUR SELECTION PAR RAPPORT A LA HAUTEUR 

"""
def up_res_h(boxes, tuple):
    i = len(boxes) - 1
    while i >0 and boxes[i][1] > tuple[1]:
        i -= 1
    boxes.insert(i + 1, tuple)

def best_box(boxes, value):
    left, right = 0, len(boxes) - 1
    result = (-1, -1)  # Initialisation du résulta
    while left <= right:
        mid = (left + right) // 2
        # Vérifier si x + valeur == 10
        if boxes[mid][1] + value == 10:
            return boxes[mid]  # Si c'est le cas, retourner le tuple trouvé

        # Mettre à jour le résultat et continuer la recherche vers la gauche
        if boxes[mid][1] + value < 10:
            left = mid + 1
        else:
            # Si x + valeur > 10, continuer la recherche vers la gauche
            right = mid - 1

    return result

def to_boxes(infinite_box):  # transforme juste les etage de la box infini en box independante
    boxes = []
    current_etage = 0
    current_cont = box(HEIGHT, WIDTH)
    remaing_h = 0
    for obj in infinite_box.list_rect:
        if obj[0] > current_etage:
            remaing_h = 10 - current_cont.list_rect[0][1].h
            up_res_h(boxes,(current_cont,remaing_h))
            current_cont = box(HEIGHT, WIDTH)
            current_etage = obj[0]
        current_cont.add(0, obj[1])
    remaing_h = 10 - current_cont.list_rect[0][1].h
    up_res_h(boxes,(current_cont,remaing_h))
    return boxes


def BF_box_algo(list_box):  # prend la liste retourner par etage_to_count et optimise l'espace
    opti_boxes = []  #Changement ICI

    while len(list_box) > 0: # pour chaque box
        current = list_box.pop(0)
        box = current[0]
        box_h = current[1]
        best = best_box(list_box,box_h)
        if best[0] !=-1:
            box = fusion_boxes(box, best[0]) # on les fusions
            list_box.remove(best) # pareil
        opti_boxes.append(box) # on ajoute la box a la lis t#Changement ICI
    return opti_boxes  #Changement ICI



def fusion_boxes(box1, box2):
    max_floor_b1 = box1.list_rect[len(box1.list_rect) - 1][0] + 1
    for rect in box2.list_rect:
        box1.list_rect.append((rect[0] + max_floor_b1, rect[1]))#Changement ICI
    return box1


"""
            ALGOS POUR LA LOCAL SEARCH 
"""


def WB_calcul(box):
    alpha = 5
    sum_h_w_box = 0
    nb_element = len(box.list_rect)
    nb_total_rect = len(donnees)
    for rect in box.list_rect:
        sum_h_w_box += (rect[1].h * rect[1].w)
    return alpha * (sum_h_w_box / (HEIGHT * WIDTH)) - (nb_element / nb_total_rect)


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



def local_search(list_box):
    wb = weakest_bin(list_box)

    while True:
        list_box.remove(wb)  # on enleve la weakest bin de la liste

        list_rect = box_to_rect(
            list_box)  # on cree un nouvelle lsit de rect sans ceux de la weakest bin

        if not wb.list_rect:  # si la weakest bin est vide on en prend une autre
            wb = weakest_bin(list_box)

        len_weakest = len(wb.list_rect)  # on sauvegarde la taille initial de la WB

        for rect in wb.list_rect:  # on passe tous les element de la WB
            list_rect.append(rect[1])  # on ajoute l'element courant a la liste MAJ
            new_list_cont = FBS(list_rect)  # on fait le FBS sur cette liste
            if len(new_list_cont) == len(list_box):  # si l'element est rentré la list_cont deviens la list_cont MAJ
                list_box = new_list_cont
                wb.list_contain.remove(rect)  # et on enleve l'element de la WB
            else:
                list_rect.remove(rect[1])
        if len_weakest == len(wb.list_rect):  # si la WB n'a pas bougé on sort
            list_box.append(wb)  # dans ce cas on remet la WB dans la list
            break

    return list_box

def box_to_rect(list_cont):
    list_rect = []
    for box in list_cont:
        for rect in box.list_rect:
            list_rect.append(rect[1])
    return list_rect

"""
            ALGO SHAKING ( en cours ) 
"""


def shacking(list_box , k ):
    if k > len(donnees):
        print("erreur")
    else:
        nb_box = len(list_box)
        for i in range(k):
            rand = random.randrange(nb_box)
            rand_box= list_box[rand]
            rand_rect = random.choice(rand_box.list_rect)
            list_box.append(box(HEIGHT,WIDTH))
            list_box[-1].add(0,rand_rect[1])
            rand_box.list_rect.remove(rand_rect)
            if not rand_box.list_rect:
                list_box.remove(rand_box)
                nb_box-=1
    return list_box






"""
    METHODE GLOBAL 

"""

def bvns(donnees_de_base):
    données_trie_cast = to_list_rect(triHauteur(donnees_de_base))
    best_solution = FBS(données_trie_cast)
    best_solution = local_search(best_solution)
    while len(best_solution) !=7:
        best_solution = shacking(best_solution,4)
        best_solution = local_search(best_solution)
    return best_solution





if __name__ == '__main__':
    test = bvns(donnees)
    for box in test:
        for rect in box.list_rect:
            print(rect[0],rect[1].to_string())
        print("\n")