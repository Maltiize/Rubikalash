#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import *
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.liCross=1,5,7,3,4



    def theCross(self,nameFace):
        while(self.checkCross(nameface)!=True):
            return 0

    def checkCross(self,nameFace):
        tmp=False,[]
        if(cube.checkPattern(nameFace,self.liCross)==False):
            return tmp
        m=cube.getMouv(nameFace.upper())
        for x in m[1]:
            colorEdge=cube.getCentralColor(x[0])
            if(cube.checkColorSquare(x[0],colorEdge,x[1][1])==False):
                return False
            
            tmp[1]=tmp[1]+[x[0]]
        tmp[0]=True
        return tmp
#R=L; U=D ; L=R


def rfjaune(c):
    j=c.down
    r=c.left
    b=c.front
    while c.down!=[['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']]:
        if  b[2][0]=='Y' and r[2][0]=='Y' and j[2][0]=='Y':
            c.rotation("L")
            c.rotation("D")
            c.rotation("L'")
            c.rotation("D")
            c.rotation("L")
            c.rotation("D2")
            c.rotation("L'")
                               
        elif r[2][2]=='Y' and b[2][2]=='Y' and j[0][2]=='Y':
            c.rotation("L")
            c.rotation("D2")
            c.rotation("L'")
            c.rotation("D'")
            c.rotation("L")
            c.rotation("D'")
            c.rotation("L'")
            
             
        elif r[2][0]=='Y' and d[2][2]=='Y':
            c.rotation("L")
            c.rotation("D")  
            c.rotation("L'")
            c.rotation("D")
            c.rotation("L")
            c.rotation("U'")
            c.rotation("L'")
            c.rotation("D")
            c.rotation("L")
            c.rotation("D'")
            c.rotation("D'")
            c.rotation("L'")
            
        elif b[2][0]=='Y':
            c.rotation("L")
            c.rotation("D2")
            c.rotation("L2")
            c.rotation("D'")
            c.rotation("L2")
            c.rotation("D'")
            c.rotation("L2")
            c.rotation("D2")
            c.rotation("L")
            
        elif r[2][0]=='Y' and j[2][0]=='Y' and j[2][2]=='Y':
             c.rotation("R'")#"L'U'RD'R'URD"
             c.rotation("D'")
             c.rotation("L")
             c.rotation("U'")
             c.rotation("L'")
             c.rotation("D")
             c.rotation("L")
             c.rotation("U")
        elif  b[2][2]=='Y' and r[2][0]=='Y' and j[0][0]=='Y' and j[2][2]=='Y':
            c.rotation("R'")#"L'URD'R'U'RD"
            c.rotation("D")
            c.rotation("L")
            c.rotation("U'")
            c.rotation("L'")
            c.rotation("D'")
            c.rotation("L")
            c.rotation("U")
        elif b[2][0]=='Y' and b[2][2]=='Y' and j[0][0]=='Y' and j[0][2]=='Y':
            c.rotation("L2") #"R2DR'U2RD'R'U2R'"
            c.rotation("U")
            c.rotation("L'")
            c.rotation("D2")
            c.rotation("L")
            c.rotation("U'")
            c.rotation("L'")
            c.rotation("D2")
            c.rotation("L'")
        else :
            c.rotation("U")
        rfjaune(c)
        
        
cube = Cube("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")
c1=Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGOGYGBYOOYRRBBYYYYYGYR")
c=Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGGOYGBYBGYRRORYOYYYYYB")
c.printCube()
c.rotation("D")
##c.rotation("L")
##c.rotation("D2")
##c.rotation("L'")
##c.rotation("D'")
##c.rotation("L")
##c.rotation("D'")
##c.rotation("L'")
#rfjaune(cub)
c.printCube()

##a=cube.left
##print(a[0][1])
        
        
