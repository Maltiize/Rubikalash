class Cube:


    # 0 si jamais la couleur n'a pas encore été indiquée 
    def __init__(self, cube=None):

        #plages d'indexes de toutes les cases de chaque face
        # CF schéma dans madoc 

        self.idx=[["u",range(0,9)],["d",range(45,54)],["f",[12,13,14 ,24,25,26, 36,37,3]],["l",[9,10,11, 21,22,23, 33,34,35]],["r",[15,16,17 ,27,28,29, 39,40,41]],["b",[18,19,20 ,30,31,32, 42,43,44]]]
        

        #liste des noms des faces permet de faciliter les boucles for
        self.liFace=["u","d","l","r","f","b"]
        
        #Initialisation des faces à 0
        
        self.up=[0,0,0],[0,0,0],[0,0,0] 
        self.down=[0,0,0],[0,0,0],[0,0,0]
        self.front=[0,0,0],[0,0,0],[0,0,0]
        self.left=[0,0,0],[0,0,0],[0,0,0]
        self.right=[0,0,0],[0,0,0],[0,0,0]
        self.back=[0,0,0],[0,0,0],[0,0,0]

        #Liste des mouvements
        self.D=["d",[["l",[6,7,8]],["f",[6,7,8],["r",[6,7,8]],["b",[6,7,8]]]]
        self.U=["u",[["l",[0,1,2]],["f",[0,1,2],["r",[0,1,2]],["b",[0,1,2]]]]
                
        self.R=["r",[["l",[1,2,3]],["f",[1,2,3],["r",[1,2,3]],["b",[1,2,3]]]]
        self.L=["l",[["l",[1,2,3]],["f",[1,2,3],["r",[1,2,3]],["b",[1,2,3]]]]
                
        self.B=["b",[["l",[1,2,3]],["f",[1,2,3],["r",[1,2,3]],["b",[1,2,3]]]]
        self.F=["f",[["l",[2,5,8]],["u",[8,7,6],["r",[6,3,1]],["d",[1,2,3]]]]
        


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
    # rotation interprete la commande et la redirige vers la methode associée
    
    def rotation(self,cmd):
        return
    
    def rotU(self,option=None):
        return

    def rotF(self,option=None):
        return


    def rotB(self,option=None):
        return


    def rotL(self,option=None):
        return


    def rotBa(self,option=None):
        return


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
    def printcube(self):
        for x in self.liFace:
            print("-------",x,"--------")
            afftab(self.getFace(x))

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


    

cube.printcube()
cube.setFace('u',[[0,0,0],[0,0,0],[0,0,0]]  )
cube.printcube()

print(cube.cubeFinished())

