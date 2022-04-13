import random
class Domino(object):
    def __init__(self, pa, pb):
        self.pa, self.pb = pa, pb
    def affiche_points(self):
        print ("face A :", self.pa)
        print ("face B :", self.pb)
    def valeur(self):
        return self.pa + self.pb
# Programme de test :
d1 = Domino(2,6)
d2 = Domino(4,3)
d1.affiche_points()
d2.affiche_points()
print("total des points :", d1.valeur() + d2.valeur())
liste_dominos = []
vt =0
for i in range(6):
    a=random.randint(0,6)
    b=random.randint(0,6)
    #print(a,b)
    liste_dominos.append(Domino(a, b))
    
for i in range(6):
    liste_dominos[i].affiche_points()
    vt = vt + liste_dominos[i].valeur()
print("valeur totale des points", vt)
