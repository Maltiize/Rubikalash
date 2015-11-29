import copy
class Cube:


    # 0|1|2
    # 3|4|5
    # 6|7|8

    # 0 si jamais la couleur n'a pas encore été indiquée 
    def __init__(self, cube=None):

        #plages d'indexes de toutes les cases de chaque face
        # CF schéma dans madoc 

        self.idx=[["u",range(0,9)],["d",range(45,54)],["f",[12,13,14 ,24,25,26, 36,37,3]],["l",[9,10,11, 21,22,23, 33,34,35]],["r",[15,16,17 ,27,28,29, 39,40,41]],["b",[18,19,20 ,30,31,32, 42,43,44]]]
        

        #liste des noms des faces permet de faciliter les boucles for
        self.liFace=["u","l","f","r","b","d"]
        
        #Initialisation des faces à 0
        
        self.up=[0,0,0],[0,0,0],[0,0,0] 
        self.down=[0,0,0],[0,0,0],[0,0,0]
        self.front=[0,0,0],[0,0,0],[0,0,0]
        self.left=[0,0,0],[0,0,0],[0,0,0]
        self.right=[0,0,0],[0,0,0],[0,0,0]
        self.back=[0,0,0],[0,0,0],[0,0,0]

        #ordre de transposition de la face qui tourne
        self.trans=[0,1,2],[2,5,8],[8,7,6],[6,3,0]

        #Liste des mouvements
        self.D="d",[["l",[6,7,8]],["f",[6,7,8]],["r",[6,7,8]],["b",[6,7,8]]]
        self.U="u",[["l",[0,1,2]],["f",[0,1,2]],["r",[0,1,2]],["b",[0,1,2]]]
                
        self.R="r",[["d",[2,5,8]],["f",[2,5,8]],["u",[2,5,8]],["b",[0,3,6]]]
        self.L="l",[["l",[0,3,6]],["f",[0,3,6]],["r",[0,3,6]],["b",[8,5,2]]]
                
        #self.B="b",[["l",[1,2,3]],["f",[1,2,3]],["r",[1,2,3]],["b",[1,2,3]]
        self.F="f",[["l",[2,5,8]],["u",[8,7,6]],["r",[6,3,1]],["d",[1,2,3]]]
        


        #Si aucunes configuration de départ n'a été renseignée
        
        if(cube==None):
            return

        #origin stocke 
        self.origin=cube

        for x in self.idx:
            self.initFace(x)
        
    #change l'état d'une face par le tableau renseigné
    def setFace(self,nameFace,face):
        if(nameFace=="u"):
            self.up=face
            return
            
        if(nameFace=="d"):
            self.down=face
            return 
            
        if(nameFace=="l"):
            self.lef=face
            return
            
        if(nameFace=="r"):
            self.right=face
            return
            
        if(nameFace=="f"):
            self.front=face
            return
            
        if(nameFace=="b"):
            self.back=face
            return

        
        print("INVALID FACENAME")
        return -1
        

    # Cette methode remplis chaque face avec les éléments qui lui correspondent 
    # et renseignés dans la listes idx ( cf __init__ )

    def initFace(self,idx):
        # on recupere la face à initialiser
        face=self.getFace(idx[0])
        i=0 
        j=0
        for val in idx[1]:

            face[j][i]=self.origin[val]
            #on passe à la case suivante   
            i=i+1

            # si on arrive à la fin d'une ligne
            # on passe à la suivante         
            if(i%3==0):   
                i=0
                j=j+1

        return face
        

    # cmd décrit l'action à operer sur le cube
    # rotation marche en deux parties
    # la rotation de la face puis la rotation des bords de la face 
    def rotation(self,cmd):
        
        return

  
    def rotationFace(self,face):
        f=self.getFace(face)
        tmp=[0,0,0],[0,0,0],[0,0,0] 
        for x in range(0,4):
            t=self.trans[x]
            s=self.trans[(x+1)%4]
            for y in range(0,3):
                tmp[int(s[y]/3)][s[y]%3]=f[int(t[y]/3)][t[y]%3]
        self.setFace(face,tmp)
        
    def getLiCase(self,nameFace,li):
        f=self.getFace(nameFace)
        ret = []
        for x in li:
            ret=ret+[f[int(x/3)][x%3]]
        print(ret)
        return ret
    
    def rotationEdge(self,mouv):
        m=self.getMouv(mouv)
        tmp=[]
        for x in range(0,4):
            tmp=tmp +[self.getLiCase(m[1][x][0],m[1][x][1])]
        #recuperer la face de travail et la face courante
        #sauvegarder les 3 cases de la face de travil
        #transfer les trois cases de la face courante vers la face de travail
        #répéter 4 fois
        for x in range(0,4):
            f=self.getFace(m[1][(x+1)%4][0])
            for y in range(0,3):
                i=m[1][(x+1)%4][1][y]
                f[int(i/3)][i%3]=tmp[x][y]

        
                
            


            
   
    # récupere la face renseignée par nameFace 
    def getFace(self,nameFace):
        if(nameFace=='u'):
            return self.up
        
        if(nameFace=='d'):
            return self.down

        if(nameFace=='f'):
            return self.front

        if(nameFace=='l'):
            return self.left

        if(nameFace=='r'):
            return self.right

        if(nameFace=='b'):
            return self.back
        
        print("INVALID FACENAME")
        return -1


    def getMouv(self,nameMouv):
        if(nameMouv=='R'):
            return self.R
        
        if(nameMouv=='L'):
            return self.L

        if(nameMouv=='U'):
            return self.U

        if(nameMouv=='D'):
            return self.D

        if(nameMouv=='B'):
            return self.B

        if(nameMouv=='F'):
            return self.F
        
        print("INVALID MOUVEMENT NAME")
        return -1

    # Verifie qu'une face est complete
    def faceFinished(self,nameFace):
        face=self.getFace(nameFace)
        color=face[0][0]
        for x in face:
            for y in x:
                if(y!=color):
                    return False
        
        return True

    # Verifie si un cube est terminé ou non 
    def cubeFinished(self):
        for x in self.liFace:
            if(self.faceFinished(x)==False):
                return False
        return True


    #methode d'affichage du cube
    def printCube(self):
        print("///////////////////////////////////")
        for x in self.liFace:
            print("-------",x,"--------")
            afftab(self.getFace(x))
        print("///////////////////////////////////")

#methode d'affichage d'une table 2D
def afftab(tab):
    for x in tab:
        aff(x)
    print("")
    print("")

        


       
def aff(tab):
   
    for x in range(0,len(tab)):
        print("_____",end='')
    print("")
    print(" | ",end='')
    for x in tab:
        print (x,end='')
        print(" | ",end='')
    print("")



        


cube = Cube("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")


cube.printCube()

cube.rotationEdge('D')
cube.printCube()
print(cube.cubeFinished())

