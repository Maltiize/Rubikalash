from Cube import *
def rplace(cube):
        c=Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")
        f1=cube.front
        u1=cube.up
        f=f1[1][1]
        u=u1[1][1]
        if u=='W':
            if f=='O':
                c.right=cube.left
                c.front=cube.back
                c.left=cube.right
                c.back=cube.front
            elif f=='B':
                c.front=cube.left
                c.right=cube.front
                c.back=cube.right
                c.left=cube.back
            elif f=='G':
                c.front=cube.right
                c.right=cube.back
                c.back=cube.left
                c.left=cube.front
        elif u=='R':
            c.front=cube.up
            c.back=cube.down
            if f=='Y':
                c.up=cube.back
                c.down=cube.front
            elif f=='G':
                c.up=cube.left
                c.right=cube.back
                c.left=cube.front
                c.down=cube.right
            elif f=='W':
                c.up=cube.front
                c.right=cube.left
                c.left=cube.right
                c.down=cube.back
            elif f=='B':
                c.up=cube.right
                c.right=cube.front
                c.left=cube.back
                c.down=cube.left
        elif u=='Y':
            c.up=cube.down
            c.down=cube.up
            if f=='Y':
                c.right=cube.left
                c.left=cub.right
            elif f=='B':
                c.front=cube.right
                c.right=cube.front
                c.back=cube.left
                c.left=cube.back
            elif f=='O':
                c.front=cube.back
                c.back=cube.front
            elif f=='G':
                c.front=cube.left
                c.right=cube.back
                c.back=cube.right
                c.left=cube.front
        elif u=='O':
            c.back=cube.up
            c.front=cube.down
            if f=='G':
                c.up=cube.right
                c.left=cube.front
                c.right=cube.back
                c.displayCube()
                c.down=cube.left
            elif f=='Y':
                c.up=cube.back
                c.left=cube.right
                c.right=cube.left
                c.down=cube.front
            elif f=='B':
                c.up=cube.left
                c.left=cube.back
                c.right=cube.front
                c.down=cuube.right
            elif f=='W':
                c.up=cube.left
                c.down=c.back
        elif u=='G':
            c.left=cube.up
            c.right=cube.down
            if f=='W':
                c.front=cube.left
                c.back=cube.right
                c.up=cube.front
                c.down=cube.back
            elif f=='R':
                c.up=cube.right
                c.down=cube.left
            elif f=='Y':
                c.front=cube.right
                c.back=cube.left
                c.up=cube.back
                c.down=cube.front
            elif f=='O':
                c.front=cube.back
                c.back=cube.front
                c.up=cube.left
                c.down=cube.right
        elif u=='B':
            c.right=cube.up
            c.left=cube.down
            if f=='R':
                c.up=cube.left
                c.down=cube.right
            elif f=='W':
                c.up=cube.front
                c.down=cube.back
                c.front=cube.right
                c.back=cube.left
            elif f=='O':
                c.up=cube.right
                c.down=cube.left
                c.front=cube.back
                c.back=cube.front
            elif f=='Y':
                c.up=cube.back
                c.down=cube.front
                c.front=cube.left
                c.back=cube.right
        
        return(c)
cube1 = Cube("OOOOOOOOOYYYGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBRRRRRRRRR")
#cube1.displayCube()
#rplace(cube1)
L=[[0,2],[1,2]]
l=[[1,3],[1,2]]
l[0][1]=L[0][1]
#print(l,L)
