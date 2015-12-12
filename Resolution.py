#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube
import Cube

class Resolution:

    def __init__(self, state= None, cube=None):
        self.state = False      #Correspond à l'état du cube s'il est résolu ou non
        self.rubiks = Cube(cube) #créé un objet Cube issu du fichier Cube.py

#recherche l'emplacement des cases blanches pour faire une croix blanche sur le coté gauche (L)
    def etape1(self):
        print(self.rubiks.getLiCase("L",9))



res = Resolution("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")
res.etape1()

print("balbla")
