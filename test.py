import random , copy


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


class all_boxes:
    list_boxes =None
    def __init__(self):
        self.list_boxes = []
    def add_box(self,this_box):
        self.list_boxes.insert(len(self.list_boxes)-1,this_box)


listRect = []

i = 10

while i > 0:
    current = rect(random.randint(1, 10), random.randint(1, 10))
    listRect.append(current)
    i -= 1


def findMinWidth(listRect):
    min_rect = rect(1000000, 1000000)
    for r in listRect:
        if r.w < min_rect.w:
            min_rect = r
    listRect.remove(min_rect)
    return min_rect


"""def FBS(list_rect, conteneur, list_cont):
    etage = 0
    remaing_H = conteneur.H
    while len(list_rect) > 0:
        current = list_rect.pop(0)
        remaing_H -=current.h
        if remaing_H >= 0:
            best_fit_algo(list_rect, current, conteneur, etage)
            etage += 1
            print(conteneur.list_contain)
        else:
            new_cont = box(conteneur.H, conteneur.W)
            FBS(list_rect, new_cont, list_cont)

    list_cont.append(conteneur)"""

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
        best_fit_algo(list_rect, current, conteneur, etage)
        etage += 1
        if len(list_rect)>0:
            current = list_rect.pop(0)
            remaing_H = remaing_H - current.h
        else:
            break
    return conteneur













def best_fit_algo(list_rect, current, conteneur, etage):
    conteneur.add(etage, current.h, current.w)
    remaing_W = conteneur.W - current.w

    while remaing_W > 0:
        min = findMinWidth(list_rect)
        if remaing_W - min.w < 0:
            break
        else:
            conteneur.add(etage, min.h, min.w)
            remaing_W -= min.w



if __name__ == '__main__':
    for r in listRect:
        print(r.h, r.w)
    conteneur = FBS(listRect)
    for rect in conteneur.list_contain:
        print(rect)
