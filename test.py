


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






def findMinWidth(listRect):
    min_rect = rect(1000000, 1000000)
    for r in listRect:
        if r.w < min_rect.w:
            min_rect = r
    listRect.remove(min_rect)
    return min_rect




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
        best_fit_width_algo(list_rect, current, conteneur, etage)
        etage += 1
        if len(list_rect)>0:
            current = list_rect.pop(0)
            remaing_H = remaing_H - current.h
        else:
            break
    return conteneur


def handle_infinite_strip(list_rect):# retourne un conteneur (Box)
    return FBS(list_rect,100000,10)[0]


def etage_to_cont(infinite_cont):
    list_cont = []
    current_etage = -1;
    current_cont = None
    for rect in infinite_cont.list_contain:
        if rect[0] != current_etage:
            list_cont.append(current_cont)
            current_cont = box(rect[1], rect[2])
            current_etage = rect[0]
        current_cont.add(0,rect[1],rect[2])
    list_cont.pop(0)
    return list_cont










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




