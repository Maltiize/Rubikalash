#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import *
class Resolution:

    def __init__(self,c):
        self.cube=c
        self.mouv = 0
        self.vr = 0
        self.br = 0
        self.bo = 0
        self.vo = 0
        
        
        # liste des indexes servant  à la croix
        self.liCross=1,5,7,3
        self.liCorner=0,2,8,6

        # liste des rotation effectué durant la résolution 
        self.liCmd=''
        self.nbCmd=0
        self.liRota='','2',"'"
        self.listeMouv=[]
        
    # Utiliser cette fonction permet de garder en mémoire les mouvements effectué durant la résolution
    def rotation(self,cmd):
        if(cmd=='' or cmd==' '):
            return 0
        if(len(cmd)!=1 and len(cmd)!=2):
            print("rotation : INVALID ROTATION NAME",cmd)
            return -1
        if(len(cmd)==2 and ( cmd[1]!="2" and cmd[1]!="'")):
            print("rotation : INVALID ROTATION NAME",cmd)
            return -1
        self.liCmd+=cmd
        self.nbCmd+=1
       
        self.cube.rotation(cmd)
        
    # Fonction qui renvoit l'inverse d'une rotation L2 => L2 L=>L' L'=>L        
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
        m=self.cube.getMouv(rotatingF.upper())
        while(x<=6):
            if(origin==m[1][x%4][0]):
                i=0
            if(destination==m[1][x%4][0] and i!=-1):
                return rotatingF.upper()+self.liRota[i-1]
            x+=1
            if(i!=-1):
                i+=1
        return -1

    #  Permet d'effectuer un certain nombre de rotation à la suite 
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
        colorcross=self.cube.getCentralColor(nameFace)
        if(tab[0]==True):
            return 0
        # pour toute les faces qui n'ont pas encore été traitée
        while(len(tab[1])!=0):
            for x in tab[1]:
                #print(tab)
                #cube.displayCube()
                # On cherche le cube de couleur "Face à traiter" + " Face où se trouve la croix"
                # on récupere donc la couleur de "Face à traiter" 
                curColor=self.cube.getCentralColor(x)
                result=self.cube.findCube([colorcross,curColor])

                # on traite les différents cas en fonction de la position du cube

                # cas ou la face de la couleur dont on veut faire la croix (ex blanc) se trouve sur la face de la croix
                if(result[0][1]==nameFace):

                    # si la croix n'a pas été commencé on peut économiser un mouvement
                    if(len(tab[1])==4):
                        self.applyCmd(self.getApproRot(result[1][1],x,result[0][1]))
                    else:
                        self.applyCmd(result[1][1].upper()+'2'+self.getApproRot(result[1][1],x,self.cube.getFaceInversed(nameFace))+x.upper()+'2')

                #cas ou la face de la couleur dont on veut faire la croix se trouve sur la face inverse de la croix
                if(result[0][1]==self.cube.getFaceInversed(nameFace)):
                    self.applyCmd(self.getApproRot(result[1][1],x,result[0][1])+x.upper()+'2')

                # si on se trouve dans aucun des deux
                if(result[0][1]!=self.cube.getFaceInversed(nameFace) and result[0][1]!=nameFace):

                    # on essaye d'approcher le morceau de croix par une seule rotation
                    # le nom de la rotation est donnée par getApproRot si une seule rotation suffit
                    # -1 est renvoyé si ce n'est pas possible ( le pire des cas )
                    # -2 est renvoyé si le la face blanche ( exemple ) se trouve sur la face de destination
                    rot=self.getApproRot(result[1][1],x,result[0][1])
                    if(rot==-1):
                        
                        # si ce n'est pas possible un minimum de trois rotations sera nécessaire
                        
                        # j'ai découpé cette partie en 2 cas à cause de certaines différences de procédure
                        # mais je pense qu'il est pssible de factoriser cette partie du code 
                        if(result[1][1]==nameFace or result[1][1]==self.cube.getFaceInversed(nameFace)):

                            # si la croix n'a pas été commencée
                            if(len(tab[1])==4):
                                tmpcmd=result[1][1].upper()
                                self.rotation(tmpcmd)
                                
                                tmppos=self.cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                                self.rotation(tmpcmd)
                                
                                tmppos=self.cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                                self.rotation(tmpcmd)
                                
                            # si la croix a été commencé on garde en mémoire le mouvement qui perturbe le travail déjà réalisé
                            # on fait ce mouvement à l'inverse une fois la face terminée
                            else:
                                tmpcmd=self.getApproRot(result[1][1],self.cube.getFaceInversed(nameFace),result[0][1])
                                self.rotation(tmpcmd)
                                self.rotation(self.cube.getFaceInversed(nameFace).upper())
                                tmppos=self.cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                                
                                faceinter=tmppos[0][1]
                                mouvinter=self.getInvRot(tmpcmd)
                                
                                self.rotation(tmpcmd)
                                
                                tmppos==self.cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                                self.rotation(tmpcmd)
                                if(faceinter not in tab[1]):
                                    self.rotation(mouvinter)
                        
                        else:
                            tmpcmd=self.getApproRot(result[0][1],self.cube.getFaceInversed(nameFace),result[1][1])
                            self.rotation(tmpcmd)
                            
                            faceinter=result[1][1]
                            mouvinter=self.getInvRot(tmpcmd)
                                
                            tmppos=self.cube.findCube([colorcross,curColor])
                            tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                            self.rotation(tmpcmd)
                                
                            tmppos=self.cube.findCube([colorcross,curColor])
                            tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                            self.rotation(tmpcmd)

                            if(faceinter not in tab[1]):
                                self.rotation(mouvinter)
                                

                    
                    # si la face blanche est sur la face cherchée il faut retourner le cube
                    elif(rot==-2):
                        #print('ok')
                        rr=result[1][1].upper()
                        #if(result[1][1]!=self.cube.getFaceInversed(nameFace) and result[1][1]!=nameFace):
                        #    rr=self.getApproRot(result[0][1],cube.getFaceInversed(nameFace),result[1][1])
                            
                        self.rotation(rr)
                        tmppos=self.cube.findCube([colorcross,curColor])
                        self.rotation(self.getApproRot(tmppos[1][1],x,tmppos[0][1]))
                        
                        if(result[1][1] not in tab[1] or (result[1][1]==nameFace and len(tab[1]!=4))):
                            self.rotation(self.getInvRot(result[1][1].upper()))
                        self.rotation(self.getApproRot(tmppos[0][1],nameFace,x))

                    # cas le plus simple ou il sufft de placer la partie de la croix sur la face ou on fait la croix
                    elif(rot==''):
                        self.rotation(self.getApproRot(result[0][1],nameFace,x))
                            
                        
    
                            
                            
                    # si rot est égal à une rotation 
                    else :
                        if(result[0][1] not in tab[1]):
                            self.applyCmd(rot+self.getApproRot(result[0][1],nameFace,x)+self.getInvRot(rot))
                        else :
                            self.applyCmd(rot+self.getApproRot(result[0][1],nameFace,x))
                            
                tab[1].remove(x)            
            
                
    
    # Cette fonction permet de verifier si la croix a été réalisée sur une face
    # Le nom de la face à vérifier est donné dans nameFace
    # On utilisera la fonction findCube() en limitant les recherches à
    # la face nameFace
    
    # Si un ou des cube n'est/ne sont pas placé(s) au bon endroit
    # La structure rénvoyée sera de la forme
    # [ False , [ nom de la face1 avec un cube mal placé, .....]]
    # si tout est bien placé on aura
    # [ True ,[] ]
    
    def checkCross(self,nameFace):
        tmp=[True,[]]
        colorcross=self.cube.getCentralColor(nameFace)
        m=self.cube.getMouv(nameFace.upper())
        
        for x in m[1]:
            coloredge=self.cube.getCentralColor(x[0])
            result=self.cube.findCube([colorcross,coloredge],nameFace)
            
            if(result==-1 or result[1][1]!=x[0]):
                tmp[1]+=[x[0]]
                tmp[0]=False
                
                
        return tmp

    #verifie si les coin sont fait
    #entré : nom de la face à vérifier
    #sortie : tableau à deux case :
    #premiere case boolean true si les coins sont bien fait false sinon
    #deuxieme case : tableau à trois dimension chaque case represente un coin mal placé avec
    #[[face ou doit etre la couleur de gauche,couleur gauche],[face ou doit etre la couleur de droite,couleur droite]]
    # si tout est bien placé on aura
    # [ True ,[] ]
    def checkCorner(self,nameFace):
        tmp=[True,[]]
        colorcorner=self.cube.getCentralColor(nameFace)
        m=self.cube.getMouv(nameFace.upper())
        for x in range (4):
            colorPrev=self.cube.getCentralColor(m[1][(x+3)%4][0])
            colorNext=self.cube.getCentralColor(m[1][x][0])
            

            result=self.cube.findCube([colorcorner,colorPrev,colorNext],nameFace)
            
            if(result==-1 or result[1][1]!=m[1][(x+3)%4][0] or result[2][1]!=m[1][x][0] ):
                tmp[1]+=[[[m[1][(x+3)%4][0],colorPrev],[m[1][x][0],colorNext]]]
                #[[face ou doit etre la couleur de gauche,couleur gauche],[face ou doit etre la couleur de droite,couleur droite]] 


                tmp[0]=False
                
        return tmp

    #the corner permet de faire les coin d'une face sans prendre en compte se qu'elle fait sur les autre face
    def theCorner(self,nameFace):
        tab=self.checkCorner(nameFace)
        colorCorner=self.cube.getCentralColor(nameFace)
        inv=self.cube.getFaceInversed(nameFace)

        
        if(tab[0]==True):
        #si les coins sont bien placé on ne fait rien
            
            return 0
        else :
            
            for idx, x in enumerate (tab[1]) :
            #pour chaque coins mal placés
                   
                    
                tmp=self.cube.findCube([colorCorner,x[0][1],x[1][1]])
                #on trouve le cube à replacer corectement
                
                
                if (tmp[0][1] != inv):
                #si la couleur de la face à aranger n'est pas à l'opposer de où elle devrait etre (cas les plus simple)
                
                    for i in range (0,2) :
                    #on regarde quelle couleur est donc à l'opposé les rotation change selon celle ci c'est pour ça qu'il y à cette boucle
                        
                        if (tmp[1+i][1] == inv):
                            #la couleur choisi est bien à l'opposé de la face à aranger
                            
                            m=self.cube.getMouv(tmp[2-i][1].upper())
                            if (tmp[0][1] == m[1][1][0]):
                                #si la couleur de la face à aranger est à la droite de la dernière couleur faire c'est rotation
                                self.rotation(self.getApproRot(tmp[0][1],self.cube.getFaceInversed(x[1-i][0]),inv))
                                self.rotation(x[1-i][0].upper())
                                self.rotation(self.getInvRot(inv.upper()))
                                self.rotation(self.getInvRot(x[1-i][0].upper()))
                                
                            else :
                                #si la couleur de la face à aranger est à la gauche de la dernière couleur faire c'est rotation
                                self.rotation(self.getApproRot(tmp[0][1],self.cube.getFaceInversed(x[1-i][0]),inv))

                                self.rotation(self.getInvRot(x[1-i][0].upper()))
                                self.rotation(inv.upper())
                                self.rotation(x[1-i][0].upper())
                else :
                    #si la couleur de la face à aranger est à l'opposer de où elle devrait etre
                    
                    self.rotation(self.getApproRot(tmp[1][1],x[1][0],inv))
                    m=self.cube.getMouv(tmp[1][1].upper())

                    if tmp[2][1] == m[1][1][0] :
                        self.rotation(self.getInvRot(x[0][0].upper()))
                        self.rotation(inv.upper()+"2")
                        self.rotation(x[0][0].upper())
                        self.rotation(inv.upper())             
                        self.rotation(self.getInvRot(x[0][0].upper()))
                        self.rotation(self.getInvRot(inv.upper()))
                        self.rotation(x[0][0].upper())
                    else :
                        self.rotation(self.getInvRot(x[1][0].upper()))
                        self.rotation(inv.upper()+"2")
                        self.rotation(x[1][0].upper())
                        self.rotation(inv.upper())             
                        self.rotation(self.getInvRot(x[1][0].upper()))
                        self.rotation(self.getInvRot(inv.upper()))

                        self.rotation(m[1][1][0].upper())


   
                
                    
        
   

                        self.rotation(x[1][0].upper())
            tab=self.checkCorner(nameFace)
            if(tab[0]==True):
                #on vérifie si les rotation que l'on à fait on suffit
                #c.a.d qu'aucun des cube mal placé est été sur la couronne de la face à modifier
                
                return 0
            else :
                for idx, x in enumerate (tab[1]) :
                    
                    tmp=self.cube.findCube([colorCorner,x[0][1],x[1][1]])
                    #on trouve les cubes manquant 
                    
                    for i in range (3) :
                        if tmp[i][1] == nameFace :
                            #ontrouve la face étant sur la face à modifier
                            
                            mtp=self.cube.getMouv(tmp[(i+1)%3][1].upper())


                            #on va placer le cube pour qu'il soit sur la couronne opposer de là ou il est et qu'il puisse ainsi etre traiter par theCorner

                            if tmp[(i+2)%3][1] == mtp[1][1][0] :
                                self.rotation(tmp[(i+1)%3][1].upper())
                                self.rotation(inv.upper())
                                self.rotation(self.getInvRot(tmp[(i+1)%3][1].upper()))
                            else:
                                self.rotation(tmp[(i+2)%3][1].upper())
                                self.rotation(inv.upper())
                                self.rotation(self.getInvRot(tmp[(i+2)%3][1].upper()))
                    i=(len(tab[1]))        
                self.theCorner(nameFace)
                #on envoie la récursivité et normalement ça doit bien placé le cube deplacer sur la couronne opposer
                        
                                
            
                                
                
                

    def rfjaune(self):
        cube=self.cube
       
        j=cube.down
        r=cube.front
        b=cube.right
        g=cube.left
        o=cube.back
        if not cube.faceFinished('d') :
          
            if r[2][0]==b[2][2] and j[0][2]==b[2][2] and j[2][0]==b[2][2] and j[2][2]!=b[2][2] and j[0][0]!=b[2][2]:
                self.applyCmd("F'RFL'F'R'FL")
                
            elif b[2][2]==b[2][0] and j[0][0]==b[2][0] and j[2][0]==b[2][0]   and j[2][2]!=b[2][0]  and j[0][2]!=b[2][0] :
                self.applyCmd("F2UF'D2FU'F'D2F'")
                
            elif r[2][0]==b[2][0] and j[2][2]==b[2][0]  and j[0][0]!=b[2][0] and j[0][2]!=b[2][0]  and j[2][0]!=b[2][0]:
                self.applyCmd("FDF'DFD2F'")
                
            elif j[0][2]== r[2][0]  and j[2][2]== r[2][0]   and j[2][0]!= r[2][0]  and j[0][0]!= r[2][0] :
                self.applyCmd("F'R'FL'F'RFL")
                

            elif  b[2][2]==r[2][2] and j[0][0]==r[2][2] and j[2][2]!=r[2][2] and j[2][0]!=r[2][2] and j[0][2]!=r[2][2]:
                self.applyCmd("FD2F'D'FD'F'")
                
            elif r[2][2]==r[2][0] and j[0][0]!=r[2][0] and j[0][2]!=r[2][0] and j[2][0]!=r[2][0] and j[2][2]!=r[2][0] :
                self.applyCmd("BD2B2D'B2D'B2D2B")
                
                
            elif j[1][1]==b[2][0] and j[0][0]!=b[2][0] and j[0][2]!=b[2][0] and j[2][0]!=b[2][0] and j[2][2]!=b[2][0] and r[2][0]!=r[2][2] and b[2][0]!=b[2][2] and g[2][0]!=g[2][2] and o[2][0]!=o[2][2] :
                self.applyCmd("FD2F2D'F2D'F2D2F")
                
            else :
                self.rotation('D')       
            self.rfjaune()
            
        else :
            return 1
        
    
