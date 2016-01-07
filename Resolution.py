#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube


from Cube import *

class Resolution:

    def __init__(self,c,face=None,listeAretes=[]):
        self.cube=c
        self.face=face
        self.listeAretes=listeAretes
        self.listeMouv=[]
        # liste des indexes servant  à la croix
        self.liCross=1,5,7,3
        self.liCorner=0,2,8,6
        # liste des rotation effectué durant la résolution 
        self.liCmd=''
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
        print("doing :" ,cmd)
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
        
        for x in m[1]:
            coloredge=cube.getCentralColor(x[0])
            result=cube.findCube([colorcross,coloredge],nameFace)
            
            if(result==-1 or result[1][1]!=x[0]):
                tmp[1]+=[x[0]]
                tmp[0]=False
                
                
        return tmp

     #verifie si les coin sont fait           
    def checkCorner(self,nameFace):
        tmp=[True,[]]
        colorcorner=cube.getCentralColor(nameFace)
        m=cube.getMouv(nameFace.upper())
        for x in range (4):
            colorPrev=cube.getCentralColor(m[1][(x+3)%4][0])
            colorNext=cube.getCentralColor(m[1][x][0])
            

            result=cube.findCube([colorcorner,colorPrev,colorNext],nameFace)
            
            if(result==-1 or result[1][1]!=m[1][(x+3)%4][0] or result[2][1]!=m[1][x][0] ):
                tmp[1]+=[[[m[1][(x+3)%4][0],colorPrev],[m[1][x][0],colorNext]]]
                tmp[0]=False
                
        return tmp

#the corner permet de faire les coin d'une face sans prendre en compte se qu'elle fait sur les autre face
    def theCorner(self,nameFace):
        tab=self.checkCorner(nameFace)
        colorCorner=cube.getCentralColor(nameFace)
        inv=cube.getFaceInversed(nameFace)
        if(tab[0]==True):
            return 0
        else :
            for idx, x in enumerate (tab[1]) :
               
                
                tmp=cube.findCube([colorCorner,x[0][1],x[1][1]])
                if (tmp[0][1] != inv):
                    for i in range (0,2) :
                        if (tmp[1+i][1] == inv):
                            m=cube.getMouv(tmp[2-i][1].upper())
                            if (tmp[2-i][1] != x[1-i][0]):
                                self.rotation(self.getApproRot(tmp[2-i][1],x[1-i][0],inv))
                                
                            if (tmp[0][1] == m[1][1][0]):
                                self.rotation(inv.upper())
                                self.rotation(tmp[2-i][1].upper())
                                self.rotation(self.getInvRot(inv.upper()))
                                self.rotation(self.getInvRot(tmp[2-i][1].upper()))
                            else :
                                self.rotation(self.getInvRot(inv.upper()))
                                self.rotation(self.getInvRot(tmp[2-i][1].upper()))
                                self.rotation(inv.upper())
                                self.rotation(tmp[2-i][1].upper())
                else :
                    m=cube.getMouv(tmp[2][1].upper())
                    if (tmp[2][1] != x[0][0]):
                        self.rotation(self.getApproRot(tmp[2][1],x[0][0],inv))
                    if (tmp[1][1]== m[1][1][0]):
                        
                        self.rotation(self.getInvRot(cube.getFaceInversed(tmp[2][1]).upper()))#R'
                        self.rotation(inv.upper()+'2')
                        self.rotation(cube.getFaceInversed(tmp[2][1]).upper())
                        self.rotation(inv.upper())
                        self.rotation(self.getInvRot(cube.getFaceInversed(tmp[2][1]).upper()))
                        self.rotation(self.getInvRot(inv.upper()))
                        self.rotation(cube.getFaceInversed(tmp[2][1]).upper())
                    else:
                        self.rotation(self.getInvRot(m[1][1][0].upper()))
                        self.rotation(inv.upper()+'2')
                        self.rotation(m[1][1][0].upper())
                        self.rotation(inv.upper())
                        self.rotation(self.getInvRot(m[1][1][0].upper()))
                        self.rotation(self.getInvRot(inv.upper()))
                        self.rotation(m[1][1][0].upper())
    def rfjaune(self):
       cube=self.cube
       j=cube.down
       r=cube.front
       b=cube.right
       if not cube.faceFinished('d'):
          
          if  b[2][0]=='Y' and r[2][0]=='Y' and j[2][2]=='Y' and j[0][0]!='Y' and j[0][2]!='Y' and j[2][0]!='Y':
             self.applyCmd("FDF'DFD2F'")

          elif  b[2][2]=='Y' and r[2][0]=='Y' and j[0][2]=='Y' and j[2][0]=='Y' and j[2][2]!='Y' and j[0][0]!='Y':
             self.applyCmd("F'RFL'F'R'FL")

          elif b[2][0]=='Y' and b[2][2]=='Y' and j[0][0]=='Y' and j[2][0]=='Y'  and j[2][2]!='Y' and j[0][2]!='Y':
             self.applyCmd("F2UF'D2FU'F'D2F'")

          elif r[2][0]=='Y' and j[0][2]=='Y' and j[2][2]=='Y'  and j[2][0]!='Y' and j[0][0]!='Y':
             self.applyCmd("F'R'FL'F'RFL")

          elif r[2][2]=='Y' and b[2][2]=='Y' and j[0][0]=='Y' and j[2][2]!='Y' and j[2][0]!='Y' and j[0][2]!='Y':
             self.applyCmd("FD2F'D'FD'F'")

          elif r[2][0]=='Y' and r[2][2]=='Y' and j[0][0]!='Y' and j[0][2]!='Y' and j[2][0]!='Y' and j[2][2]!='Y' :
             self.applyCmd("FDF'DFD'F'DFD'D'F'")

          elif b[2][0]=='Y' and j[0][0]!='Y' and j[0][2]!='Y' and j[2][0]!='Y' and j[2][2]!='Y':
             self.applyCmd("FD2F2D'F2D'F2D2F")

          else :
             cube.rotation('D')       
             self.rfjaune()
    

        


