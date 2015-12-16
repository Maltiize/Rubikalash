#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.liCross=1,5,7,3



    def theCross(self,nameFace):
        return 0

    def checkCross(self,nameFace):
        tmp=[False,[]]
        bol=True
        colorcross=cube.getCentralColor(nameFace)
        m=cube.getMouv(nameFace.upper())
        for idx,x in enumerate(m[1]) :
            colorEdge=cube.getCentralColor(x[0])
            if(cube.checkColorSquare(x[0],colorEdge,x[1][1])==False or cube.checkColorSquare(nameFace,colorcross,self.liCross[idx])):
                bol=False
            
            else :
                tmp[1]=tmp[1]+[x[0]]
        tmp[0]=bol
        return tmp
            
        
        
        

cube = Cube("O0OOOOOOOBBBRRRJJJGGGBBBRRRJJJGGGBBBRRRJJJGGGYYYYYYYYY")
cube.rotation("R")
resol= Resolution(cube)

cube.printCube()
print(resol.checkCross('u'))

        
        
