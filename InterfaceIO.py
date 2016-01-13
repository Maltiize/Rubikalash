from Resolution import *
import random
import os
class InterfaceIO:

#classe qui gère les entrées sorties avec l'utilisateur
    
    def __init__(self, entree=None, sortie=None):
        self.entry=entree
        self.output=sortie
        self.path="D:/Projet Python RUBIK'S CUBE/Rubikcube_of_death_that_kill/"
        self.file="cube.txt"

#l'utilisateur entre dans le programme la position du cube de départ
        
    def getEntry(self):
        self.entry = input("Entrez la configuration du Rubik's Cube a résoudre :")
        
        #54 correspond au nombre de cases d'un rubik's cube
        while self.checkEntry() == False:
            print("Erreur, configuration impossible.")
            self.entry = input("Réessayez : ")

#vérifie que l'entrée contient le nombre de caractères nécessaires et les bons caracteres
            
    def checkEntry(self):
        carac=["B","R","Y","W","G","O"]
        n = len(self.entry)
#On vérifie que l'entrée contient 54 caracteres
        if len(self.entry) != n :
            return False
#On verifie que les caracteres entrés sont les bons
        for i in range(n):
            if self.entry[i] not in carac:
                return False
        return True
            
#crée un Liste de cube aléatoire sous la forme de chaine de caractères 
    
    def batCube(self,nbcube=1000):
        tCube=[]
        j=0
        while (j <= nbcube) :
        
            tab = ['U','L','R','B','D','F','U2','L2','R2','B2','D2','F2',]
            cube = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")
         
            for i in range(random.randint(0,100)):
                mouv = tab[random.randint(0,11)]
                cube.rotation(mouv)
            strtmp=cube.getStr()
            
            if strtmp not in tCube :
                tCube.append(strtmp)
                j+=1
            
        
        writeTab(tCube,self.path,self.file)
               
        return tCube

    #fait une resolution pour chaque cube present dans la liste en entré
    def batTest(self,TCube=None):
        nbfini=0
        nbmvt=0
        Tfail=[]
        if(TCube==None):
            TCube=getCubeFile(self.path+self.file)
            print("nbcube à tester : ",len(TCube))
        for idi,i in enumerate (TCube) :
            self.output = resolutionFinale(i)
            if self.output[1]==True:
                nbfini+=1
            else :
                Tfail.append(i)
            nbmvt+=self.output[2]
            print("cube num : ",nbfini)
            print("moyfini : ",nbfini/(idi+1))
            print("moymvt : ",nbmvt/(nbfini))
            
#renvoie les mouvements a faire a l'utilisateur      
    def setOutput(self):
        
        self.output = resolutionFinale("WROWWOGYYGGRWGRGWWBBOGGOYRYBBWBORORBRWRBOOGGBWRYYYBYOY")
        #self.output = resolutionFinale("BBGYWWYWWYGGOOOGGYRORYGBRRRGBWROOWBBOROBBWRORYYWYYWBGG")
        #self.output = resolutionFinale("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY", "B2 F D B' L F L B' R U F' B D2 L' F2 B2 U R2 L F B2 L2 U2 R' U'")
##        self.output = resolutionFinale("D2 L U2 B' U L2 R' D2 B D2 B2 F' L' D' R2 L' U2 B2 D' U' F' L' F2 B' R'")
##        self.output = resolutionFinale("B' R L U' B' U' R' U2 R' L2 D2 R U2 B2 D L2 U2 B2 F2 R2 F' L R' B2 R")
##        self.output = resolutionFinale("U' F U2 L' D2 L' U2 L2 D' B2 F2 R' D' F2 D' F' U2 D2 F D R2 F' R' U' L'")
##        self.output = resolutionFinale("U' L' F R2 F2 U R U B2 R' U F2 B2 R B2 F' R L U' R B U2 B F U2") #Quentin 32 mvts wtf
##        self.output = resolutionFinale("D' U2 F2 R F2 B2 R' U2 R' L2 F2 B R D2 U2 R' F U' R' L2 D2 U2 R' D2 L")
##        self.output = resolutionFinale("B' D' B' L' D2 U2 L U' D2 L F' B2 L' B2 D2 B' L' D2 L' B2 L R' U R F")
##        self.output = resolutionFinale("L' D' R' D2 R' F R2 F2 B R' L D' R2 U' R U' D' R D2 R F L F U B2")
##        self.output = resolutionFinale("B2 F2 U2 D' R2 L' F L' U' B L U2 F' U' L' U' L U B R' B' L U2 D2 L2")
##        self.output = resolutionFinale("L B F2 L F B U' L D F' D' R F U D R B2 R F2 R' L F2 R2 B2 L'")
##        self.output = resolutionFinale("U' L' R' D' L R U2 L2 R' B U L' D2 B' L' D2 L2 R' B' D' B' R L' U D")
##        self.output = resolutionFinale("D2 L U D F2 U B2 D' U2 F U R D' B L F' U' D R2 L D2 F2 R2 F2 R'")
##        self.output = resolutionFinale("U' D2 F' B' U' L2 F2 D' F' B2 L' F2 B' U F U F' B' D B2 R D2 B D' R'")
##        self.output = resolutionFinale("B U' B' R' D U2 F R L F' D2 F R2 U' R2 F2 D B L2 U2 R D B2 D' B'")
##        self.output = resolutionFinale("B2 F D B' L F L B' R U F' B D2 L' F2 B2 U R2 L F B2 L2 U2 R' U'")
##        self.output = resolutionFinale("D U F R B2 L2 B2 U B L2 D R U' D2 R B2 R' L D' F' R' F' D2 R L2")
        print(self.output)
        
        

def writeInFile(strcu,path,new=False,ficName="cube.txt"):
    if(new==True):
        mode='w'
    else :
        mode ='a'
    os.chdir(path)
    fic = open(ficName,mode) 
    fic.write(strcu)
    fic.close()

def writeTab(tab,path,ficName="cube.txt"):
    new=True
    for x in tab :
        writeInFile(x+"\n",path,new,ficName)
        new=False

     
def getCubeFile(path):
    liCube=[]
    tmp=''

    fic = open(path, 'r') # url = fichier .txt
    data = fic.read()
    fic.close()
    data.replace('\n',' ') # Remplace le 2eme parametre par le character que tu
    #veut ou laisse comme ca pour juste supprimer
    data.split()
    for x in data:
        if(x=='\n'):
            cube = Cube(tmp)
            liCube+=[tmp]
            tmp=''
        else :
            tmp+=x   
    return liCube

    

        
#bonjour = InterfaceIO()
#bonjour.getEntry()

resolutionCube = InterfaceIO()


#batTestOfBatCube=resolutionCube.batCube(10000)

#batTestOfBatCube=resolutionCube.batCube(10000)

resolutionCube.batTest()
#resolutionCube.setOutput()
#batTestOfBatCube=resolutionCube.batCube(10)
#resolutionCube.batTest()
#resolutionCube.getEntry()
#resolutionCube.setOutput()

