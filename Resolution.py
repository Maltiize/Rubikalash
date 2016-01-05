#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c,face=None,listeAretes=[]):
        self.cube=c
        self.face=face
        self.listeAretes=listeAretes

#Fonction qui renvoie quelle face est de la couleur recherchée (jaune pour mon algo ("Y"))
#On compare avec la couleur de chaque face en [1][1] et donc au milieu
    def whichIsColor(self,color):
        colorF = cube.up[1][1]  
        if colorF == color :
            return "u"
        colorF = cube.down[1][1]
        if colorF == color :
            return "d"
        colorF = cube.right[1][1]
        if colorF == color :
            return "r"
        colorF = cube.left[1][1]
        if colorF == color :
            return "l"
        colorF = cube.back[1][1]
        if colorF == color :
            return "b"
        colorF = cube.front[1][1]
        if colorF == color:
            return "f"

#Fonction qui recherche les aretes manquantes puis effectue les rotations nécessaires pour les amener
    def solveYellow(self):
        listeColors=['G','R','B','O']
        for i in range(len(listeColors)):   
            self.listeAretes.append(cube.findCube(['Y',listeColors[i]]))
        #trouve toutes les aretes jaunes que l'on doit placer
            
#Fonction qui vérifie si la croix non orienté est vérifiée
    def checkCrossNonOriente(self):
        posColor = self.whichIsColor('Y')   #on trouve la position de la face jaune
        listeColors=['G','R','B','O']       #c'est la liste des couleurs composants les aretes avec une face jaune
        for i in range(len(listeColors)):   #on parcout la liste des couleurs
            pos = cube.findCube(['Y',listeColors[i][0][0]]) #on récupère la position des aretes
            if pos[0][1] != posColor:   #si la position de la face jaune des aretes n'est pas sur la face jaune, alors la croix n'est pas vérifiée
                return False
        return True

#pas utile cette fonction apparemment
#on récupère l'emplacement des aretes
    def checkEmplacement(self):
        posColor = self.whichIsColor('Y')
        listeColors=['G','R','O','B']
        listos=[]
        liste=[]
        for i in range(len(listeColors)):
            listos=[]
            pos = cube.findCube(['Y',listeColors[i][0][0]])
            listos.append(pos[0][1])
            listos.append(listeColors[i][0][0])
            liste.append(listos)
        return liste

#fonction resolvant la croix yellow
    def resolutionYellowCross(self):
        #tant que la croix n'est pas vérifiée
        while self.checkCrossNonOriente() != True:
            listos=[]
            #liste=self.checkEmplacement()
            for i in range(len(liste)):
                if liste[i][0] != self.whichIsColor('Y'):
                    listos.append(liste[i])
                    print(listos)
            if len(listos) == 3:
                resolution.rotate(['R','U',"2R'","U'",'R',"U'","R'"])
            if len(listos) == 2:
                if cube.getCentralColor(listos[0]) == 'B' and cube.getCentralColor(listos[1]) =='G' or cube.getCentralColor(listos[0]) == 'R' and cube.getCentralColor(listos[1]) == 'O':
                    resolution.rotate(['F','R','U',"R'","U'","F'"])
            else:
                resolution.rotate(['F','U',"R","U'","R'","F'"])

    def rotate(self,liste):
        for i in range(len(liste)):
            cube.rotation(liste[i])
            cube.displayCube()
                    


cube = Cube("YBGGGGGGGRRRWWWOOOYYBGRRWWWOOOYYYYRRWWWOOGRYOBBBBBBBRY")

resolution = Resolution(cube)

cube.displayCube()
        
resolution.solveYellow()

print(resolution.checkCrossNonOriente())
#print(resolution.checkEmplacement())
resolution.resolutionYellowCross()
