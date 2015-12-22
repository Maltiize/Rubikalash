#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c,face=None):
        self.cube=c
        self.face=face

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
        
        
        


cube = Cube("GGGGGGOGROOBYYGYRRWWWOORYYYBRRWWWOORBYYORRWWWYOGBBBBBB")

resolution = Resolution(cube)

cube.printCube()
        
print(resolution.whichIsColor('Y'))
