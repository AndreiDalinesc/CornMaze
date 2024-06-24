import turtle as tt
import tkinter as tk
import svgReader as r

def drawLine(canva,p1,p2):
    canva.penup()
    canva.goto((p1[0],p1[1]))
    canva.write(str(p1[0])+","+str(p1[1])+"\n")
    canva.pendown()
    canva.goto((p2[0],p2[1]))
    canva.write(str(p2[0])+","+str(p2[1])+"\n")

appMaze =  tt.Screen()
appMaze.title("MazeGenerator")
appMaze.screensize(10000,10000)
mz = tt.Turtle()
mz.hideturtle()
mz.speed(0)

for i in r.line_list:
    drawLine(mz,i[0],i[1])

tk.mainloop()
mz.done()