############## PARTIE 2ND COURONNE #################################
##    def checkscdcouronne(self):
##        if self.cube.front[1] == ['R','R','R'] and self.cube.right[1] == ['B','B','B'] and self.cube.back[1] == ['O','O','O'] and self.cube.left[1] == ['G','G','G']:
##            return True
##        else:
##            return False
##
##    def deuxcubeinv(self):
##        #si 2 cubes sont inversé sur une 2 face opposées
##        
##        br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##        bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
##
##        #si le cube bleu/rouge inversé avec le vert/rouge
##        if (br[0][1] == 'l' and vr[0][1] == 'r') or (br[0][1] == 'f' and vr[0][1] == 'f') or (br[0][1] == 'l' and vr[0][1] == 'f') or (br[0][1] == 'f' and vr[0][1] == 'r'):
##            self.rotation("F2")
##            self.rotation("D2")
##            self.rotation("F2")
##            self.rotation("D2")
##            self.rotation("F2")
##            self.mouv += 5
##
##        #si le cube bleu/rouge inversé avec le bleu/orange
##        if (br[1][1] == 'b' and bo[1][1] == 'f') or (br[1][1] == 'r' and bo[1][1] == 'r') or (br[1][1] == 'b' and bo[1][1] == 'r') or (br[1][1] == 'r' and bo[1][1] == 'f'):
##            self.rotation("R2")
##            self.rotation("D2")
##            self.rotation("R2")
##            self.rotation("D2")
##            self.rotation("R2")
##            self.mouv += 5
##            
##        #si le cube vert/orange inversé avec le bleu/orange
##        if (vo[0][1] == 'r' and bo[0][1] == 'l') or (vo[0][1] == 'b' and bo[0][1] == 'b') or (vo[0][1] == 'r' and bo[0][1] == 'b') or (vo[0][1] == 'b' and bo[0][1] == 'l'):
##            self.rotation("B2")
##            self.rotation("D2")
##            self.rotation("B2")
##            self.rotation("D2")
##            self.rotation("B2")
##            self.mouv += 5
##
##        #si le cube vert/orange inversé avec le vert/rouge
##        if (vo[1][1] == 'f' and vr[1][1] == 'b') or (vo[1][1] == 'l' and vr[1][1] == 'l') or (vo[1][1] == 'f' and vr[1][1] == 'l') or (vo[1][1] == 'l' and vr[1][1] == 'b'):
##            self.rotation("L2")
##            self.rotation("D2")
##            self.rotation("L2")
##            self.rotation("D2")
##            self.rotation("L2")
##            self.mouv += 5
##        #self.cube.displayCube()
##        #print("2cubeinv")
##
##    def cubeinv(self):
##        #si cube au bon endroit mais couleurs inversées
##        br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##        bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
##
##        if br[0][1] == 'f' and br[1][1] == 'r':
##            self.rotation("F")
##            self.rotation("D")
##            self.rotation("F'")
##            self.rotation("D2")
##            self.rotation("F")
##            self.rotation("D2")
##            self.rotation("F'")
##            self.rotation("D")
##            self.rotation("R'")
##            self.rotation("D'")
##            self.rotation("R")
##            self.mouv += 11
##            #self.cube.displayCube()
##
##        if vr[0][1] == 'f' and vr[1][1] == 'l':
##            self.rotation("L")
##            self.rotation("D")
##            self.rotation("L'")
##            self.rotation("D2")
##            self.rotation("L")
##            self.rotation("D2")
##            self.rotation("L'")
##            self.rotation("D")
##            self.rotation("F'")
##            self.rotation("D'")
##            self.rotation("F")
##            self.mouv += 11
##            #self.cube.displayCube()
##
##        if vo[0][1] == 'b' and vo[1][1] == 'l':
##            self.rotation("B")
##            self.rotation("D")
##            self.rotation("B'")
##            self.rotation("D2")
##            self.rotation("B")
##            self.rotation("D2")
##            self.rotation("B'")
##            self.rotation("D")
##            self.rotation("L'")
##            self.rotation("D'")
##            self.rotation("L")
##            self.mouv += 11
##
##        if bo[0][1] == 'b' and bo[1][1] == 'r':
##            self.rotation("R")
##            self.rotation("D")
##            self.rotation("R'")
##            self.rotation("D2")
##            self.rotation("R")
##            self.rotation("D2")
##            self.rotation("R'")
##            self.rotation("D")
##            self.rotation("B'")
##            self.rotation("D'")
##            self.rotation("B")
##            self.mouv += 11
##            
##    
##    def deuxcouronne(self):
##        
##        #peut creer une fonction maj pour savoir ou sont les 4 cubes ? utile?
##        br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##        bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
##        while not self.checkscdcouronne():
##            while br[0][1] == 'd' or br[1][1] == 'd' or vr[0][1] == 'd' or vr[1][1] == 'd' or vo[0][1] == 'd' or vo[1][1] == 'd' or bo[0][1] == 'd' or bo[1][1] == 'd':
##                self.deuxiemecouronne()
##                br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##                vr = self.cube.findCube(['G', 'R']) #vert/rouge
##                vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##                bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
##
##            if self.checkscdcouronne():
##                break
##            self.cubeinv()
##            self.deuxcubeinv()
##            
##        return self.cube
##    
##    def majcube(self):
##        self.br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        self.vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        self.vo = self.cube.findCube(['G', 'O']) #cube vert/orang
##        self.bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
##
##    def deuxiemecouronne(self):
##    #regarder les 4 coins au dessus et si il n'y a pas de jaune la bouger au bon endroit
##
##            #cube bleu/rouge
##            br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##            #on remet le cube bleu/rouge sur sa face correspondante 
##            if br[0][1] == 'd':  #ici le cube bleu est sur la face down
##                self.mouv += 9
##                #if br[1][1] == 'f':
##                    #ne rien faire car bon endroit
##                if br[1][1] == 'l':
##                    #faire
##                    self.rotation("D")
##                elif br[1][1] == 'b':
##                    #faire
##                    self.rotation("D2")
##                elif br[1][1] == 'r':
##                    #faire
##                    self.rotation("D'")
##                #on doit faire basculer le cube a gauche/ au dessus du rouge
##                self.rotation("D'")
##                self.rotation("R'")
##                self.rotation("D")
##                self.rotation("R")
##                self.rotation("D")
##                self.rotation("F")
##                self.rotation("D'")
##                self.rotation("F'")
##
##                    
##            elif br[1][1] == 'd': #ici le cube rouge est sur la face down
##                if br[0][1] == 'f':
##                    #faire
##                    self.rotation("D")
##                elif br[0][1] == 'l':
##                    #faire
##                    self.rotation("D2")
##                elif br[0][1] == 'b':
##                    #faire
##                    self.rotation("D'")
##                #if a[0][1] == 'r':
##                    #ne rien faire
##                #on doit faire basculer le cube a droite
##                self.rotation("D")
##                self.rotation("F")
##                self.rotation("D'")
##                self.rotation("F'")
##                self.rotation("D'")
##                self.rotation("R'")
##                self.rotation("D")
##                self.rotation("R")
##
##            
##            #cube vert/rouge
##            vr = self.cube.findCube(['G', 'R']) #cube vert/rouge
##            #on remet le cube vert/rouge sur sa face correspondante
##            if vr[0][1] == 'd':  #ici le cube vert est sur la face down
##
##                self.mouv += 9
##                
##                if vr[1][1] == 'l':
##                    #faire
##                    self.rotation("D")
##                elif vr[1][1] == 'b':
##                    #faire
##                    self.rotation("D2")
##                elif vr[1][1] == 'r':
##                    #faire
##                    self.rotation("D'")
##                #on doit faire basculer le cube a droite
##                self.rotation("D")
##                self.rotation("L")
##                self.rotation("D'")
##                self.rotation("L'")
##                self.rotation("D'")
##                self.rotation("F'")
##                self.rotation("D")
##                self.rotation("F")
##
##            elif vr[1][1] == 'd': #ici le cube rouge est sur la face down
##                if vr[0][1] == 'f':
##                    #faire
##                    self.rotation("D'")
##                elif vr[0][1] == 'r':
##                    #faire
##                    self.rotation("D2")
##                elif vr[0][1] == 'b':
##                    #faire
##                    self.rotation("D")
##                #elif a[0][1] == 'r':
##                    #ne rien faire
##                #on doit faire basculer le cube a gauche
##                self.rotation("D'")
##                self.rotation("F'")
##                self.rotation("D")
##                self.rotation("F")
##                self.rotation("D")
##                self.rotation("L")
##                self.rotation("D'")
##                self.rotation("L'")
##                self.cube.displayCube()
##
##            #cube vert/orange
##            vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##                #on remet le cube vert/orange sur sa face correspondante 
##            if vo[0][1] == 'd':  #ici le cube vert est sur la face down
##                self.mouv += 8
##                if vo[1][1] == 'f':
##                     #faire
##                    self.rotation("D2")
##                elif vo[1][1] == 'l':
##                    #faire
##                    self.rotation("D'")
##                #if vr[1][1] == 'b':
##                   #ne rien faire car bon endroit
##                elif vo[1][1] == 'r':
##                    #faire
##                    self.rotation("D")
##                #on doit faire basculer le cube a gauche
##                self.rotation("D'")
##                self.rotation("L'")
##                self.rotation("D")
##                self.rotation("L")
##                self.rotation("D")
##                self.rotation("B")
##                self.rotation("D'")
##                self.rotation("B'")
##                self.cube.displayCube()
##                
##            elif vo[1][1] == 'd': #ici le cube orange est sur la face down
##                if vo[0][1] == 'f':
##                    #faire
##                    self.rotation("D'")
##                elif vo[0][1] == 'r':
##                    #faire
##                    self.rotation("D2")
##                elif vo[0][1] == 'b':
##                    #faire
##                    self.rotation("D")
##                #if vo[0][1] == 'r':
##                    #ne rien faire
##                #on doit faire basculer le cube a droite
##                self.rotation("D")
##                self.rotation("B")
##                self.rotation("D'")
##                self.rotation("B'")
##                self.rotation("D'")
##                self.rotation("L'")
##                self.rotation("D")
##                self.rotation("L")
##                self.cube.displayCube()
##
##            #cube bleu/orange
##            bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
##            #on remet le cube bleu/orange sur sa face correspondante 
##            if bo[0][1] == 'd':  #ici le cube bleu est sur la face down
##                self.mouv += 8
##                if bo[1][1] == 'f':
##                     #faire
##                    self.rotation("D2")
##                elif bo[1][1] == 'l':
##                    #faire
##                    self.rotation("D'")
##                #if bo[1][1] == 'b':
##                   #ne rien faire car bon endroit
##                elif bo[1][1] == 'r':
##                    #faire
##                    self.rotation("D")
##                    #on doit faire basculer le cube a droite
##                self.rotation("D")
##                self.rotation("R")
##                self.rotation("D'")
##                self.rotation("R'")
##                self.rotation("D'")
##                self.rotation("B'")
##                self.rotation("D")
##                self.rotation("B")
##                self.cube.displayCube()
##            
##            elif bo[1][1] == 'd': #ici le cube orange est sur la face down
##                if bo[0][1] == 'f':
##                    #faire
##                    self.rotation("D")
##                #if bo[0][1] == 'r':
##                    #ne rien faire
##                elif bo[0][1] == 'b':
##                    #faire
##                    self.rotation("D'")
##                elif bo[0][1] == 'l':
##                    #faire
##                    self.rotation("D2")
##                #on doit faire basculer le cube a gauche
##                self.rotation("D'")
##                self.rotation("B'")
##                self.rotation("D")
##                self.rotation("B")
##                self.rotation("D")
##                self.rotation("R")
##                self.rotation("D'")
##                self.rotation("R'")
##                self.cube.displayCube()

    def checkscdcouronne(self):
        if self.cube.front[1] == ['R','R','R'] and self.cube.right[1] == ['B','B','B'] and self.cube.back[1] == ['O','O','O'] and self.cube.left[1] == ['G','G','G']:
            return True
        else:
            return False

    def deuxcubeinv(self):
        #si 2 cubes sont inversé sur une 2 face opposées
        a = 0
