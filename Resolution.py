#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c,face=None,listeAretes=[]):
        self.cube=c
        self.face=face
        self.listeAretes=listeAretes

#Fonction qui renvoie quelle face est de la couleur recherchée (jaune pour mon algo ("Y"))
    def whichIsColor(self,color):
        
        colorF = cube.up[1][1]
        if colorF == 'Y' :
            return "u"
        colorF = cube.down[1][1]
        if colorF == 'Y' :
            return "d"
        colorF = cube.right[1][1]
        if colorF == 'Y' :
            return "r"
        colorF = cube.left[1][1]
        if colorF == 'Y' :
            return "l"
        colorF = cube.back[1][1]
        if colorF == 'Y' :
            return "b"
        colorF = cube.front[1][1]
        if colorF == 'Y':
            return "f"

#Fonction qui recherche les aretes manquantes puis effectue les rotations nécessaires pour les amener
    def solveYellow(self):
        listeColors=['G','R','B','O']
        for i in range(len(listeColors)):   
            self.listeAretes.append(cube.findCube(['Y',listeColors[i]]))
        #trouve toutes les aretes jaunes que l'on doit placer

    def checkCrossNonOriente(self):
        posColor = self.whichIsColor('Y')
        listeColors=['G','R','B','O']
        for i in range(len(listeColors)):
            pos = cube.findCube(['Y',listeColors[i][0][0]])
            print(pos)
            if pos[0][1] != posColor:
                return False
        return True

    def checkEmplacement(self):
        posColor = self.whichIsColor('Y')
        listeColors=['G','R','O','B']
        listos=[]
        liste=[]
        for i in range(len(listeColors)):
            listos=[]
            pos = cube.findCube(['Y',listeColors[i][0][0]])
            print(pos)
            print(pos[0][1])
            listos.append(pos[0][1])
            listos.append(listeColors[i][0][0])
            liste.append(listos)
            print(liste)
        return liste
        


cube = Cube("YBGGGGGGGRRRWWWOOOYYBGRRWWWOOOYYYYRRWWWOOGRYOBBBBBBBRY")

resolution = Resolution(cube)

cube.printCube()
        
resolution.solveYellow()

print(resolution.checkCrossNonOriente())
print(resolution.checkEmplacement())
