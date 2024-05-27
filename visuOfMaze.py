import mazeGenerator as vom
import turtle as tt
import tkinter as tk

partition = 30

def drawLine(p1,p2):
    mz.penup()
    mz.goto((p1[0] - vom.dimOfMaze[0]/2, p1[1] - vom.dimOfMaze[0]/2))
    mz.pendown()
    mz.goto((p2[0] - vom.dimOfMaze[0]/2, p2[1] - vom.dimOfMaze[0]/2))

def drawPoint(p1):
    mz.penup()
    mz.goto((p1[0] - vom.dimOfMaze[0]/2, p1[1] - vom.dimOfMaze[0]/2))
    mz.pendown()
    mz.circle(2)

def midSeg(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def resize(p1, reType = ""):
    if reType == 'tuple':
        return (p1[0]*partition-vom.dimOfMaze[0]*partition/2,p1[1]*partition-vom.dimOfMaze[1]*partition/2)
    else:
        return p1[0]*partition-vom.dimOfMaze[0]*partition/2,p1[1]*partition-vom.dimOfMaze[1]*partition/2

appMaze =  tt.Screen()
appMaze.title("MazeGenerator")
appMaze.screensize(vom.dimOfMaze[0],vom.dimOfMaze[1])
mz = tt.Turtle()
mz.hideturtle()
mz.speed(0)

mid = []
for i in vom.links.keys():
    i_new = resize(i, 'tuple')
    for j in vom.links[i]:
        j = resize(j,'tuple')
        drawLine(i_new, j)
        mid.append(midSeg(i_new,j))

mz.pencolor("Green")
mz.pensize(2)

no_draw = []
dim_resize = resize(vom.dimOfMaze, "tuple")

# for ii in range(vom.dimOfMaze[0]+1):
#     for j in range(vom.dimOfMaze[1]+1):
#         i, j = resize((ii, j))
#         drawPoint((i,j))



for ii in range(vom.dimOfMaze[0] + 1):
    for j in range(vom.dimOfMaze[1] + 1):
        i,j = resize((ii-.5,j-.5))
        # mz.pencolor("red")
        # drawPoint((i,j))
        if i - partition >= 0 and ((i-partition,j) not in no_draw) and (midSeg((i,j),(i-partition,j)) not in mid):
            drawLine((i,j),(i-partition,j))
        if i + partition < dim_resize[0] and ((i,j+partition) not in no_draw) and (midSeg((i,j),(i+partition,j)) not in mid):
            drawLine((i,j),(i+partition,j))
        if j - partition >= 0 and ((i,j-partition) not in no_draw) and (midSeg((i,j),(i,j-partition)) not in mid):
            drawLine((i,j),(i,j-partition))
        if j + partition < dim_resize[1] and ((i,j+partition) not in no_draw) and (midSeg((i,j),(i,j+partition)) not in mid):
            drawLine((i,j),(i,j+partition))
        no_draw.append((i,j))


tk.mainloop()
mz.done()