##        br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##        bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
        self.majcube()

        #si le cube bleu/rouge inversé avec le vert/rouge
        if (self.br[0][1] == 'l' and self.vr[0][1] == 'r') or (self.br[0][1] == 'f' and self.vr[0][1] == 'f') or (self.br[0][1] == 'l' and self.vr[0][1] == 'f') or (self.br[0][1] == 'f' and self.vr[0][1] == 'r'):
            a = "F"
        #si le cube bleu/rouge inversé avec le bleu/orange
        elif (self.br[1][1] == 'b' and self.bo[1][1] == 'f') or (self.br[1][1] == 'r' and self.bo[1][1] == 'r') or (self.br[1][1] == 'b' and self.bo[1][1] == 'r') or (self.br[1][1] == 'r' and self.bo[1][1] == 'f'):
            a = "R"
        #si le cube vert/orange inversé avec le bleu/orange
        elif (self.vo[0][1] == 'r' and self.bo[0][1] == 'l') or (self.vo[0][1] == 'b' and self.bo[0][1] == 'b') or (self.vo[0][1] == 'r' and self.bo[0][1] == 'b') or (self.vo[0][1] == 'b' and self.bo[0][1] == 'l'):
            a = "B"
        #si le cube vert/orange inversé avec le vert/rouge
        elif (self.vo[1][1] == 'f' and self.vr[1][1] == 'b') or (self.vo[1][1] == 'l' and self.vr[1][1] == 'l') or (self.vo[1][1] == 'f' and self.vr[1][1] == 'l') or (self.vo[1][1] == 'l' and self.vr[1][1] == 'b'):
            a = "L"
        if a!= 0:
            self.cube.rotation(str(a)+str(2))
            self.cube.rotation("D2")
            self.cube.rotation(str(a)+str(2))
            self.cube.rotation("D2")
            self.cube.rotation(str(a)+str(2))

