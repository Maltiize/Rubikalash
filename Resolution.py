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
            listos=[]
            pos = cube.findCube(['Y',listeColors[i][0][0]])
            listos.append(pos[0][1])
            listos.append(listeColors[i][0][0])
            liste.append(listos)    
            #liste contenant les listes des arêtes avec (1) : sur quelle face se trouve la partie Y de l'arete et (2) : de quelle couleur est l'autre partie
        return liste

#fonction resolvant la croix yellow
    def resolutionYellowCross(self):

        #tant que la croix n'est pas vérifiée
        while self.checkCrossNonOriente() != True:
            listos=[]
            #on récupère la position des arêtes ainsi que leur couleur a chaque tour
            liste=self.checkEmplacement()   
            
            #On parcourt la liste, et si les parties Y ne sont pas sur la bonne face, on les ajoute à la liste des aretes a prendre en compte
            for i in range(len(liste)):
                if liste[i][0] != self.whichIsColor('Y'):
                    listos.append(liste[i])
            

            
            # CAS 1 --------------------------------------------------------------------------------------------------



            if len(listos) == 3:
                resolution.rotate(['R','U',"2R'","U'",'R',"U'","R'"])



            # CAS 2 --------------------------------------------------------------------------------------------------
            


            #retourner deux aretes adjacentes
            if len(listos) == 2:
                #les différents cas possibles où les deux aretes sont adjacentes
                if (cube.findCube([listos[0][0]]))[0][1] == 'u' and ((cube.findCube([listos[1][0]]))[1][1] == 'l' or (cube.findCube([listos[1][0]]))[1][1] == 'r'):

                    if (cube.findCube([listos[1][0]]))[1][1] == 'l':
                        self.listeMouv.append(self.getApproRot("u","r","l"))
                        self.listeMouv.append(self.getApproRot("l","u","u"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("u","l","u"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("r","u","l"))
                    #a vérifier
                    if (cube.findCube([listos[1][0]]))[1][1] == 'r':
                        self.listeMouv.append(self.getApproRot("u","r","u"))
                        self.listeMouv.append(self.getApproRot("l","u","r"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("u","l","r"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("r","u","u"))

                if (cube.findCube([listos[1][0]]))[1][1] == 'u' and ((cube.findCube([listos[0][0]]))[1][1] == 'l' or (cube.findCube([listos[0][0]]))[1][1] == 'r'):

                    if (cube.findCube([listos[0][0]]))[1][1] == 'l':
                        self.listeMouv.append(self.getApproRot("u","r","l"))
                        self.listeMouv.append(self.getApproRot("l","u","u"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("u","l","u"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("r","u","l"))
                    #a vérifier
                    if (cube.findCube([listos[0][0]]))[1][1] == 'r':
                        self.listeMouv.append(self.getApproRot("u","r","u"))
                        self.listeMouv.append(self.getApproRot("l","u","r"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("u","l","r"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("r","u","u"))


                if (cube.findCube([listos[0][0]]))[0][1] == 'd' and ((cube.findCube([listos[1][0]]))[1][1] == 'l' or (cube.findCube([listos[1][0]]))[1][1] == 'r'):
                    
                    #a faire j'ai eu la flemme
                    if (cube.findCube([listos[1][0]]))[1][1] == 'l':
                        self.listeMouv.append(self.getApproRot("u","r","d"))
                        self.listeMouv.append(self.getApproRot("u","l","l"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("l","u","l"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("r","u","d"))
                    #a vérifier
                    if (cube.findCube([listos[1][0]]))[1][1] == 'r':
                        self.listeMouv.append(self.getApproRot("u","r","r"))
                        self.listeMouv.append(self.getApproRot("u","l","d"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("l","u","d"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("r","u","r"))

                if (cube.findCube([listos[1][0]]))[1][1] == 'd' and ((cube.findCube([listos[0][0]]))[1][1] == 'l' or (cube.findCube([listos[0][0]]))[1][1] == 'r'):
                    

                    if (cube.findCube([listos[0][0]]))[1][1] == 'l':
                        self.listeMouv.append(self.getApproRot("d","l","d"))
                        self.listeMouv.append(self.getApproRot("u","l","l"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("l","u","l"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("l","d","d"))
                    #a vérifier
                    if (cube.findCube([listos[0][0]]))[1][1] == 'r':
                        self.listeMouv.append(self.getApproRot("d","l","r"))
                        self.listeMouv.append(self.getApproRot("u","l","d"))
                        self.listeMouv.append(self.getApproRot("u","r","b"))

                        self.listeMouv.append(self.getApproRot("l","u","d"))
                        self.listeMouv.append(self.getApproRot("r","u","b"))
                        self.listeMouv.append(self.getApproRot("l","d","r"))

            #if cube.getCentralColor(listos[0]) == 'B' and cube.getCentralColor(listos[1]) =='G' or cube.getCentralColor(listos[0]) == 'R' and cube.getCentralColor(listos[1]) == 'O':
             #       resolution.rotate(['F','R','U',"R'","U'","F'"])
            
            # CAS 3 --------------------------------------------------------------------------------------------------




                
            
            else:
                resolution.rotate(['F','U',"R","U'","R'","F'"])

    def rotate(self,liste):
        for i in range(len(liste)):
            cube.rotation(liste[i])
            cube.displayCube()
                    


cube = Cube("YBGGGGGGGRRRWWWOOOYYBGRRWWWOOOYYYYRRWWWOOGRYOBBBBBBBRY")

resolution = Resolution(cube)

cube.displayCube()
        
resolution.solveYellow()

print(resolution.checkCrossNonOriente())
print(resolution.checkEmplacement())
resolution.resolutionYellowCross()
print(resolution.getApproRot("d","l","d"))
