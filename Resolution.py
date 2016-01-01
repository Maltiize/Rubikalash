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
    r=c.front
    b=c.right
    if c.down!=[['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']]:
        if  b[2][0]=='Y' and r[2][0]=='Y' and j[2][2]=='Y':
            c.rotation("F")
            c.rotation("D")
            c.rotation("F'")
            c.rotation("D")
            c.rotation("F")
            c.rotation("D2")
            c.rotation("F'")
            print("FDF'DFD2F'")
        elif  b[2][2]=='Y' and r[2][0]=='Y' and j[0][2]=='Y' and j[2][0]=='Y':
            c.rotation("F'")
            c.rotation("R")   ##Testé 
            c.rotation("F")
            c.rotation("L'")
            c.rotation("F'")
            c.rotation("R'")
            c.rotation("F")
            c.rotation("L")
            print("F'RFL'F'R'FL")
        elif b[2][0]=='Y' and b[2][2]=='Y' and j[0][0]=='Y' and j[2][0]=='Y':
            c.rotation("F2") #"R2DR'U2RD'R'U2R'"
            c.rotation("U")
            c.rotation("F'")
            c.rotation("D2")    ## testé
            c.rotation("F")
            c.rotation("U'")
            c.rotation("F'")
            c.rotation("D2")
            c.rotation("F'")
            print("F2UF'D2FU'F'D2F'")
        elif r[2][0]=='Y' and j[0][2]=='Y' and j[2][2]=='Y':
            c.rotation("F'")#"L'U'RD'R'URD"
            c.rotation("R'")
            c.rotation("F")
            c.rotation("L'")
            c.rotation("F'")
            c.rotation("R")
            c.rotation("F")
            c.rotation("L")
            print("F'R'FL'F'RFL")
        elif r[2][2]=='Y' and b[2][2]=='Y' and j[0][0]=='Y':
            c.rotation("F")
            c.rotation("D2")
            c.rotation("F'")
            c.rotation("D'")
            c.rotation("F")
            c.rotation("D'")
            c.rotation("F'")
            print("FD2F'D'FD'F'")
             
        elif r[2][0]=='Y' and r[2][2]=='Y':
            c.rotation("F")
            c.rotation("D")  
            c.rotation("F'")    #Testé
            c.rotation("D")
            c.rotation("F")
            c.rotation("D'")
            c.rotation("F'")
            c.rotation("D")
            c.rotation("F")
            c.rotation("D'")
            c.rotation("D'")
            c.rotation("F'")
            print("FDF'DFD'F'DFD'D'F'")
        elif b[2][0]=='Y':
            c.rotation("F")
            c.rotation("D2")
            c.rotation("F2")
            c.rotation("D'")
            c.rotation("F2")
            c.rotation("D'")
            c.rotation("F2")
            c.rotation("D2")
            c.rotation("F")
            print("FD2F2D'F2D'F2D2F")
        
        
        else :
            c.rotation("D")
            rfjaune(c)
    return(c.printCube())
        
   
        
cube = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGOOYBRBGYGROBYYYYYYYR")
c1=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGRBROYBYGOOYYBYYYYYR")
c=Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGYYYYYYYYY")
c2=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGRBYGYBBGYOYRYOYYYRYO")
##c.printCube()
##c.rotation("D")  L=B R=F F=R U=D D=U
#"R'U'RD'R'URD"
#l'URD'R'U'RDx'


##cube.printCube()
##cube.rotation("F'")
##cube.rotation("R")
##cube.rotation("F")
##cube.rotation("L'")
##cube.rotation("F'")
##cube.rotation("R'")
##cube.rotation("F")
##cube.rotation("L")
##cube.printCube()

####
#cube.printCube()
##c.rotation("L")
##c.rotation("D2")
##c.rotation("L'")
##c.rotation("D'")
##c.rotation("L")
##c.rotation("D'")
##c.rotation("L'")
##j=cube.down
##r=cube.front
##b=cube.right
##a=b[2][2]
##z=r[2][0]
##y=j[0][2]
##x=j[2][0]
#print(a,z,y,x)
rfjaune(c2)
#c1.printCube()

##a=cube.left
##print(a[0][1])
##c1.rotation("F2")
###c1.rotation("F")#"R2DR'U2RD'R'U2R'"
##c1.rotation("U")
##c1.rotation("F'")
##c1.rotation("D2")
##c1.rotation("F")
##c1.rotation("U'")
##c1.rotation("F'")
##c1.rotation("D2")
##c1.rotation("F'")
##c1.printCube()
        
