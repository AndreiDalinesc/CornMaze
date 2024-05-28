import mazeGenerator as vom
import drawLibrary as dl
import utilFuction as f

import turtle as tt
import tkinter as tk



appMaze =  tt.Screen()
appMaze.title("MazeGenerator")
appMaze.screensize(vom.dimOfMaze[0],vom.dimOfMaze[1])
mz = tt.Turtle()
mz.hideturtle()
mz.speed(0)

mid = []
for i in vom.links.keys():
    i_new = f.resize(i, 'tuple')
    for j in vom.links[i]:
        j = f.resize(j,'tuple')
        dl.drawLine(mz,i_new, j)
        mid.append(f.midSeg(i_new,j))

mz.pencolor("Green")
mz.pensize(2)

no_draw = []
dim_resize = f.resize(vom.dimOfMaze, "tuple")

# for ii in range(vom.dimOfMaze[0]+1):
#     for j in range(vom.dimOfMaze[1]+1):
#         i, j = f.resize((ii, j))
#         dl.drawPoint(mz,(i,j))



for ii in range(vom.dimOfMaze[0] + 1):
    for j in range(vom.dimOfMaze[1] + 1):
        i,j = f.resize((ii-.5,j-.5))
        # mz.pencolor("red")
        # dl.drawPoint(mz,(i,j))
        if i - f.partition >= 0 and ((i-partition,j) not in no_draw) and (f.midSeg((i,j),(i-partition,j)) not in mid):
            dl.drawLine(mz,(i,j),(i-partition,j))
        if i + f.partition < dim_resize[0] and ((i,j+partition) not in no_draw) and (f.midSeg((i,j),(i+partition,j)) not in mid):
            dl.drawLine(mz,(i,j),(i+partition,j))
        if j - f.partition >= 0 and ((i,j-partition) not in no_draw) and (f.midSeg((i,j),(i,j-partition)) not in mid):
            dl.drawLine(mz,(i,j),(i,j-partition))
        if j + f.partition < dim_resize[1] and ((i,j+partition) not in no_draw) and (f.midSeg((i,j),(i,j+partition)) not in mid):
            dl.drawLine(mz,(i,j),(i,j+partition))
        no_draw.append((i,j))


tk.mainloop()
mz.done()