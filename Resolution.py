#récupère le cube de départ entrée par l'utilisateur dans InterfaceIO
#et renvoie à InterfaceIO la résolution du cube

from Cube import Cube
class Resolution:

    def __init__(self,c):
        self.cube=c




    def retournerDeuxAretes(self,nameFace):
        print("cube.rotation")
        
        
        


cube = Cube("GGGGGGGGGOOOOOOOOOYYYYYYYYYRRRRRRRRRBBBBBBBBBWWWWWWWWW")

resolution = Resolution(cube)

cube.printCube()
        
        
