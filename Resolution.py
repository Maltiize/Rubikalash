#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.liCross=1,5,7,3
        self.liCmd=[]
        self.liRota='','2',"'"
        
    # Cette fonction renvoit le type de rotation a éffectué
    # pour que le cube sur la face origin se retrouve sur la face
    # destination
    # la rotation doit etre une composante de la face rotatingF
    def getApproRot(self,origin,destination,rotatingF):
        if(origin == destination):
            return -1
        i=-1
        x=0
        m=cube.getMouv(rotatingF.upper())
        while(True):
            if(origin==m[1][x%4][0]):
                print("ok")
                i=0
            if(destination==m[1][x%4][0] and i!=-1):
                return rotatingF.upper()+self.liRota[i-1]
            x+=1
            if(i!=-1):
                i+=1

                

    

    def theCross(self,nameFace):
        tab=self.checkCross(nameFace)
        colorcross=cube.getCentralColor(nameFace)
        cmd=''
        if(tab[0]==True):
            return 0
        for x in tab[1]:
            curColor=cube.getCentralColor(x)
            result=cube.findCube([colorcross,curColor])
            if(result[0][1]=='b'):
                cmd+=self.getApproRot(x,result[1][1],result[0][1])+x+'2'
            
    
    # Cette fonction permet de verifier si la croix a été réalisée sur une face
    # Le nom de la face à vérifier est donné dans nameFace
    # On utilisera la fonction findCube() en limitant les recherches à
    # la face nameFace
    
    # Si un ou des cube n'est/ne sont pas placé(s) au bon endroit
    # La structure rénvoyée sera de la forme
    # [ False , [ nom de la face1 avec un cube mal placé, .....]]
    # si tout est bien placé on aura
    # [ True ,[]]
    
    def checkCross(self,nameFace):
        tmp=[True,[]]
        colorcross=cube.getCentralColor(nameFace)
        m=cube.getMouv(nameFace.upper())
        tabcolor=[]
        for x in m[1]:
            coloredge=cube.getCentralColor(x[0])
            result=cube.findCube([colorcross,coloredge],nameFace)
            
            if(result==-1 or result[1][1]!=x[0]):
                tmp[1]+=[x[0]]
                tmp[0]=False
                
                
        return tmp
                
                        
        
        
        

cube = Cube("OOOOOOOOOBBBRRRJJJGGGBBBRRRJJJGGGBBBRRRJJJGGGYYYYYYYYY")
resol= Resolution(cube)
print(resol.getApproRot('f','l','u'))
