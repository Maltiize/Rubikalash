#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,cube):
        self.rubiks = cube
        self.mouv = 0
        self.br = 0
        self.vr = 0
        self.vo = 0
        self.bo = 0

    def checkCross(self,nameFace):
        tmp=False,[]
        if(cube.checkPattern(nameFace,self.liCross)==False):
            return tmp
        m=cube.getMouv(nameFace.upper())
        for x in m[1]:
            colorEdge=cube.getCentralColor(x[0])
            if(cube.checkColorSquare(x[0],colorEdge,x[1][1])==False):
                return False
            
            tmp[1]=tmp[1]+[x[0]]
        tmp[0]=True
        return tmp

    def checkscdcouronne(self):
        if self.rubiks.front[1] == ['R','R','R'] and self.rubiks.right[1] == ['B','B','B'] and self.rubiks.back[1] == ['O','O','O'] and self.rubiks.left[1] == ['G','G','G']:
            return True
        else:
            return False

    def deuxcubeinv(self):
        #si 2 cubes sont inversé sur une 2 face opposées
        a = 0
##        br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
##        vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
##        bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange
        self.majcube()

        #si le cube bleu/rouge inversé avec le vert/rouge
        if br[0][1] == 'l' and vr[0][1] == 'r':
            a = "F"
        #si le cube bleu/rouge inversé avec le bleu/orange
        elif br[1][1] == 'b' and bo[1][1] == 'f':
            a = "R"
        #si le cube vert/orange inversé avec le bleu/orange
        elif vo[0][1] == 'r' and bo[0][1] == 'l':
            a = "B"
        #si le cube vert/orange inversé avec le vert/rouge
        elif vo[1][1] == 'f' and vr[1][1] == 'b':
            a = "L"
        if a!= 0:
            self.rubiks.rotation(str(a)+str(2))
            self.rubiks.rotation("D2")
            self.rubiks.rotation(str(a)+str(2))
            self.rubiks.rotation("D2")
            self.rubiks.rotation(str(a)+str(2))

##        #si le cube bleu/rouge inversé avec le vert/rouge
##        if br[0][1] == 'l' and vr[0][1] == 'r':
##            self.rubiks.rotation("F2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("F2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("F2")
##            self.mouv += 5
##
##        #si le cube bleu/rouge inversé avec le bleu/orange
##        if br[1][1] == 'b' and bo[1][1] == 'f':
##            self.rubiks.rotation("R2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("R2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("R2")
##            self.mouv += 5
##            
##        #si le cube vert/orange inversé avec le bleu/orange
##        if vo[0][1] == 'r' and bo[0][1] == 'l':
##            self.rubiks.rotation("B2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("B2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("B2")
##            self.mouv += 5
##
##        #si le cube vert/orange inversé avec le vert/rouge
##        if vo[1][1] == 'f' and vr[1][1] == 'b':
##            self.rubiks.rotation("L2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("L2")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("L2")
        self.mouv += 5
        self.rubiks.displayCube()
        print("2cubeinv")

    def cubeinv(self):
        #si cube au bon endroit mais couleurs inversées
##        br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
##        vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
##        bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange
        self.majcube()
        a = 0
        b = 0
        
        if self.br[0][1] == 'f' and self.br[1][1] == 'r':
            a = "F"
            b = "R"
        if self.vr[0][1] == 'f' and self.vr[1][1] == 'l':
            a = "L"
            b = "F"
        if self.vo[0][1] == 'b' and self.vo[1][1] == 'l':
            a = "B"
            b = "L"
        if self.bo[0][1] == 'b' and self.bo[1][1] == 'r':
            a = "R"
            b = "B"
        if a != 0:
            self.rubiks.rotation(str(a))
            self.rubiks.rotation("D")
            self.rubiks.rotation(str(a)+"'")
            self.rubiks.rotation("D2")
            self.rubiks.rotation(str(a))
            self.rubiks.rotation("D2")
            self.rubiks.rotation(str(a)+"'")
            self.rubiks.rotation("D")
            self.rubiks.rotation(str(b)+"'")
            self.rubiks.rotation("D'")
            self.rubiks.rotation(str(b))
            self.mouv += 11
            self.rubiks.displayCube()

