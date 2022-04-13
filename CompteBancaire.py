class CompteBancaire(object):
  def __init__(self, nom ='Ali', solde =10000):
    self.nom, self.solde = nom, solde
  def depot(self, somme):
    self.solde = self.solde + somme
  def retrait(self, somme):
    self.solde = self.solde - somme
  def affiche(self):
    print("Le solde du compte bancaire de {0} est de {1} dirhams.".\format(self.nom, self.solde))
# Programme de test :
c1 = CompteBancaire('Brahim', 800)
c1.depot(350)
c1.retrait(200)
c1.affiche()