#Fonction qui renvoie quelle face est de la couleur recherchée (jaune pour mon algo ("Y"))
#On compare avec la couleur de chaque face en [1][1] et donc au milieu
    def whichIsColor(self,color):

        colorF = cube.up[1][1]  
        if colorF == color :
            return "u"

        colorF = cube.down[1][1]
        if colorF == color :
            return "d"

        colorF = cube.right[1][1]
        if colorF == color :
            return "r"

        colorF = cube.left[1][1]
        if colorF == color :
            return "l"

        colorF = cube.back[1][1]
        if colorF == color :
            return "b"

        colorF = cube.front[1][1]
        if colorF == color:
            return "f"

#Fonction qui recherche les aretes manquantes puis effectue les rotations nécessaires pour les amener
    def solveYellow(self):
        listeColors=['G','R','B','O']
        for i in range(len(listeColors)):   
            self.listeAretes.append(cube.findCube(['Y',listeColors[i]]))
        #trouve toutes les aretes jaunes que l'on doit placer
            
#Fonction qui vérifie si la croix non orienté est vérifiée
    def checkCrossNonOriente(self):
        posColor = self.whichIsColor('Y')   #on trouve la position de la face jaune
        listeColors=['G','R','B','O']       #c'est la liste des couleurs composants les aretes avec une face jaune
        for i in range(len(listeColors)):   #on parcout la liste des couleurs
            pos = cube.findCube(['Y',listeColors[i][0][0]]) #on récupère la position des aretes
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
            pos = cube.findCube(['Y',listeColors[i][0][0]])
            listos.append(pos[0][1])
            listos.append(pos[1][1])
            liste.append(listos)    
            #liste contenant les listes des arêtes avec (1) : sur quelle face se trouve la partie Y de l'arete et (2) : de quelle couleur est l'autre partie
        return liste

