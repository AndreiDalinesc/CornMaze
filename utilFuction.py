import mazeGenerator as vom

partition = 30
def midSeg(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def resize(p1, reType = ""):
    if reType == 'tuple':
        return (p1[0]*partition-vom.dimOfMaze[0]*partition/2,p1[1]*partition-vom.dimOfMaze[1]*partition/2)
    else:
        return p1[0]*partition-vom.dimOfMaze[0]*partition/2,p1[1]*partition-vom.dimOfMaze[1]*partition/2
