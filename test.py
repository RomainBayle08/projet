


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










def FBS(list_rect, conteneur_H,conteneur_W):
    list_cont = []
    while len(list_rect)>0:
        list_cont.append(fill_cont(list_rect,conteneur_H,conteneur_W))
    return list_cont





def fill_cont(list_rect, conteneur_H,conteneur_W):
    etage = 0
    current = list_rect.pop(0)
    remaing_H = conteneur_H - current.h
    conteneur = box(conteneur_H,conteneur_W)
    while remaing_H>=0:
       # projet.best_fit_width_algo(list_rect, current, conteneur, etage)
        etage += 1
        if len(list_rect)>0:
            current = list_rect.pop(0)
            remaing_H = remaing_H - current.h
        else:
            break
    return conteneur





def etage_to_cont_raw(infinite_cont):
    list_cont = []
    current_etage = 0;
    current_cont = box(10,10)
    remaing_h = 0
    for rect in infinite_cont.list_contain:

        if rect[0] > current_etage  :
            remaing_h = 10- current_cont.list_contain[0][1]
            list_cont.append((remaing_h, current_cont))
            current_cont = box(10, 10)
            current_etage = rect[0]
        current_cont.add(0,rect[1],rect[2])
    return list_cont


def etage_to_opti_cont(list_cont):
    list_opti_cont=[]
    remaing_h_current_cont = 0
    while len(list_cont) > 0:
        cont = list_cont.pop(0)
        remaing_h_current_cont = cont[0]
        current_cont = cont[1]
        closest_match = find_closest_match(list_cont,remaing_h_current_cont)
        if remaing_h_current_cont>0 and len(closest_match.list_contain)>0:
            current_cont.list_contain.extend(closest_match.list_contain)
        list_opti_cont.append(current_cont)
    return list_opti_cont

def find_closest_match(list_cont , remaing_h):
    closest_match = box(10,10)
    for cont in list_cont:
        if cont[0] <= remaing_h:
            closest_match.list_contain = cont[1].list_contain
    return closest_match

"""def best_fit_strip_algo(list_cont):
    list_cont_updated = []
    current_cont = box(10,10)
    remaing_h = 10
    for cont in list_cont:
        if remaing_h <0:
            list_cont_updated.append(current_cont)
            current_cont = box(10,10)
        current_cont.list_contain = cont.list_contain
        remaing_h = remaing_h - current_cont.list_contain[0][1]  # l'objet le plus grand est en [0] de chaque conteneur
    return list_cont_updated"""