##        #si le cube bleu/rouge inversé avec le vert/rouge
##        if br[0][1] == 'l' and vr[0][1] == 'r':
##            self.cube.rotation("F2")
##            self.cube.rotation("D2")
##            self.cube.rotation("F2")
##            self.cube.rotation("D2")
##            self.cube.rotation("F2")
##            self.mouv += 5
##
##        #si le cube bleu/rouge inversé avec le bleu/orange
##        if br[1][1] == 'b' and bo[1][1] == 'f':
##            self.cube.rotation("R2")
##            self.cube.rotation("D2")
##            self.cube.rotation("R2")
##            self.cube.rotation("D2")
##            self.cube.rotation("R2")
##            self.mouv += 5
##            
##        #si le cube vert/orange inversé avec le bleu/orange
##        if vo[0][1] == 'r' and bo[0][1] == 'l':
##            self.cube.rotation("B2")
##            self.cube.rotation("D2")
##            self.cube.rotation("B2")
##            self.cube.rotation("D2")
##            self.cube.rotation("B2")
##            self.mouv += 5
##
##        #si le cube vert/orange inversé avec le vert/rouge
##        if vo[1][1] == 'f' and vr[1][1] == 'b':
##            self.cube.rotation("L2")
##            self.cube.rotation("D2")
##            self.cube.rotation("L2")
##            self.cube.rotation("D2")
##            self.cube.rotation("L2")
        self.mouv += 5
        self.cube.displayCube()
        print("2cubeinv")

    def cubeinv(self):
        #si cube au bon endroit mais couleurs inversées