##        if br[0][1] == 'f' and br[1][1] == 'r':
##            self.rubiks.rotation("F")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("F'")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("F")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("F'")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("R'")
##            self.rubiks.rotation("D'")
##            self.rubiks.rotation("R")
##            self.mouv += 11
##            self.rubiks.displayCube()
##
##        if vr[0][1] == 'f' and vr[1][1] == 'l':
##            self.rubiks.rotation("L")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("L'")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("L")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("L'")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("F'")
##            self.rubiks.rotation("D'")
##            self.rubiks.rotation("F")
##            self.mouv += 11
##            self.rubiks.displayCube()
##
##        if vo[0][1] == 'b' and vo[1][1] == 'l':
##            self.rubiks.rotation("B")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("B'")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("B")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("B'")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("L'")
##            self.rubiks.rotation("D'")
##            self.rubiks.rotation("L")
##            self.mouv += 11
##            self.rubiks.displayCube()
##
##        if bo[0][1] == 'b' and bo[1][1] == 'r':
##            self.rubiks.rotation("R")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("R'")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("R")
##            self.rubiks.rotation("D2")
##            self.rubiks.rotation("R'")
##            self.rubiks.rotation("D")
##            self.rubiks.rotation("B'")
##            self.rubiks.rotation("D'")
##            self.rubiks.rotation("B")
##            self.mouv += 11
##            self.rubiks.displayCube()
            
        print("cubeinv")
    
    def deuxcouronne(self):
        
        #peut creer une fonction maj pour savoir ou sont les 4 cubes ? utile?
##        br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
##        vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
##        vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
##        bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange
        self.majcube()
        while not self.checkscdcouronne():
            while self.br[0][1] == 'd' or self.br[1][1] == 'd' or self.vr[0][1] == 'd' or self.vr[1][1] == 'd' or self.vo[0][1] == 'd' or self.vo[1][1] == 'd' or self.bo[0][1] == 'd' or self.bo[1][1] == 'd':
                self.deuxiemecouronne()
                self.majcube()
