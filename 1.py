import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor("gray")
for x in range(360):
    colors=["red","black","blue","orange","green","purple","pink"]
    sides=7
    t.pencolor(colors[x%sides])
    t.width(x*sides/100)#3
    t.forward(x*3/sides+x)#x
    t.left(360/sides+1)#50