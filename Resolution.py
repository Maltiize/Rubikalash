#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.liCross=1,5,7,3
        self.liCmd=[]
        self.liRota='','2',"'"

    def rotation(self,cmd):
        if(cmd==''):
            return 0
        if(len(cmd)!=1 and len(cmd)!=2):
            print("rotation : INVALID ROTATION NAME",cmd)
            return -1
        if(len(cmd)==2 and ( cmd[1]!="2" and cmd[1]!="'")):
            print("rotation : INVALID ROTATION NAME",cmd)
            return -1
        self.liCmd+=cmd
        print("doing :" ,cmd)
        self.cube.rotation(cmd)
        
            
    def getInvRot(self,cmd):
        if(len(cmd)!=1 and len(cmd)!=2):
            print("getInvRot : INVALID ROTATION NAME",cmd)
            return -1
        if(len(cmd)==1):
            return cmd+"'"
        if(cmd[1]=='2'):
            return cmd
        return cmd[0]
        
    # Cette fonction renvoit le type de rotation a éffectué
    # pour que le cube sur la face origin se retrouve sur la face
    # destination
    # la rotation doit etre une composante de la face rotatingF
    def getApproRot(self,origin,destination,rotatingF):
        if(origin == destination):
            return ''
        if(rotatingF==destination):
            return -2
        i=-1
        x=0
        m=cube.getMouv(rotatingF.upper())
        while(x<=6):
            if(origin==m[1][x%4][0]):
                i=0
            if(destination==m[1][x%4][0] and i!=-1):
                return rotatingF.upper()+self.liRota[i-1]
            x+=1
            if(i!=-1):
                i+=1
        return -1

                
    def applyCmd(self,cmd):
        cpt=0
        while(cpt!=len(cmd)):
            tmp=cmd[cpt]
            if(cpt==len(cmd)-1):
                self.rotation(tmp)
                return 0
            if(cmd[cpt+1]=="'" or cmd[cpt+1]=="2"):
                tmp+=cmd[cpt+1]
                self.rotation(tmp)
                cpt+=1
            else :
                self.rotation(tmp)
            tmp=''
            cpt+=1
        return 0
            


        
            
            
            
    

    def theCross(self,nameFace):
        tab=self.checkCross(nameFace)
        print (tab)
        colorcross=cube.getCentralColor(nameFace)
        if(tab[0]==True):
            return 0
        # pour toute les faces qui n'ont pas encore été traitée
        while(len(tab[1])!=0):
            for x in tab[1]:
                print("doing : " ,x)
                cube.printCube()
                # On cherche le cube de couleur "Face à traiter" + " Face où se trouve la croix"
                # on récupere donc la couleur de "Face à traiter" 
                curColor=cube.getCentralColor(x)
                result=cube.findCube([colorcross,curColor])
                print(result)

                # on traite les différents cas en fonction de la position du cube 
                if(result[0][1]==nameFace):
                    if(len(tab[1])==4):
                        self.applyCmd(self.getApproRot(result[1][1],x,result[0][1]))
                        # on actualise la liste des face à traiter au fur à mesure pour eviter de défaire ce qui a déjà été fait
                        tab[1].remove(x)
                    else:
                        self.applyCmd(result[1][1].upper()+self.getApproRot(result[1][1],x,result[0][1])+x.upper()+'2')
                        tab[1].remove(x)

                if(result[0][1]==cube.getFaceInversed(nameFace)):
                    self.applyCmd(self.getApproRot(result[1][1],x,result[0][1])+x.upper()+'2')
                    tab[1].remove(x)
                    
                if(result[0][1]!=cube.getFaceInversed(nameFace) and result[0][1]!=nameFace):
                    rot=self.getApproRot(result[1][1],x,result[0][1])
                    print(rot)

                    
                    if(rot==-1):
                        if(result[1][1]==nameFace or result[1][1]==cube.getFaceInversed(nameFace)):
                            if(len(tab[1]==4)):
                                tmpcmd=result[1][1].upper()
                                self.rotation(tmpcmd)
                                
                                tmppos=cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                                self.rotation(tmpcmd)
                                
                                tmppos=cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                                self.rotation(tmpcmd)
                                
                                tab[1].remove(x)
                            else:
                                tmpcmd=self.getApproRot(result[1][1],cube.getFaceInversed(nameFace),result[0][1])
                                self.rotation(tmpcmd)
                                self.rotation(cube.getFaceInversed(nameFace).upper())
                                tmppos=cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                                
                                faceinter=tmppos[0][1]
                                mouvinter=self.getInvRot(tmpcmd[0])
                                
                                self.cube.rotation(tmpcmd[0])
                                
                                tmppos==cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                                if(faceinter not in tab[1]):
                                    self.rotation(mouvinter)
                                tab[1].remove(x)
                        else:
                            tmpcmd=self.getApproRot(result[0][1],cube.getFaceInversed(nameFace),result[1][1])
                            self.rotation(tmpcmd)
                            
                            faceinter=result[1][1]
                            mouvinter=self.getInvRot(tmpcmd)
                                
                            tmppos=cube.findCube([colorcross,curColor])
                            tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                            self.rotation(tmpcmd)
                                
                            tmppos=cube.findCube([colorcross,curColor])
                            tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                            self.rotation(tmpcmd)

                            if(faceinter not in tab[1]):
                                self.rotation(mouvinter)
                                
                            tab[1].remove(x)

                    

                    elif(rot==-2):
                        print("ok")
                        self.rotation(result[1][1].upper())
                        tmppos=cube.findCube([colorcross,curColor])
                        self.rotation(self.getApproRot(tmppos[1][1],x,tmppos[0][1]))
                        
                        if(result[1][1] not in tab[1] or (result[1][1]==nameFace and len(tab[1]!=4))):
                            self.rotation(self.getInvRot(result[1][1].upper()))
                        self.rotation(self.getApproRot(tmppos[0][1],nameFace,x))
                        tab[1].remove(x)
                            
                            
                        
    
                            
                            

                    else :
                        if(result[0][1] in tab[1]):
                            self.applyCmd(rot+self.getApproRot(result[0][1],nameFace,x)+self.getInvRot(rot))
                            tab[1].remove(x)
                        else :
                            self.applyCmd(rot+self.getApproRot(result[0][1],nameFace,x))
                            tab[1].remove(x)
                            
            print("face finished : " ,x)
            
                
    
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
                
              
        
        
        

#cube = Cube("OOOOOOOOOBBBRRRJJJGGGBBBRRRJJJGGGBBBRRRJJJGGGYYYYYYYYY")
cube = Cube("BWGOWWWWRYYBOBBWOOYGRRRGOBRBORYGWGOBOYOWGYGRRYBGBYYWGR")
cube.printCube()

resol= Resolution(cube)
resol.applyCmd("L'FDUDB2LR'B2D2L'U2L'")
cube.printCube()
resol.theCross('u')
cube.printCube()
