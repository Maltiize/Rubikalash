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
    
        #self.output = resolutionFinale("RWYRWGOGOYYGWRWBOOBOGGGYORGWBWBOYBBGYRRBRGWOWOWYYYBRBR")
        self.output = resolutionFinale("D2 L U2 B' U L2 R' D2 B D2 B2 F' L' D' R2 L' U2 B2 D' U' F' L' F2 B' R'")
        #JEAN self.output = resolutionFinale("B' R L U' B' U' R' U2 R' L2 D2 R U2 B2 D L2 U2 B2 F2 R2 F' L R' B2 R")
        #OMAR self.output = resolutionFinale("U' F U2 L' D2 L' U2 L2 D' B2 F2 R' D' F2 D' F' U2 D2 F D R2 F' R' U' L'")
        self.output = resolutionFinale("U' L' F R2 F2 U R U B2 R' U F2 B2 R B2 F' R L U' R B U2 B F U2")
        #JEAN self.output = resolutionFinale("D' U2 F2 R F2 B2 R' U2 R' L2 F2 B R D2 U2 R' F U' R' L2 D2 U2 R' D2 L")
        self.output = resolutionFinale("B' D' B' L' D2 U2 L U' D2 L F' B2 L' B2 D2 B' L' D2 L' B2 L R' U R F")
        print(self.output)
        
        
        
        
#bonjour = InterfaceIO()
#bonjour.getEntry()

resolutionCube = InterfaceIO()
#resolutionCube.getEntry()
resolutionCube.setOutput()

