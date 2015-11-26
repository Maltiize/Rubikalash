class Cube:


    # 0 si jamais la couleur n'a pas encore été indiquée 
    def __init__(self, cube=None):

        #plages d'indexes de toutes les cases correspondantes à chaque face
        # CF schéma dans madoc 

        self.idxu=range(0,9)
        self.idxd=range(45,54)
        self.idxf=[12,13,14 ,24,25,26, 36,37,3]
        self.idxl=[9,10,11, 21,22,23, 33,34,35]
        self.idxr=[15,16,17 ,27,28,29, 39,40,41]
        self.idxb=[18,19,20 ,30,31,32, 42,43,44]

        
        #Initialisation des faces à 0
        
        self.up=[0,0,0],[0,0,0],[0,0,0] 
        self.down=[0,0,0],[0,0,0],[0,0,0]
        self.front=[0,0,0],[0,0,0],[0,0,0]
        self.left=[0,0,0],[0,0,0],[0,0,0]
        self.right=[0,0,0],[0,0,0],[0,0,0]
        self.back=[0,0,0],[0,0,0],[0,0,0]


        #Si aucunes configuration de départ n'a été renseignée
        
        if(Cube==None):
            return

        self.origin=cube

        
        self.up=self.setface(self.idxu,self.up)
        self.down=self.setface(self.idxd,self.down)
        self.front=self.setface(self.idxf,self.front)
        self.left=self.setface(self.idxl,self.left)
        self.right=self.setface(self.idxr,self.right)
        self.back=self.setface(self.idxb,self.back)


    # Cette methode remplis chaque face avec les éléments qui lui correspondent 
    # ( renseignés dans les listes idx[nomface] )

    def setface(self,idx,face):
        if(len(idx)!=9):
            print("INVALID SIZE ON IDX")
            return -1
        
        i=0
        j=0
        for val in idx:

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
    # rotation interprete la coommande et la redirige vers la methode associée
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



    def getFace(self,nameFace):
        return


    def faceFinished(self):
        return


    def cubeFinished(self):
        return


    #methode d'affichage du cube
    def printcube(self):
        afftab(self.up)
        afftab(self.left)
        afftab(self.front)
        afftab(self.right)
        afftab(self.back)
        afftab(self.down)

#methode d'affichage d'un table 2D
def afftab(tab):
    for x in tab:
        aff(x)
    print("")
    print("")

        


       
def aff(tab):
    for x in tab:
        print (x,end='')
        print(" , ",end='')
    print("")



        


cube = Cube("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")


    

cube.printcube()