##        br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##        bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
        self.majcube()
        a = 0
        b = 0
        
        if self.br[0][1] == 'f' and self.br[1][1] == 'r':
            a = "F"
            b = "R"
        if self.vr[0][1] == 'f' and self.vr[1][1] == 'l':
            a = "L"
            b = "F"
        if self.vo[0][1] == 'b' and self.vo[1][1] == 'l':
            a = "B"
            b = "L"
        if self.bo[0][1] == 'b' and self.bo[1][1] == 'r':
            a = "R"
            b = "B"
        if a != 0:
            self.cube.rotation(str(a))
            self.cube.rotation("D")
            self.cube.rotation(str(a)+"'")
            self.cube.rotation("D2")
            self.cube.rotation(str(a))
            self.cube.rotation("D2")
            self.cube.rotation(str(a)+"'")
            self.cube.rotation("D")
            self.cube.rotation(str(b)+"'")
            self.cube.rotation("D'")
            self.cube.rotation(str(b))
            self.mouv += 11
            self.cube.displayCube()

##        if br[0][1] == 'f' and br[1][1] == 'r':
##            self.cube.rotation("F")
##            self.cube.rotation("D")
##            self.cube.rotation("F'")
##            self.cube.rotation("D2")
##            self.cube.rotation("F")
##            self.cube.rotation("D2")
##            self.cube.rotation("F'")
##            self.cube.rotation("D")
##            self.cube.rotation("R'")
##            self.cube.rotation("D'")
##            self.cube.rotation("R")
##            self.mouv += 11
##            self.cube.displayCube()
##
##        if vr[0][1] == 'f' and vr[1][1] == 'l':
##            self.cube.rotation("L")
##            self.cube.rotation("D")
##            self.cube.rotation("L'")
##            self.cube.rotation("D2")
##            self.cube.rotation("L")
##            self.cube.rotation("D2")
##            self.cube.rotation("L'")
##            self.cube.rotation("D")
##            self.cube.rotation("F'")
##            self.cube.rotation("D'")
##            self.cube.rotation("F")
##            self.mouv += 11
##            self.cube.displayCube()
##
##        if vo[0][1] == 'b' and vo[1][1] == 'l':
##            self.cube.rotation("B")
##            self.cube.rotation("D")
##            self.cube.rotation("B'")
##            self.cube.rotation("D2")
##            self.cube.rotation("B")
##            self.cube.rotation("D2")
##            self.cube.rotation("B'")
##            self.cube.rotation("D")
##            self.cube.rotation("L'")
##            self.cube.rotation("D'")
##            self.cube.rotation("L")
##            self.mouv += 11
##            self.cube.displayCube()
##
##        if bo[0][1] == 'b' and bo[1][1] == 'r':
##            self.cube.rotation("R")
##            self.cube.rotation("D")
##            self.cube.rotation("R'")
##            self.cube.rotation("D2")
##            self.cube.rotation("R")
##            self.cube.rotation("D2")
##            self.cube.rotation("R'")
##            self.cube.rotation("D")
##            self.cube.rotation("B'")
##            self.cube.rotation("D'")
##            self.cube.rotation("B")
##            self.mouv += 11
##            self.cube.displayCube()
            
        print("cubeinv")
    
    def deuxcouronne(self):
        
        #peut creer une fonction maj pour savoir ou sont les 4 cubes ? utile?
##        br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.cube.findCube(['G', 'R']) #vert/rouge
##        vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##        bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
        self.majcube()
        while not self.checkscdcouronne():
            while self.br[0][1] == 'd' or self.br[1][1] == 'd' or self.vr[0][1] == 'd' or self.vr[1][1] == 'd' or self.vo[0][1] == 'd' or self.vo[1][1] == 'd' or self.bo[0][1] == 'd' or self.bo[1][1] == 'd':
                self.deuxiemecouronne()
                self.majcube()
