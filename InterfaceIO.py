from Resolution import *

class InterfaceIO:

#classe qui gère les entrées sorties avec l'utilisateur
    
    def __init__(self, entree=None, sortie=None):
        self.entry=entree
        self.output=sortie

#l'utilisateur entre dans le programme la position du cube de départ
        
    def getEntry(self):
        self.entry = input("Entrez la configuration du Rubik's Cube a résoudre :")
        
        #54 correspond au nombre de cases d'un rubik's cube
        while self.checkEntry() == False:
            print("Erreur, configuration impossible.")
            self.entry = input("Réessayez : ")

#vérifie que l'entrée contient le nombre de caractères nécessaires et les bons caracteres
            
    def checkEntry(self):
        carac=["B","R","Y","W","G","O"]
        n = len(self.entry)
#On vérifie que l'entrée contient 54 caracteres
        if len(self.entry) != n :
            return False
#On verifie que les caracteres entrés sont les bons
        for i in range(n):
            if self.entry[i] not in carac:
                return False
        return True
            
#renvoie les mouvements a faire a l'utilisateur
            
    def setOutput(self):

        self.output = resolutionFinale(self.entry)
        print(self.output)
        
        
        
        
#bonjour = InterfaceIO()
#bonjour.getEntry()

resolutionCube = InterfaceIO()
resolutionCube.getEntry()
resolutionCube.setOutput()