#fonction qui renvoie la position des 


    def solveYellowCross(self):
        dicAdj = [['u','r'],['u','l'],['d','r'],['d','l']]
        dicOp = [['u','d'],['l','r']]
        #tant que la croix jaune n'est pas vérifiée
        print("Dans la fonction")
        while self.checkCrossNonOriente() != True:
            print("Dans la boucle")
            
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

            print(len(listeAretes))
            if len(listeAretes) == 0 or len(listeAretes) == 3 or len(listeAretes)==1:
                print("cas 1")
                if len(listeAretes) == 3:
                    print("Trois faces sur la dernieres, on tente")
    
                listeCeTour.append('U')
                listeCeTour.append('R')
                listeCeTour.append('B')      #bon
                listeCeTour.append("R'")
                listeCeTour.append("B'")
                listeCeTour.append("U'")
                

                    # D F R Fi Ri Di
                    #on prend n'import lequel balek

                # F U R Ui Ri Fi
            if len(listeAretes) == 2:

                #Cas si les aretes sont 'adjacentes'
                for i in range(len(dicAdj)):

                    if listeAretes[0] in dicAdj[i] and listeAretes[1] in dicAdj[i]:
                        pos = i
                        adj = True

                        print("cas 2")
                if adj == True :
                    if pos  == 0:
                        print(pos)

                        listeCeTour.append('D')
                        listeCeTour.append('B')
                        listeCeTour.append('L')      
                        listeCeTour.append("B'")     #Check
                        listeCeTour.append("L'")
                        listeCeTour.append("D'")
                        # D F R Fi Ri Di
                        #cas down
                        
                    elif pos == 1:
                        print(pos)

                        listeCeTour.append('R')
                        listeCeTour.append('B')
                        listeCeTour.append('D')      #Check
                        listeCeTour.append("B'")
                        listeCeTour.append("D'")
                        listeCeTour.append("R'")
                        # R U B Ui Bi Ri
                        #cas right

                    elif pos == 2:
                        print(pos)

                        listeCeTour.append('L')
                        listeCeTour.append('B')
                        listeCeTour.append('U')      #Check
                        listeCeTour.append("B'")
                        listeCeTour.append("U'")
                        listeCeTour.append("L'")
                        # L U F Ui Fi Li
                        #cas left

                    elif pos == 3:
                        print(pos)

                        listeCeTour.append('U')
                        listeCeTour.append('B')
                        listeCeTour.append('R')      #Check
                        listeCeTour.append("B'")
                        listeCeTour.append("R'")
                        listeCeTour.append("U'")
                        # U B R Bi Ri Ui
                        #cas up

                        # F U R Ui Ri Fi
                else :
                    print("cas 3")
                    if listeAretes[0] in dicOp[0] and listeAretes[1] in dicOp[0]:
                        # R B U Bi Ui Ri
                        print("------------------- 1 -------------------")
                        listeCeTour.append('R')
                        listeCeTour.append('D')
                        listeCeTour.append('B')
                        listeCeTour.append("D'")     #ERREURS
                        listeCeTour.append("B'")
                        listeCeTour.append("R'")

                        #on fait cas right
                        #cas left or right
                    if listeAretes[0] in dicOp[1] and listeAretes[1] in dicOp[1]:
                        # U R B Ri Bi Ui
                        print("------------------- 2 -------------------")
                        listeCeTour.append('U')
                        listeCeTour.append('R')
                        listeCeTour.append('B')      #Check
                        listeCeTour.append("R'")
                        listeCeTour.append("B'")
                        listeCeTour.append("U'")

                        #cas up 
                        #cas up or down

                        # F R U Ri Ui Fi
            print(listeCeTour)
            self.listeMouv.append(listeCeTour)
            self.rotate(listeCeTour)

                
            



             

    def rotate(self,liste):
        for i in range(len(liste)):
            cube.rotation(liste[i])
            cube.displayCube()
                    
#cc      
#cube = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGOOYBRBGYGROBYYYYYYYR")
#c1=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGRBROYBYGOOYYBYYYYYR")
#c=Cube("WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGYYYYYYYYY")
#c2=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGRBYGYBBGYOYRYOYYYRYO")

#rfjaune(c2)
        
    
#cube = Cube("OOOOOOOOOBBBRRRJJJGGGBBBRRRJJJGGGBBBRRRJJJGGGYYYYYYYYY")
cube = Cube("GGRRWGYRGYYBRBWOYWGWOOGRGRWBBWOOBBOYGYBWOBRRYRBOYYGOWW")
cube1=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOBRBOBYGOGYGRYYRYYYYYO")

#cube.displayCube()
#resol= Resolution(cube)
#resol.theCross('f')
#cube.displayCube()
#cube.displayCube()
#resol.applyCmd("FRD2L'F")
#cube.displayCube()
resol=Resolution(cube1)
##resol.theCross('f')
##cube.displayCube()
resol.rfjaune()
cube1.displayCube()

#cube = Cube("GOBOOOOOOYGGWWWBBYOYOYGGWWWBBYGYBRGGWWWBBRYYYRRRRRRBRG")
#cube = Cube("YYRBBBBBBBOOWWWRRYBBOYOOWWWRRYRYOOOOWWWRRGRGYGGGGGGGYY")
#cube = Cube("GYROOOOOOYGGWWWBBGYBOYGGWWWBBRYYGRGGWWWBBBOYYRRRRRRBOY")
#cube = Cube("YRYOOOOOOBGGWWWBBRGYOYGGWWWBBGYYBGGGWWWBBRBOORRRRRRYYY")
            #meme cube *2
#cube = Cube("OYYGGGGGGYRRWWWOOGOBBRRRWWWOOGYYYRRRWWWOOBYOGBBBBBBYYR")
#cube = Cube("GGBOOOOOOYGGWWWBBRYYOYGGWWWBBYOYBOGGWWWBBYGYBRRRRRRYRR")
            #meme cube *4
#cube = Cube("BGRRRRRRROBBWWWGGGYYYYBBWWWGGYRYBYBBWWWGGYOYBOOOOOOROG")
#cube = Cube("YYOBBBBBBROOWWWRRBYBBOOOWWWRRGYYYGOOWWWRRRYROGGGGGGYYG")
#cube = Cube("GOROOOOOOYGGWWWBBYBYOYGGWWWBBYBYRGGGWWWBBOYYYRRRRRRRGB")
cube = Cube("GYYGGGGGGRRRWWWOOGORYGRRWWWOOOYYYBRRWWWOORBBYBBBBBBOYY")
resolution = Resolution(cube)


# PROBLEME SUR LA ROTATION RIGHT



cube.displayCube()
        
resolution.solveYellow()

print(resolution.checkCrossNonOriente())
print(resolution.checkEmplacement())
resolution.solveYellowCross()
print(resolution.listeMouv)

