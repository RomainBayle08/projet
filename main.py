# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import turtle

# Fonction pour dessiner un carré
def dessiner_carre(longueur):
    for _ in range(4):
        turtle.forward(longueur)
        turtle.left(90)

# Liste de longueurs pour les carrés
longueurs_carres = [50, 30, 70, 40]

# Espacement entre les carrés
espace_entre_carres = 10

# Positionnez la tortue au début du dessin
turtle.penup()
turtle.goto(-(sum(longueurs_carres) + espace_entre_carres * (len(longueurs_carres) - 1)) / 2, 0)
turtle.pendown()

# Dessinez les carrés
for longueur in longueurs_carres:
    dessiner_carre(longueur)
    turtle.forward(espace_entre_carres + longueur)

# Fermez la fenêtre lorsqu'elle est cliquée
turtle.exitonclick()