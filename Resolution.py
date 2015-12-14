#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.liCross=1,5,7,3,4



    def theCross(self,nameFace):
        while(self.checkCross(nameface)!=True)
        return 0

    def checkCross(self,nameFace):
        tmp=False,[]
        if(cube.checkPattern(nameFace,self.liCross)==False)
            return tmp
        m=cube.getMouv(nameFace.upper())
        for x in m[1]
            colorEdge=cube.getCentralColor(x[0])
            if(cube.checkColorSquare(x[0],colorEdge,x[1][1])==False)
                return False
            
            tmp[1]=tmp[1]+[x[0]]
        tmp[0]=True
        return tmp
            
        
        
        


cube = Cube("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")

        
        
