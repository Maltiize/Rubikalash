class InterfaceIO:

#classe qui gère les entrées sorties avec l'utilisateur
    def __init__(self, entree=None, sortie=None):
        self.entree=entree
        self.sortie=sortie

#récupère le cube de départ
    def PrendEntree(self):
        self.entree = input("Entrez la configuration du Rubik's Cube a résoudre")
        
#renvoie les mouvements a faire a l'utilisateur
    def EnvoieSortie(self):
        
        
