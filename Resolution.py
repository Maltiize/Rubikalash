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
        dicAdj = [['u','r'],['u','l'],['d','r'],['d','l'],['f','r'],['f','l'],['b','r'],['b','l'],['u','f'],['u','b'],['d','f'],['d','b']]
        dicOp = [['u','d'],['l','r']
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
                if listeAretes[0] == 'b' or listeAretes[0] == 'f':
                    listeCeTour.append('U')
                    listeCeTour.append('R')
                    listeCeTour.append('B')      #bon
                    listeCeTour.append("R'")
                    listeCeTour.append("B'")
                    listeCeTour.append("U'")
                else:
                    listeCeTour.append('F')
                    listeCeTour.append('D')
                    listeCeTour.append('L')      #A check
                    listeCeTour.append("D'")
                    listeCeTour.append("L'")
                    listeCeTour.append("F'")
                    

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
cube = Cube("GOROOOOOOYGGWWWBBYBYOYGGWWWBBYBYRGGGWWWBBOYYYRRRRRRRGB")
#cube = Cube("GYYGGGGGGRRRWWWOOGORYGRRWWWOOOYYYBRRWWWOORBBYBBBBBBOYY")
resolution = Resolution(cube)


# PROBLEME SUR LA ROTATION RIGHT



cube.displayCube()
        
resolution.solveYellow()

print(resolution.checkCrossNonOriente())
print(resolution.checkEmplacement())
#resolution.resolutionYellowCross()
#print(resolution.getApproRot("d","l","d"))
resolution.solveYellowCross()
print(resolution.listeMouv)
