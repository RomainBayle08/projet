import random


class box:
    H = 0
    W = 0
    list_contain = []

    def __init__(self, h, w):
        self.H = h
        self.W = w

    def add(self, etage , h, w):
        self.list_contain.append((etage , h,w))


class rect:
    h=0
    w=0

    def __init__(self,h,w):
        self.h = h
        self.w = w


listRect = []

i = 10

while i >0:
    current = rect(random.randint(1,10),random.randint(1,10))
    listRect.append(current)
    i-=1




def findMinWidth(listRect):
    min_rect = rect(1000000,1000000)
    for r in listRect:
        if r.w < min_rect.w :
            min_rect = r
    listRect.remove(min_rect)
    return min_rect


def FBS(list_rect):
    etage = 0
    conteneur = box(1000,10)
    
    while len(list_rect) > 0:
        current = list_rect.pop(0)

        conteneur.add(etage , current.h , current.w)
        remaing = conteneur.W - current.w

        while remaing >0 :
            min = findMinWidth(list_rect)
            if remaing - min.w < 0 :
                break
            else:
                conteneur.add(etage , min.h,min.w)
                remaing-=min.w

        etage+=1

    return conteneur



if __name__ == '__main__':
    for r in listRect:
        print(r.h,r.w)
    conteneur = FBS(listRect)
    for rect in conteneur.list_contain:
        print(rect)



