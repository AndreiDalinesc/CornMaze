import mazeGenerator as vom

def drawLine(canva,p1,p2):
    canva.penup()
    canva.goto((p1[0] - vom.dimOfMaze[0]/2, p1[1] - vom.dimOfMaze[0]/2))
    canva.pendown()
    canva.goto((p2[0] - vom.dimOfMaze[0]/2, p2[1] - vom.dimOfMaze[0]/2))

def drawPoint(canva,p1):
    canva.penup()
    canva.goto((p1[0] - vom.dimOfMaze[0]/2, p1[1] - vom.dimOfMaze[0]/2))
    canva.pendown()
    canva.circle(2)