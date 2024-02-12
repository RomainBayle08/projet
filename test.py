


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





def etage_to_cont(infinite_cont): # transforme juste les etage de la box infini en box independante
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


def best_fit_cont_algo(list_cont): # prend la liste retourner par etage_to_count et optimise l'espace
    list_opti_cont=[]
    remaing_h_current_cont = 0
    while len(list_cont) > 0:
        cont = list_cont.pop(0)
        remaing_h_current_cont = cont[0]
        current_cont = cont[1]
        for cont in list_cont:
            if 10-cont[0] <= remaing_h_current_cont:
                last_plus_grand_etage = current_cont.list_contain[len(current_cont.list_contain)-1][0]
                for rect in cont[1].list_contain:
                    current_cont.add(last_plus_grand_etage+1,rect[1],rect[2])
                list_cont.remove(cont)
                break
        list_opti_cont.append(current_cont)
    return list_opti_cont















