#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.liCross=1,5,7,3



    def theCross(self,nameFace):
        return 0
    
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

cube.printCube()
print(resol.checkCross('u'))


        
        