##                br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
##                vr = self.cube.findCube(['G', 'R']) #vert/rouge
##                vo = self.cube.findCube(['G', 'O']) #cube vert/orange
##                bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
            self.cube.displayCube()
            if self.checkscdcouronne():
                break
            self.cubeinv()
            if self.checkscdcouronne():
                break
            self.cube.displayCube()
            self.deuxcubeinv()
            self.cube.displayCube()

        print(self.mouv)
        return self.cube
    
    def majcube(self):
        self.br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
        self.vr = self.cube.findCube(['G', 'R']) #vert/rouge
        self.vo = self.cube.findCube(['G', 'O']) #cube vert/orang
        self.bo = self.cube.findCube(['B', 'O']) #cube bleu/orange

    def deuxiemecouronne(self):
    #regarder les 4 coins au dessus et si il n'y a pas de jaune la bouger au bon endroit

            #cube bleu/rouge
            br = self.cube.findCube(['B', 'R']) #cube bleu/rouge
            #on remet le cube bleu/rouge sur sa face correspondante 
            if br[0][1] == 'd':  #ici le cube bleu est sur la face down
                if br[1][1] == 'l':
                    #faire
                    self.cube.rotation("D")
                elif br[1][1] == 'b':
                    #faire
                    self.cube.rotation("D2")
                elif br[1][1] == 'r':
                    #faire
                    self.cube.rotation("D'")
                    self.cube.printCube()
                #on doit faire basculer le cube a gauche/ au dessus du rouge
                self.cube.rotation("D'")
                self.cube.rotation("R'")
                self.cube.rotation("D")
                self.cube.rotation("R")
                self.cube.rotation("D")
                self.cube.rotation("F")
                self.cube.rotation("D'")
                self.cube.rotation("F'")
                self.cube.displayCube()

                    
            elif br[1][1] == 'd': #ici le cube rouge est sur la face down
                if br[0][1] == 'f':
                    #faire
                    self.cube.rotation("D")
                elif br[0][1] == 'l':
                    #faire
                    self.cube.rotation("D2")
                elif br[0][1] == 'b':
                    #faire
                    self.cube.rotation("D'")
                #if a[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a droite
                self.cube.rotation("D")
                self.cube.rotation("F")
                self.cube.rotation("D'")
                self.cube.rotation("F'")
                self.cube.rotation("D'")
                self.cube.rotation("R'")
                self.cube.rotation("D")
                self.cube.rotation("R")
                self.cube.displayCube()

            
            #cube vert/rouge
            vr = self.cube.findCube(['G', 'R']) #cube vert/rouge
            #on remet le cube vert/rouge sur sa face correspondante
            if vr[0][1] == 'd':  #ici le cube vert est sur la face down

                self.mouv += 9
                
                if vr[1][1] == 'l':
                    #faire
                    self.cube.rotation("D")
                elif vr[1][1] == 'b':
                    #faire
                    self.cube.rotation("D2")
                elif vr[1][1] == 'r':
                    #faire
                    self.cube.rotation("D'")
                #on doit faire basculer le cube a droite
                self.cube.rotation("D")
                self.cube.rotation("L")
                self.cube.rotation("D'")
                self.cube.rotation("L'")
                self.cube.rotation("D'")
                self.cube.rotation("F'")
                self.cube.rotation("D")
                self.cube.rotation("F")
                self.cube.displayCube()
            elif vr[1][1] == 'd': #ici le cube rouge est sur la face down
                if vr[0][1] == 'f':
                    #faire
                    self.cube.rotation("D'")
                elif vr[0][1] == 'r':
                    #faire
                    self.cube.rotation("D2")
                elif vr[0][1] == 'b':
                    #faire
                    self.cube.rotation("D")
                #elif a[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a gauche
                self.cube.rotation("D'")
                self.cube.rotation("F'")
                self.cube.rotation("D")
                self.cube.rotation("F")
                self.cube.rotation("D")
                self.cube.rotation("L")
                self.cube.rotation("D'")
                self.cube.rotation("L'")
                self.cube.displayCube()

            #cube vert/orange
            vo = self.cube.findCube(['G', 'O']) #cube vert/orange
                #on remet le cube vert/orange sur sa face correspondante 
            if vo[0][1] == 'd':  #ici le cube vert est sur la face down
                self.mouv += 8
                if vo[1][1] == 'f':
                     #faire
                    self.cube.rotation("D2")
                elif vo[1][1] == 'l':
                    #faire
                    self.cube.rotation("D'")
                #if vr[1][1] == 'b':
                   #ne rien faire car bon endroit
                elif vo[1][1] == 'r':
                    #faire
                    self.cube.rotation("D")
                #on doit faire basculer le cube a gauche
                self.cube.rotation("D'")
                self.cube.rotation("L'")
                self.cube.rotation("D")
                self.cube.rotation("L")
                self.cube.rotation("D")
                self.cube.rotation("B")
                self.cube.rotation("D'")
                self.cube.rotation("B'")
                self.cube.displayCube()
                
            elif vo[1][1] == 'd': #ici le cube orange est sur la face down
                if vo[0][1] == 'f':
                    #faire
                    self.cube.rotation("D'")
                elif vo[0][1] == 'r':
                    #faire
                    self.cube.rotation("D2")
                elif vo[0][1] == 'b':
                    #faire
                    self.cube.rotation("D")
                #if vo[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a droite
                self.cube.rotation("D")
                self.cube.rotation("B")
                self.cube.rotation("D'")
                self.cube.rotation("B'")
                self.cube.rotation("D'")
                self.cube.rotation("L'")
                self.cube.rotation("D")
                self.cube.rotation("L")
                self.cube.displayCube()

            #cube bleu/orange
            bo = self.cube.findCube(['B', 'O']) #cube bleu/orange
            #on remet le cube bleu/orange sur sa face correspondante 
            if bo[0][1] == 'd':  #ici le cube bleu est sur la face down
                self.mouv += 8
                if bo[1][1] == 'f':
                     #faire
                    self.cube.rotation("D2")
                elif bo[1][1] == 'l':
                    #faire
                    self.cube.rotation("D'")
                #if bo[1][1] == 'b':
                   #ne rien faire car bon endroit
                elif bo[1][1] == 'r':
                    #faire
                    self.cube.rotation("D")
                    #on doit faire basculer le cube a droite
                self.cube.rotation("D")
                self.cube.rotation("R")
                self.cube.rotation("D'")
                self.cube.rotation("R'")
                self.cube.rotation("D'")
                self.cube.rotation("B'")
                self.cube.rotation("D")
                self.cube.rotation("B")
                self.cube.displayCube()
            
            elif bo[1][1] == 'd': #ici le cube orange est sur la face down
                if bo[0][1] == 'f':
                    #faire
                    self.cube.rotation("D")
                #if bo[0][1] == 'r':
                    #ne rien faire
                elif bo[0][1] == 'b':
                    #faire
                    self.cube.rotation("D'")
                elif bo[0][1] == 'l':
                    #faire
                    self.cube.rotation("D2")
                #on doit faire basculer le cube a gauche
                self.cube.rotation("D'")
                self.cube.rotation("B'")
                self.cube.rotation("D")
                self.cube.rotation("B")
                self.cube.rotation("D")
                self.cube.rotation("R")
                self.cube.rotation("D'")
                self.cube.rotation("R'")
                self.cube.displayCube()
            print("2couronne")   

############## PARTIE 2ND COURONNE #################################
        

############## PARTIE CROIX JAUNE #################################

#Fonction qui renvoie quelle face est de la couleur recherchée (jaune pour mon algo ("Y"))
#On compare avec la couleur de chaque face en [1][1] et donc au milieu
    def whichIsColor(self,color):

        colorF = self.cube.up[1][1]  
        if colorF == color :
            return "u"

        colorF = self.cube.down[1][1]
        if colorF == color :
            return "d"

        colorF = self.cube.right[1][1]
        if colorF == color :
            return "r"

        colorF = self.cube.left[1][1]
        if colorF == color :
            return "l"

        colorF = self.cube.back[1][1]
        if colorF == color :
            return "b"

        colorF = self.cube.front[1][1]
        if colorF == color:
            return "f"


            
#Fonction qui vérifie si la croix non orienté est vérifiée
    def checkCrossNonOriente(self):
        posColor = self.whichIsColor('Y')   #on trouve la position de la face jaune
        listeColors=['G','R','B','O']       #c'est la liste des couleurs composants les aretes avec une face jaune
        for i in range(len(listeColors)):   #on parcout la liste des couleurs
            pos = self.cube.findCube(['Y',listeColors[i][0][0]]) #on récupère la position des aretes
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
            #plutot que leur couleur ; on va mettre la position de la couleur
            listos=[]
            pos = self.cube.findCube(['Y',listeColors[i][0][0]])
            listos.append(pos[0][1])
            listos.append(pos[1][1])
            liste.append(listos)    
            #liste contenant les listes des arêtes avec (1) : sur quelle face se trouve la partie Y de l'arete et (2) : de quelle couleur est l'autre partie
        return liste

#fonction qui renvoie la position des 
    
    def opposite(self,face):
        if face == 'u':
            return 'D'
        elif face == 'd':
            return 'U'
        elif face == 'r':
            return 'L'
        elif face == 'l':
            return 'R'
        elif face == 'f':
            return 'B'
        elif face == 'b':
            return 'F'


#fonction qui renvoie les deux aretes dans le bon ordre pour le cas 2 de la croix jaune
    def case2(self,pos1,pos2):
    
        posY = self.whichIsColor('Y')
        index=['u','d','f','b','r','l'] 
        liste=[['L','B','R','F'],['R','B','L','F'],['L','U','R','D'],['R','U','L','D'],['F','U','B','D'],['B','U','F','D']] #chaque liste correspond a un index respectif

        ind=index.index(posY)
        a=liste[ind].index(pos1.upper())
        b=liste[ind].index(pos2.upper())
        if a > b:
            if liste[ind][(a+1)%4] != pos2.upper() or a < 3:
                return [pos1,pos2]
            else:
                return [pos2,pos1]
        else:
            if liste[ind][(b+1)%4] != pos1.upper() or b <3:
                return [pos2,pos1]
            else:
                return [pos1,pos2]