##                br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
##                vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
##                vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
##                bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange
            self.rubiks.displayCube()
            if self.checkscdcouronne():
                break
            self.cubeinv()
            if self.checkscdcouronne():
                break
            self.rubiks.displayCube()
            self.deuxcubeinv()
            self.rubiks.displayCube()

        print(self.mouv)
        return self.rubiks
    
    def majcube(self):
        self.br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
        self.vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
        self.vo = self.rubiks.findCube(['G', 'O']) #cube vert/orang
        self.bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange

    def deuxiemecouronne(self):
    #regarder les 4 coins au dessus et si il n'y a pas de jaune la bouger au bon endroit

            #cube bleu/rouge
            br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
            #on remet le cube bleu/rouge sur sa face correspondante 
            if br[0][1] == 'd':  #ici le cube bleu est sur la face down
                self.mouv += 9
                #if br[1][1] == 'f':
                    #ne rien faire car bon endroit
                if br[1][1] == 'l':
                    #faire
                    self.rubiks.rotation("D")
                elif br[1][1] == 'b':
                    #faire
                    self.rubiks.rotation("D2")
                elif br[1][1] == 'r':
                    #faire
                    self.rubiks.rotation("D'")
                    self.rubiks.printCube()
                #on doit faire basculer le cube a gauche/ au dessus du rouge
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("R")
                self.rubiks.rotation("D")
                self.rubiks.rotation("F")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("F'")
                self.rubiks.displayCube()

                    
            elif br[1][1] == 'd': #ici le cube rouge est sur la face down
                if br[0][1] == 'f':
                    #faire
                    self.rubiks.rotation("D")
                elif br[0][1] == 'l':
                    #faire
                    self.rubiks.rotation("D2")
                elif br[0][1] == 'b':
                    #faire
                    self.rubiks.rotation("D'")
                #if a[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a droite
                self.rubiks.rotation("D")
                self.rubiks.rotation("F")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("F'")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("R")
                self.rubiks.displayCube()

            
            #cube vert/rouge
            vr = self.rubiks.findCube(['G', 'R']) #cube vert/rouge
            #on remet le cube vert/rouge sur sa face correspondante
            if vr[0][1] == 'd':  #ici le cube vert est sur la face down

                self.mouv += 9
                
                if vr[1][1] == 'l':
                    #faire
                    self.rubiks.rotation("D")
                elif vr[1][1] == 'b':
                    #faire
                    self.rubiks.rotation("D2")
                elif vr[1][1] == 'r':
                    #faire
                    self.rubiks.rotation("D'")
                #on doit faire basculer le cube a droite
                self.rubiks.rotation("D")
                self.rubiks.rotation("L")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("L'")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("F'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("F")
                self.rubiks.displayCube()
            elif vr[1][1] == 'd': #ici le cube rouge est sur la face down
                if vr[0][1] == 'f':
                    #faire
                    self.rubiks.rotation("D'")
                elif vr[0][1] == 'r':
                    #faire
                    self.rubiks.rotation("D2")
                elif vr[0][1] == 'b':
                    #faire
                    self.rubiks.rotation("D")
                #elif a[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a gauche
                self.rubiks.rotation("D'")
                self.rubiks.rotation("F'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("F")
                self.rubiks.rotation("D")
                self.rubiks.rotation("L")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("L'")
                self.rubiks.displayCube()

            #cube vert/orange
            vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
                #on remet le cube vert/orange sur sa face correspondante 
            if vo[0][1] == 'd':  #ici le cube vert est sur la face down
                self.mouv += 8
                if vo[1][1] == 'f':
                     #faire
                    self.rubiks.rotation("D2")
                elif vo[1][1] == 'l':
                    #faire
                    self.rubiks.rotation("D'")
                #if vr[1][1] == 'b':
                   #ne rien faire car bon endroit
                elif vo[1][1] == 'r':
                    #faire
                    self.rubiks.rotation("D")
                #on doit faire basculer le cube a gauche
                self.rubiks.rotation("D'")
                self.rubiks.rotation("L'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("L")
                self.rubiks.rotation("D")
                self.rubiks.rotation("B")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("B'")
                self.rubiks.displayCube()
                
            elif vo[1][1] == 'd': #ici le cube orange est sur la face down
                if vo[0][1] == 'f':
                    #faire
                    self.rubiks.rotation("D'")
                elif vo[0][1] == 'r':
                    #faire
                    self.rubiks.rotation("D2")
                elif vo[0][1] == 'b':
                    #faire
                    self.rubiks.rotation("D")
                #if vo[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a droite
                self.rubiks.rotation("D")
                self.rubiks.rotation("B")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("B'")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("L'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("L")
                self.rubiks.displayCube()

            #cube bleu/orange
            bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange
            #on remet le cube bleu/orange sur sa face correspondante 
            if bo[0][1] == 'd':  #ici le cube bleu est sur la face down
                self.mouv += 8
                if bo[1][1] == 'f':
                     #faire
                    self.rubiks.rotation("D2")
                elif bo[1][1] == 'l':
                    #faire
                    self.rubiks.rotation("D'")
                #if bo[1][1] == 'b':
                   #ne rien faire car bon endroit
                elif bo[1][1] == 'r':
                    #faire
                    self.rubiks.rotation("D")
                    #on doit faire basculer le cube a droite
                self.rubiks.rotation("D")
                self.rubiks.rotation("R")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R'")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("B'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("B")
                self.rubiks.displayCube()
            
            elif bo[1][1] == 'd': #ici le cube orange est sur la face down
                if bo[0][1] == 'f':
                    #faire
                    self.rubiks.rotation("D")
                #if bo[0][1] == 'r':
                    #ne rien faire
                elif bo[0][1] == 'b':
                    #faire
                    self.rubiks.rotation("D'")
                elif bo[0][1] == 'l':
                    #faire
                    self.rubiks.rotation("D2")
                #on doit faire basculer le cube a gauche
                self.rubiks.rotation("D'")
                self.rubiks.rotation("B'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("B")
                self.rubiks.rotation("D")
                self.rubiks.rotation("R")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R'")
                self.rubiks.displayCube()
            print("2couronne")   
            #return self.rubiks
        


#cube = Cube("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")
#cube1 = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRBYBBOOOGGRYRBORYBOOGYYYYRYYB")
#cube1.printCube()
#resol = Resolution(cube1)
#resol.deuxiemecouronne()
#cube1.printCube()
cube2 = Cube("WWWWWWWWWGGGRRRBBBOOOGGBYRBRBYROYRYYOBRYROYGYGOGOYGBOB")
cube2.displayCube()
resol = Resolution(cube2)
print(resol.checkscdcouronne())
resol.deuxcouronne()
cube2.displayCube()
print(resol.checkscdcouronne())
