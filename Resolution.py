#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
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
        print(posY)
        index=['u','d','f','b','r','l'] 
        liste=[['L','B','R','F'],['R','B','L','F'],['L','U','R','D'],['R','U','L','D'],['F','U','B','D'],['B','U','F','D']] #chaque liste correspond a un index respectif

        ind=index.index(posY)
        a=liste[ind].index(pos1.upper())
        b=liste[ind].index(pos2.upper())
        if a > b:
            if liste[ind][(a+1)%4] != pos2.upper() or a < 3:
                print(1)
                return [pos1,pos2]
            else:
                print(2)
                return [pos2,pos1]
        else:
            if liste[ind][(b+1)%4] != pos1.upper() or b <3:
                print(3)
                return [pos2,pos1]
            else:
                print(4)
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

    def ultimateYellowCross(self):
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

            print(len(listeAretes))
            print(listeAretes)
            if len(listeAretes) == 0 or len(listeAretes) == 3 or len(listeAretes)==1:
                print("cas 1")
                if len(listeAretes) == 3:
                    print("Trois faces sur la dernieres, on tente")

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
                        print("cas 2")

                if adj == True :

                    tmp = self.case2(listeAretes[0],listeAretes[1])   #on récupère les aretes dans le bon ordre pour notre algorithme
                    print(tmp)
                    #on applique les rotations par rapport aux bonnes faces du coup
                    listeCeTour.append(self.opposite(tmp[0]))
                    listeCeTour.append(posY.upper())
                    listeCeTour.append(self.opposite(tmp[1]))
                    listeCeTour.append(posY.upper() + "'")
                    listeCeTour.append(self.opposite(tmp[1])+"'")
                    listeCeTour.append(self.opposite(tmp[0])+"'")

                        # F U R Ui Ri Fi
                else :
                    print("cas 3")
                    tmp = self.case3(listeAretes[0])
                    
                    listeCeTour.append(tmp[0])
                    listeCeTour.append(tmp[1])
                    listeCeTour.append(tmp[2])
                    listeCeTour.append(tmp[1]+"'")     #ERREURS
                    listeCeTour.append(tmp[2]+"'")
                    listeCeTour.append(tmp[0]+"'")

                        # F R U Ri Ui Fi
            print(listeCeTour)
            self.listeMouv.append(listeCeTour)
            self.rotate(listeCeTour)



    def rotate(self,liste):
        for i in range(len(liste)):
            cube.rotation(liste[i])
            cube.displayCube()
                    


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

#cube = Cube("GYYGGGGGGRRRWWWOOGORYGRRWWWOOOYYYBRRWWWOORBBYBBBBBBOYY")


            #cube solve v2
#cube = Cube("WWWWWWWWWBBBRRRGGGOOOBBBRRRGGGOOOGOBRRYGYBYYRYYOYYBYGO")

cube = Cube("GYRYYRBGYRBYOYGOYYBOYOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW")
resolution = Resolution(cube)


# PROBLEME SUR LA ROTATION RIGHT



cube.displayCube()
        

#print(resolution.checkCrossNonOriente())
#print(resolution.checkEmplacement())
#resolution.resolutionYellowCross()
#print(resolution.getApproRot("d","l","d"))
resolution.ultimateYellowCross()
print(resolution.listeMouv)