#fonction qui renvoie les faces a utiliser pour le cas 1 de la résolution croix jaune
    def case1(self):
        posY=self.whichIsColor('Y')
        index=['u','d','f','b','r','l']
        liste=[['F','U','R'],['F','D','L'],['D','F','R'],['U','B','R'],['F','R','D'],['F','L','U']]
        return liste[index.index(posY)]

    def case3(self,pos1):

        posY=self.whichIsColor('Y')
        index=['u','d','f','b','r','l']
        liste=[['L','B','R','F'],['R','B','L','F'],['L','U','R','D'],['R','U','L','D'],['F','U','B','D'],['B','U','F','D']]
        listeDroite=[['F','R','B','L'],['F','L','B','R'],['R','U','L','D'],['R','D','L','U'],['D','B','U','F'],['D','F','U','B']]
        ind = index.index(posY)
        ind1 = liste[ind].index(pos1.upper())
        ind2 = listeDroite[ind].index(liste[ind][(ind1+1)%4])
        return [liste[ind][(ind1+1)%4] , listeDroite[ind][(ind2+1)%4] , posY.upper()]


        # F R U Ri Ui Fi

    def resolutionCroixJaune(self):
        posY=self.whichIsColor('Y')

        #adj : Y en b u f 
        dicAdj = [['u','r'],['l','u'],['r','d'],['d','l'],['l','f'],['b','l'],['r','b'],['f','r']]
        dicOp = [['u','d'],['l','r']]
        #tant que la croix jaune n'est pas vérifiée

        while self.checkCrossNonOriente() != True:

            
            pos=None #position up ou down
            adj=False
            #on récupère la position des aretes jaunes qui sont sur la face jaune
            liste=self.checkEmplacement()   
            #liste contenant le placement des aretes dont la partie jaune est déjà sur la face jaune
            listeAretes=[]
            listeCeTour=[]


            #on récupère la position des aretes dont la partie jaune est sur la face jaune
            for i in range(len(liste)):
                #si la partie jaune de l'arete est sur la face jaune
                if liste[i][0] == self.whichIsColor("Y"):
                    #alors on récupère l'emplacement de la partie de l'autre couleur
                    listeAretes.append(liste[i][1])
            #si il n'y a que la case jaune du milieu

            if len(listeAretes) == 0 or len(listeAretes) == 3 or len(listeAretes)==1:

                tmp = self.case1()
                listeCeTour.append(tmp[0])
                listeCeTour.append(tmp[1])
                listeCeTour.append(tmp[2])      #a check
                listeCeTour.append(tmp[1]+"'")
                listeCeTour.append(tmp[2]+"'")
                listeCeTour.append(tmp[0]+"'")
                
                    

                    # D F R Fi Ri Di
                    #on prend n'import lequel balek

                # F U R Ui Ri Fi
            if len(listeAretes) == 2:

                #Cas si les aretes sont 'adjacentes'
                for i in range(len(dicAdj)):

                    if listeAretes[0] in dicAdj[i] and listeAretes[1] in dicAdj[i]: #On vérifie qu'on est dans le cas de l'adjacence
                        adj = True

                if adj == True :

                    tmp = self.case2(listeAretes[0],listeAretes[1])   #on récupère les aretes dans le bon ordre pour notre algorithme
                    #on applique les rotations par rapport aux bonnes faces du coup
                    listeCeTour.append(self.opposite(tmp[0]))
                    listeCeTour.append(posY.upper())
                    listeCeTour.append(self.opposite(tmp[1]))
                    listeCeTour.append(posY.upper() + "'")
                    listeCeTour.append(self.opposite(tmp[1])+"'")
                    listeCeTour.append(self.opposite(tmp[0])+"'")

                        # F U R Ui Ri Fi
                else :
                    tmp = self.case3(listeAretes[0])
                    
                    listeCeTour.append(tmp[0])
                    listeCeTour.append(tmp[1])
                    listeCeTour.append(tmp[2])
                    listeCeTour.append(tmp[1]+"'")     #ERREURS
                    listeCeTour.append(tmp[2]+"'")
                    listeCeTour.append(tmp[0]+"'")

                        # F R U Ri Ui Fi
            self.listeMouv.append(listeCeTour)
            self.rotate(listeCeTour)



    def rotate(self,liste):
        for i in range(len(liste)):
            self.rotation(liste[i])

############## PARTIE CROIX JAUNE #################################            

## ETAPE 6 & 7 : FIN ##
    
    
    def lastStep(self) :
        if self.cube.cubeFinished() == False :
            # Récupération des différentes variables nécéssaire à la résolution
            faceJaune = self.getFaceJaune()
            tabParc = self.getTabParc(faceJaune)
            tabLiFaceChange = self.getTabLiFaceChange(faceJaune)

            # Résolution des coins et des arrêtes
            self.putCornerLastFace(faceJaune, tabParc, tabLiFaceChange)
            
        if self.cube.cubeFinished() == False :
            self.putAreteLastFace(faceJaune, tabParc, tabLiFaceChange)

    def getFaceJaune(self) :
        faceBlanche = ''
        faceJaune = ''

        # On trouve les deux face "finies" pour savoir quelles faces modifier par la suite
        for face in self.cube.liFace :
            faceBlanche = face
            faceJaune = self.cube.getFaceInversed(face)
            if self.cube.faceFinished(faceBlanche) and self.cube.faceFinished(faceJaune):
                break

        # Si les deux faces sont inversé
        faceTest = self.cube.getFace(self.cube.liFace[(self.cube.liFace.index(faceJaune)+2)%6])
        if (faceJaune == 'u' and faceTest[0][0] == faceTest[0][1] == faceTest[0][2]) or (faceJaune == 'f' and faceTest[0][0] == faceTest[1][0] == faceTest[2][0]) or ((faceJaune == 'd' or faceJaune == 'b') and faceTest[2][0] == faceTest[2][1] == faceTest[2][2]) or ((faceJaune == 'l' or faceJaune == 'r') and faceTest[0][2] == faceTest[1][2] == faceTest[2][2])  :
            temp = faceJaune
            faceJaune = faceBlanche
            faceBlanche = temp

        return faceJaune
        
    def getTabParc(self, faceJaune) :
        # TabParc va nous servir à parcourir le cube pour trouver les cubes inversés en fonction des 4 faces à finir
        if faceJaune == 'u' :
            tabParc = [0,'x']
            
        elif faceJaune == 'd' :
            tabParc = [2,'x']
            
        elif faceJaune == 'l' or 'f' :
            tabParc = ['x',0]
            
        elif faceJaune == 'r' or 'b' :
            tabParc = ['x',2]

        return tabParc

    def getTabLiFaceChange(self, faceJaune) :
        # Ce tableau contient les face non finies, il va nous permettre de nous afranchir des couleurs
        # car les mouvements à faire pour résoudre le cube sont symétrique
        if faceJaune == 'd' or faceJaune == 'u' :
            return ['l','f','r','b']
        elif faceJaune == 'l' or faceJaune == 'r' :
            return ['f','u','b','d']
        else :
            return ['d','r','u','l']
        
    def putCornerLastFace(self, faceJaune, tabParc, tabLiFaceChange) :
       
        tabMiniReplace = []
        
        #A ce niveau de résolution il est possible de bien placer deux coins,
        #donc tant que je n'obtient pas seulement deux coins mal placés :
        while len(tabMiniReplace) != 4 :
            tabMiniReplace = []
            for i in range(4) :
                faceEnCours = self.cube.getFace(tabLiFaceChange[i])
                if tabParc[0] != 'x' :
                    if faceEnCours[tabParc[0]][0] != faceEnCours[(tabParc[0]+1)%2][0] :
                        tabMiniReplace.append([i,tabParc[0],0])
                    if faceEnCours[tabParc[0]][2] != faceEnCours[(tabParc[0]+1)%2][2] :
                        tabMiniReplace.append([i,tabParc[0],2])
                else :
                    if faceEnCours[0][tabParc[1]] != faceEnCours[0][(tabParc[1]+1)%2] :
                        tabMiniReplace.append([i,0,tabParc[1]])
                    if faceEnCours[2][tabParc[1]] != faceEnCours[2][(tabParc[1]+1)%2] :
                        tabMiniReplace.append([i,2,tabParc[1]])
            #(suite) je tourne la face "Jaune" (non résolue)
            if len(tabMiniReplace) != 4 :
                self.rotation(faceJaune.upper())

        # cas 1 : les deux cubes à intervertir sont sur la même face
        # cas 2 : les deux cubes à intervertir sont des coins opposés
        cas1 = False
        for i in range(4):
            if tabMiniReplace[i][0] == tabMiniReplace[(i+1)%4][0] or tabMiniReplace[i][0] == tabMiniReplace[(i+2)%4][0] or tabMiniReplace[i][0] == tabMiniReplace[(i+3)%4][0] :
                cas1 = True
                faceChange = tabMiniReplace[i][0]
                break

        if faceJaune == 'd' or faceJaune == 'r' or faceJaune == 'b' :
            sensRotation = 1
        else :
            sensRotation = -1

