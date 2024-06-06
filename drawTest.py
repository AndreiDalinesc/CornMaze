import turtle as tt
import tkinter as tk
import svgReader as r

a=1

def drawLine(canva,p1,p2):
    canva.penup()
    canva.goto((p1[0],p1[1]))
    canva.pendown()
    canva.goto((p2[0],p2[1]))

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