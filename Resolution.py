#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import *




def rfjaune(c):
    j=c.down
    r=c.front
    b=c.right
    if c.down!=[['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']]:
        if  b[2][0]=='Y' and r[2][0]=='Y' and j[2][2]=='Y':
            c.rotation("F")
            c.rotation("D")
            c.rotation("F'")    #testé
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
            c.rotation("L'")   #Testé
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
s
c=Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGYYYYYYYYY")
c2=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGRBYGYBBGYOYRYOYYYRYO")

c3=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOYGRYBBYROBOGBYRYYYBYY")
c4=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGRYRRBBBOOYGYYYYYOYY")

rfjaune(c4)

        