#CAS 1 : 
        if cas1 :
            self.rotation(tabLiFaceChange[faceChange].upper())
            self.rotation(faceJaune.upper())
            self.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            self.rotation(faceJaune.upper()+'\'')
            self.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            self.rotation(tabLiFaceChange[(faceChange+(1*sensRotation))%4].upper())
            self.rotation(tabLiFaceChange[faceChange].upper()+'2')
            self.rotation(faceJaune.upper()+'\'')
            self.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            self.rotation(faceJaune.upper()+'\'')
            self.rotation(tabLiFaceChange[faceChange].upper())
            self.rotation(faceJaune.upper())
            self.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            self.rotation(tabLiFaceChange[(faceChange+(1*sensRotation))%4].upper()+'\'')
        else :
            for i in range(4):
                if tabParc[0] != 'x' :
                    if tabMiniReplace[i][2] == 2 - tabParc[0] :
                        faceChange = tabMiniReplace[i][0]
                        break
                else : 
                    if tabMiniReplace[i][1] == tabParc[1] :
                        faceChange = tabMiniReplace[i][0]
                        break
#CAS 2 :
            self.rotation(tabLiFaceChange[faceChange].upper())
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            self.rotation(faceJaune.upper()+'\'') 
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            self.rotation(faceJaune.upper()+'\'')
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            self.rotation(faceJaune.upper())
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            self.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            self.rotation(faceJaune.upper())
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            self.rotation(faceJaune.upper()+'\'')
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            self.rotation(tabLiFaceChange[faceChange].upper())
            self.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            self.rotation(tabLiFaceChange[faceChange].upper()+'\'')

    def putAreteLastFace(self, faceJaune, tabParc, tabLiFaceChange) :
        if faceJaune == 'd' or faceJaune == 'r' or faceJaune == 'b' :
            sensRotation = 1
        else :
            sensRotation = -1

        faceOpposeFinie = None
        for i in range(4) :
            if self.cube.faceFinished(tabLiFaceChange[i]) :
                faceOpposeFinie = self.cube.getFaceInversed(tabLiFaceChange[i])
                break

        if faceOpposeFinie != None :
            if tabParc[0] == 'x' :
                couleurMiniCube = self.cube.getFace(faceOpposeFinie)[1][tabParc[1]]
            else :
                couleurMiniCube = self.cube.getFace(faceOpposeFinie)[tabParc[0]][1]
                

            faceSuivanteOF = tabLiFaceChange[(tabLiFaceChange.index(faceOpposeFinie)+(1*sensRotation))%4]

            # CAS 2
            #R' U R' U' R' U' R' U R U R2
            if couleurMiniCube == self.cube.getCentralColor(self.cube.liFace[self.cube.liFace.index(faceSuivanteOF)]) :
                self.rotation(faceSuivanteOF.upper()+'\'')
                self.rotation(faceJaune.upper())
                self.rotation(faceSuivanteOF.upper()+'\'')
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(faceSuivanteOF.upper()+'\'')
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(faceSuivanteOF.upper()+'\'')
                self.rotation(faceJaune.upper())
                self.rotation(faceSuivanteOF.upper())
                self.rotation(faceJaune.upper())
                self.rotation(faceSuivanteOF.upper()+'2')

            # CAS 1
            # R2 U' R' U' R U R U R U' R
            else :
                self.rotation(faceSuivanteOF.upper()+'2')
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(faceSuivanteOF.upper()+'\'')
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(faceSuivanteOF.upper())
                self.rotation(faceJaune.upper())
                self.rotation(faceSuivanteOF.upper())
                self.rotation(faceJaune.upper())
                self.rotation(faceSuivanteOF.upper())
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(faceSuivanteOF.upper())

        else :
            if tabParc[0] == 'x' :
                couleurMiniCube = self.cube.getFace(tabLiFaceChange[2])[1][tabParc[1]]
            else :
                couleurMiniCube = self.cube.getFace(tabLiFaceChange[0])[tabParc[0]][1]

            # CAS 1
            # M2 U M2 U2 M2 U M2
            if couleurMiniCube == self.cube.getFace(self.cube.getFaceInversed(tabLiFaceChange[2]))[1][1] :
                # L2 + R2 = M2 ou B2 + F2 = M2 mais cela inverse la face haute et basse
                self.rotation(tabLiFaceChange[0].upper()+'2')
                self.rotation(tabLiFaceChange[2].upper()+'2')
                self.rotation(self.cube.getFaceInversed(faceJaune).upper())
                self.rotation(tabLiFaceChange[0].upper()+'2')
                self.rotation(tabLiFaceChange[2].upper()+'2')
                self.rotation(faceJaune.upper()+'2')
                self.rotation(tabLiFaceChange[0].upper()+'2')
                self.rotation(tabLiFaceChange[2].upper()+'2')
                self.rotation(self.cube.getFaceInversed(faceJaune).upper())
                self.rotation(tabLiFaceChange[0].upper()+'2')
                self.rotation(tabLiFaceChange[2].upper()+'2')

                self.nbCmd -= 4 

            # CAS 2
            # U R' U' R U' R U R U' R' U R U R2 U' R' U
            else :
                if faceJaune == 'l' or faceJaune == 'r' :
                    face = 1
                else :
                    face = 2
                    
                self.rotation(faceJaune.upper())
                self.rotation(tabLiFaceChange[face].upper()+'\'')
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(tabLiFaceChange[face].upper())
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(tabLiFaceChange[face].upper())
                self.rotation(faceJaune.upper())
                self.rotation(tabLiFaceChange[face].upper())
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(tabLiFaceChange[face].upper()+'\'')
                self.rotation(faceJaune.upper())
                self.rotation(tabLiFaceChange[face].upper())
                self.rotation(faceJaune.upper())
                self.rotation(tabLiFaceChange[face].upper()+'2')
                self.rotation(faceJaune.upper()+'\'')
                self.rotation(tabLiFaceChange[face].upper()+'\'')
                self.rotation(faceJaune.upper())
                
## ETAPE 6 & 7  : FIN  ##         


def resolutionFinale(strcu="WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY",entry=''):
    
    cube = Cube(strcu)
    resolution = Resolution(cube)
    #cube = Cube("RWYRWGOGOYYGWRWBOOBOGGGYORGWBWBOYBBGYRRBRGWOWOWYYYBRBR")
    #cube.displayCube()
    resolution.applyCmd(entry)

    print("Cube d'origine")
    print(cube.getStr())
    cube.displayCube()
    
    print(resolution.liCmd)
    print(str(resolution.nbCmd) + '\n')
    
    print("Etape 1 : Croix")
    resolution.theCross('u')
    cube.displayCube()

    print(resolution.liCmd)
    print(str(resolution.nbCmd) + '\n')

    print("Etape 2 : Les coins")

    resolution.theCorner('u')
    cube.displayCube()

    print(resolution.liCmd)
    print(str(resolution.nbCmd) + '\n')

    print("Etape 3 : la deuxieme couronne")
    resolution.deuxcouronne()
    cube.displayCube()

    print(resolution.liCmd)
    print(str(resolution.nbCmd)+ '\n')

    print("Etape 4 : la croix inverse")
    resolution.resolutionCroixJaune()
    cube.displayCube()

    print(resolution.liCmd)
    print(str(resolution.nbCmd) + '\n')

    print("Etape 5 : la face inverse")
    resolution.rfjaune()
    cube.displayCube()

    print(resolution.liCmd)
    print(str(resolution.nbCmd) + '\n')

    print("Etape 6 : les coins et les arretes jaunes ")
    resolution.lastStep()
    cube.displayCube()

    print(resolution.liCmd)
    print(str(resolution.nbCmd) + '\n')

    return resolution.liCmd
#MODIFIER POUR QUE SA FONCTION PERSONNELLE FONCTIONNE



