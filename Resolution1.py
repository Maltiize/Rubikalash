#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,cube):
        self.rubiks = cube


    def checkscdcouronne(self):
        if self.rubiks.front[1] == ['R','R','R'] and self.rubiks.right[1] == ['B','B','B'] and self.rubiks.back[1] == ['O','O','O'] and self.rubiks.left[1] == ['G','G','G']:
            return True
        else:
            return False

    def deuxcubeinv(self):
        #si 2 cubes sont inversé sur une 2 face opposées
        
        br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
        vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
        vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
        bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange

        #si le cube bleu/rouge inversé avec le vert/rouge
        if br[0][1] == 'l' and vr[0][1] == 'r':
            self.rubiks.rotation("F2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("F2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("F2")

        #si le cube bleu/rouge inversé avec le bleu/orange
        if br[1][1] == 'b' and bo[1][1] == 'f':
            self.rubiks.rotation("R2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("R2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("R2")
            
        #si le cube vert/orange inversé avec le bleu/orange
        if vo[0][1] == 'r' and bo[0][1] == 'l':
            self.rubiks.rotation("B2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("B2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("B2")

        #si le cube vert/orange inversé avec le vert/rouge
        if vo[1][1] == 'f' and vr[1][1] == 'b':
            self.rubiks.rotation("L2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("L2")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("L2")

    def cubeinv(self):
        #si cube au bon endroit mais couleurs inversées
        br = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
        vr = self.rubiks.findCube(['G', 'R']) #vert/rouge
        vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
        bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange

        if br[0][1] == 'f' and br[1][1] == 'r':
            self.rubiks.rotation("F")
            self.rubiks.rotation("D")
            self.rubiks.rotation("F'")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("F")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("F'")
            self.rubiks.rotation("D")
            self.rubiks.rotation("R'")
            self.rubiks.rotation("D'")
            self.rubiks.rotation("R")

        if vr[0][1] == 'f' and vr[1][1] == 'l':
            self.rubiks.rotation("L")
            self.rubiks.rotation("D")
            self.rubiks.rotation("L'")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("L")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("L'")
            self.rubiks.rotation("D")
            self.rubiks.rotation("F'")
            self.rubiks.rotation("D'")
            self.rubiks.rotation("F")

        if vo[0][1] == 'b' and vo[1][1] == 'l':
            self.rubiks.rotation("B")
            self.rubiks.rotation("D")
            self.rubiks.rotation("B'")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("B")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("B'")
            self.rubiks.rotation("D")
            self.rubiks.rotation("L'")
            self.rubiks.rotation("D'")
            self.rubiks.rotation("L")

        if bo[0][1] == 'b' and bo[1][1] == 'r':
            self.rubiks.rotation("R")
            self.rubiks.rotation("D")
            self.rubiks.rotation("R'")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("R")
            self.rubiks.rotation("D2")
            self.rubiks.rotation("R'")
            self.rubiks.rotation("D")
            self.rubiks.rotation("B'")
            self.rubiks.rotation("D'")
            self.rubiks.rotation("B")
            
        return self.rubiks
            

    def deuxiemecouronne(self):
    #regarder les 4 coins au dessus et si il n'y a pas de jaune la bouger au bon endroit
        #print(self.rubiks.getLiCase('u', 9))
        #while not self.rubiks.checkscdcouronne():#tant que la 2eme couronne n'est pas fini

            #cube bleu/rouge
            a = self.rubiks.findCube(['B', 'R']) #cube bleu/rouge
            #on remet le cube bleu/rouge sur sa face correspondante 
            if a[0][1] == 'd':  #ici le cube bleu est sur la face down
                #if a[1][1] == 'f':
                    #ne rien faire car bon endroit
                if a[1][1] == 'l':
                    #faire
                    self.rubiks.rotation("D")
                elif a[1][1] == 'b':
                    #faire
                    self.rubiks.rotation("D2")
                elif a[1][1] == 'r':
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
                    
            elif a[1][1] == 'd': #ici le cube rouge est sur la face down
                if a[0][1] == 'f':
                    #faire
                    self.rubiks.rotation("D")
                elif a[0][1] == 'l':
                    #faire
                    self.rubiks.rotation("D2")
                elif a[0][1] == 'b':
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
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R")
                 #if self.rubiks.down[0][1] == 'B' and self.rubiks.back[0][1] == '
                  #   self.rubiks.rotation(
            #return self.rubiks.down[2][0]
            
            #cube vert/rouge
            vr = self.rubiks.findCube(['G', 'R']) #cube vert/rouge
            #on remet le cube vert/rouge sur sa face correspondante 
            if vr[0][1] == 'd':  #ici le cube vert est sur la face down
                #if vr[1][1] == 'f':
                    #ne rien faire car bon endroit
                if vr[1][1] == 'l':
                    #faire
                    self.rubiks.rotation("D")
                if vr[1][1] == 'b':
                    #faire
                    self.rubiks.rotation("D2")
                if vr[1][1] == 'r':
                    #faire
                    self.rubiks.rotation("D'")
                #on doit faire basculer le cube a droite
                self.rubiks.rotation("D")
                self.rubiks.rotation("R")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R'")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("F'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("F")
            elif vr[1][1] == 'd': #ici le cube rouge est sur la face down
                if vr[0][1] == 'f':
                    #faire
                    self.rubiks.rotation("D")
                if vr[0][1] == 'l':
                    #faire
                    self.rubiks.rotation("D2")
                if vr[0][1] == 'b':
                    #faire
                    self.rubiks.rotation("D'")
                #if a[0][1] == 'r':
                    #ne rien faire
                #on doit faire basculer le cube a gauche
                self.rubiks.rotation("D'")
                self.rubiks.rotation("F'")
                self.rubiks.rotation("D")
                self.rubiks.rotation("F")
                self.rubiks.rotation("D")
                self.rubiks.rotation("R")
                self.rubiks.rotation("D'")
                self.rubiks.rotation("R'")

            #cube vert/orange
                vo = self.rubiks.findCube(['G', 'O']) #cube vert/orange
                #on remet le cube vert/orange sur sa face correspondante 
                if vo[0][1] == 'd':  #ici le cube vert est sur la face down
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
                if vo[1][1] == 'd': #ici le cube orange est sur la face down
                    if vo[0][1] == 'f':
                        #faire
                        self.rubiks.rotation("D")
                    elif vo[0][1] == 'l':
                        #faire
                        self.rubiks.rotation("D2")
                    elif vo[0][1] == 'b':
                        #faire
                        self.rubiks.rotation("D'")
                    #if a[0][1] == 'r':
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

            #cube bleu/orange
                bo = self.rubiks.findCube(['B', 'O']) #cube bleu/orange
                #on remet le cube bleu/orange sur sa face correspondante 
                if bo[0][1] == 'd':  #ici le cube bleu est sur la face down
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
                
                elif bo[1][1] == 'd': #ici le cube orange est sur la face down
                    if bo[0][1] == 'f':
                        #faire
                        self.rubiks.rotation("D'")
                    #if bo[0][1] == 'l':
                        #ne rien faire
                    elif bo[0][1] == 'b':
                        #faire
                        self.rubiks.rotation("D")
                    elif bo[0][1] == 'r':
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
                
            return self.rubiks
        



cube1 = Cube("WW1WW2WW3GGGRRRBBBOOOGGGRRBYBBOOOGGRYRBORYBOOGYYYYRYYB")

cube1.printCube()
cube1.rotation("R")

cube1.printCube()
#print(vr[0][1])
#print(va[0][1])
#resol = Resolution(cube1)
#resol.deuxiemecouronne()
#cube1.printCube()
#cube2 = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRYBBOOOGGGRRRBBBOOOYBYYYYYYY")
#cube1.printCube()
#resol = Resolution(cube1)
##print(resol.checkscdcouronne())
#resol.deuxiemecouronne()
#cube1.printCube()
##print(resol.checkscdcouronne())
a=cube1.findCube(['B', 'W',])

        
        