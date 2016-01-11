#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import *
class Resolution:

    def __init__(self,c):
        self.cube=c
        
        # liste des indexes servant  à la croix
        self.liCross=1,5,7,3

        # liste des rotation effectué durant la résolution 
        self.liCmd=[]
        self.liRota='','2',"'"
        
    # Utiliser cette fonction permet de garder en mémoire les mouvements effectué durant la résolution
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
        #print("doing :" ,cmd)
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
        colorcross=cube.getCentralColor(nameFace)
        if(tab[0]==True):
            return 0
        
        # pour toute les faces qui n'ont pas encore été traitée
        while(len(tab[1])!=0):
            for x in tab[1]:
                # On cherche le cube de couleur "Face à traiter" + " Face où se trouve la croix"
                # on récupere donc la couleur de "Face à traiter" 
                curColor=cube.getCentralColor(x)
                result=cube.findCube([colorcross,curColor])

                # on traite les différents cas en fonction de la position du cube

                # cas ou la face de la couleur dont on veut faire la croix (ex blanc) se trouve sur la face de la croix
                if(result[0][1]==nameFace):

                    # si la croix n'a pas été commencé on peut économiser un mouvement
                    if(len(tab[1])==4):
                        self.applyCmd(self.getApproRot(result[1][1],x,result[0][1]))
                    else:
                        self.applyCmd(result[1][1].upper()+'2'+self.getApproRot(result[1][1],x,cube.getFaceInversed(nameFace))+x.upper()+'2')

                #cas ou la face de la couleur dont on veut faire la croix se trouve sur la face inverse de la croix
                if(result[0][1]==cube.getFaceInversed(nameFace)):
                    self.applyCmd(self.getApproRot(result[1][1],x,result[0][1])+x.upper()+'2')

                # si on se trouve dans aucun des deux
                if(result[0][1]!=cube.getFaceInversed(nameFace) and result[0][1]!=nameFace):

                    # on essaye d'approcher le morceau de croix par une seule rotation
                    # le nom de la rotation est donnée par getApproRot si une seule rotation suffit
                    # -1 est renvoyé si ce n'est pas possible ( le pire des cas )
                    # -2 est renvoyé si le la face blanche ( exemple ) se trouve sur la face de destination
                    rot=self.getApproRot(result[1][1],x,result[0][1])
                    if(rot==-1):
                        
                        # si ce n'est pas possible un minimum de trois rotations sera nécessaire
                        
                        # j'ai découpé cette partie en 2 cas à cause de certaines différences de procédure
                        # mais je pense qu'il est pssible de factoriser cette partie du code 
                        if(result[1][1]==nameFace or result[1][1]==cube.getFaceInversed(nameFace)):

                            # si la croix n'a pas été commencée
                            if(len(tab[1])==4):
                                tmpcmd=result[1][1].upper()
                                self.rotation(tmpcmd)
                                
                                tmppos=cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                                self.rotation(tmpcmd)
                                
                                tmppos=cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                                self.rotation(tmpcmd)
                                
                            # si la croix a été commencé on garde en mémoire le mouvement qui perturbe le travail déjà réalisé
                            # on fait ce mouvement à l'inverse une fois la face terminée
                            else:
                                tmpcmd=self.getApproRot(result[1][1],cube.getFaceInversed(nameFace),result[0][1])
                                self.rotation(tmpcmd)
                                self.rotation(cube.getFaceInversed(nameFace).upper())
                                tmppos=cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[1][1],x,tmppos[0][1])
                                
                                faceinter=tmppos[0][1]
                                mouvinter=self.getInvRot(tmpcmd)
                                
                                self.cube.rotation(tmpcmd)
                                
                                tmppos==cube.findCube([colorcross,curColor])
                                tmpcmd=self.getApproRot(tmppos[0][1],nameFace,x)
                                self.rotation(tmpcmd)
                                if(faceinter not in tab[1]):
                                    self.rotation(mouvinter)
                        
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
                                

                    
                    # si la face blanche est sur la face cherchée il faut retourner le cube
                    elif(rot==-2):
                        self.rotation(result[1][1].upper())
                        tmppos=cube.findCube([colorcross,curColor])
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

    ## ETAPE 6 & 7 ##
    
    
    def lastStep(self, cube) :
        if cube.cubeFinished() == False :
            # Récupération des différentes variables nécéssaire à la résolution
            faceJaune = self.getFaceJaune(cube)
            tabParc = self.getTabParc(cube, faceJaune)
            tabLiFaceChange = self.getTabLiFaceChange(cube, faceJaune)

            # Résolution des coins et des arrêtes
            self.putCornerLastFace(cube, faceJaune, tabParc, tabLiFaceChange)
            self.putAreteLastFace(cube, faceJaune, tabParc, tabLiFaceChange)

    def getFaceJaune(self, cube) :
        faceBlanche = ''
        faceJaune = ''

        # On trouve les deux face "finies" pour savoir quelles faces modifier par la suite
        for face in cube.liFace :
            faceBlanche = face
            faceJaune = cube.getFaceInversed(face)
            if cube.faceFinished(faceBlanche) and cube.faceFinished(faceJaune):
                break

        # Si les deux faces sont inversé
        faceTest = cube.getFace(cube.liFace[(cube.liFace.index(faceJaune)+2)%6])
        if ((faceJaune == 'u' or faceJaune == 'b') and faceTest[0][0] == faceTest[0][1] == faceTest[0][2]) or ((faceJaune == 'l' or faceJaune == 'r') and faceTest[0][0] == faceTest[1][0] == faceTest[2][0]) or ((faceJaune == 'd' or faceJaune == 'f') and faceTest[2][0] == faceTest[2][1] == faceTest[2][2]) :
            temp = faceJaune
            faceJaune = faceBlanche
            faceBlanche = temp

        return faceJaune
        
    def getTabParc(self, cube, faceJaune) :
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

    def getTabLiFaceChange(self, cube, faceJaune) :
        # Ce tableau contient les face non finies, il va nous permettre de nous afranchir des couleurs
        # car les mouvements à faire pour résoudre le cube sont symétrique
        if faceJaune == 'd' or faceJaune == 'u' :
            return ['l','f','r','b']
        elif faceJaune == 'l' or faceJaune == 'r' :
            return ['f','u','b','d']
        else :
            return ['d','r','u','l']
        
    def putCornerLastFace(self, cube, faceJaune, tabParc, tabLiFaceChange) :
        if tabParc[0] == 'x' :
            index = 1
        else :
            index = 0

        tabMiniReplace = []
        
        #A ce niveau de résolution il est possible de bien placer deux coins,
        #donc tant que je n'obtient pas seulement deux coins mal placés :
        while len(tabMiniReplace) != 4 :
            for i in range(4) :
                faceEnCours = cube.getFace(tabLiFaceChange[i])
                if index == 0 :
                    if faceEnCours[tabParc[index]][0] != faceEnCours[(tabParc[index]+1)%2][0] :
                        tabMiniReplace.append([i,tabParc[index],0])
                    if faceEnCours[tabParc[index]][2] != faceEnCours[(tabParc[index]+1)%2][2] :
                        tabMiniReplace.append([i,tabParc[index],2])
                else :
                    if faceEnCours[0][tabParc[index]] != faceEnCours[0][(tabParc[index]+1)%2] :
                        tabMiniReplace.append([i,0,tabParc[index]])
                    if faceEnCours[2][tabParc[index]] != faceEnCours[2][(tabParc[index]+1)%2] :
                        tabMiniReplace.append([i,2,tabParc[index]])
            #(suite) je tourne la face "Jaune" (non résolue)
            if len(tabMiniReplace) != 4 :
                cube.rotation(faceJaune.upper())

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
            cube.rotation(tabLiFaceChange[faceChange].upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            cube.rotation(tabLiFaceChange[(faceChange+(1*sensRotation))%4].upper())
            cube.rotation(tabLiFaceChange[faceChange].upper()+'2')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(tabLiFaceChange[faceChange].upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            cube.rotation(tabLiFaceChange[(faceChange+(1*sensRotation))%4].upper()+'\'')
        else :
            for i in range(4):
                if index == 0 :
                    if tabMiniReplace[i][2] == 2 - tabParc[index] :
                        faceChange = tabMiniReplace[i][0]
                        break
                else : 
                    if tabMiniReplace[i][1] == tabParc[index] :
                        faceChange = tabMiniReplace[i][0]
                        break
#CAS 2 :
            cube.rotation(tabLiFaceChange[faceChange].upper())
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            cube.rotation(faceJaune.upper()+'\'') 
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            cube.rotation(tabLiFaceChange[faceChange].upper()+'\'')
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper()+'\'')
            cube.rotation(tabLiFaceChange[faceChange].upper())
            cube.rotation(tabLiFaceChange[(faceChange+(3*sensRotation))%4].upper())
            cube.rotation(tabLiFaceChange[faceChange].upper()+'\'')

    def putAreteLastFace(self, cube, faceJaune, tabParc, tabLiFaceChange) :
        if faceJaune == 'd' or faceJaune == 'r' or faceJaune == 'b' :
            sensRotation = 1
        else :
            sensRotation = -1

        faceOpposeFinie = None
        for i in range(4) :
            if cube.faceFinished(tabLiFaceChange[i]) :
                faceOpposeFinie = cube.getFaceInversed(tabLiFaceChange[i])
                break

        if tabParc[0] == 'x' :
            couleurMiniCube = cube.getFace(faceOpposeFinie)[1][tabParc[1]]
        else :
            couleurMiniCube = cube.getFace(faceOpposeFinie)[tabParc[0]][1]
            

        faceSuivanteOF = tabLiFaceChange[(tabLiFaceChange.index(faceOpposeFinie)+(1*sensRotation))%4]

        # CAS 2
        #R' U R' U' R' U' R' U R U R2
        if couleurMiniCube == cube.getCentralColor(cube.liFace[cube.liFace.index(faceSuivanteOF)]) :
            cube.rotation(faceSuivanteOF.upper()+'\'')
            cube.rotation(faceJaune.upper())
            cube.rotation(faceSuivanteOF.upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(faceSuivanteOF.upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(faceSuivanteOF.upper()+'\'')
            cube.rotation(faceJaune.upper())
            cube.rotation(faceSuivanteOF.upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(faceSuivanteOF.upper()+'2')

        # CAS 1
        # R2 U' R' U' R U R U R U' R
        else :
            cube.rotation(faceSuivanteOF.upper()+'2')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(faceSuivanteOF.upper()+'\'')
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(faceSuivanteOF.upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(faceSuivanteOF.upper())
            cube.rotation(faceJaune.upper())
            cube.rotation(faceSuivanteOF.upper())
            cube.rotation(faceJaune.upper()+'\'')
            cube.rotation(faceSuivanteOF.upper())


        print(tabLiFaceChange)
        


    ## ETAPE 6 & 7 ##         


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
    
        
#cube = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGOOYBRBGYGROBYYYYYYYR")
#c1=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGRBROYBYGOOYYBYYYYYR")
#c=Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGYYYYYYYYY")
#c2=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGRBYGYBBGYOYRYOYYYRYO")

#rfjaune(c2)
        

#cube = Cube("OOOOOOOOOBBBRRRJJJGGGBBBRRRJJJGGGBBBRRRJJJGGGYYYYYYYYY")
#COIN
    #CAS1

        #Gauche
#cube = Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGBNGRNBONOGNRYYYYYYYYY")

        #Droite
#cube = Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRNRBNOGNBONGYYYYYYYYY")

    #CAS2
cube = Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGROOGRBOGRBBGYYYYYYYYY")

resol= Resolution(cube)
cube.displayCube()
resol.lastStep(cube)
cube.displayCube()

