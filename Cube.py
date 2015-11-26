class Cube:


    # 0 si jamais la couleur n'a pas encore été indiquée 
    def __init__(self, cube=None):

        #plages d'indexes de toutes les cases correspondantes à chaque face
        # CF schéma dans madoc 

        self.idxu=range(0,7)
        self.idxd=range(40,47)
        self.idxf=[11,12,13,22,23,31,32,33]
        self.idxl=[8,9,10,20,21,28,29,30]
        self.idxr=[14,15,16,24,25,34,35,36]
        self.idxb=[17,18,19,26,27,37,38,39]

        
        #Initialisation des faces à 0
        
        self.up=[0,0,0],[0,"U",0],[0,0,0] 
        self.down=[0,0,0],[0,"D",0],[0,0,0]
        self.front=[0,0,0],[0,"F",0],[0,0,0]
        self.left=[0,0,0],[0,"L",0],[0,0,0]
        self.right=[0,0,0],[0,"R",0],[0,0,0]
        self.back=[0,0,0],[0,"B",0],[0,0,0]


        #Si aucunes configuration de départ n'a été renseignée
        
        if(Cube==None):
            return

        self.origin=cube

        
        up=setface(idxu,up)
        down=setface(idxd,down)
        front=setface(idxf,front)
        left=setface(idxl,left)
        right=setface(idxr,right)
        back=setface(idxb,back)


    # Cette methode remplis chaque face avec les éléments qui lui correspondent 
    # ( renseignés dans les listes idx[nomface] )

    def setface(self,idx,face):
        if(len(idx)!=8):
            print("INVALID SIZE ON IDX")
            return -1
        
        i=0
        j=0
        for val in idx:
            
            # cette condition sert à "sauter" la case avec le nom de la face
            # R L F B U ou D
            
            if(face[j][i]==0): 
                face[j][i]=self.origin[val]
            else:
                
                # si on tombe sur la case avec le nom de la face
                # on remplis la case juste apres
                # et on saute une ligne (j+1)
                
                face[j][i+1]=self.origin[val]
                j=j+1
                
            #on passe à la case suivante   
            i=i+1
            
            if(i%3==0):
                
                # si on arrive à la fin d'une ligne
                # on passe à la suivante
                
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

