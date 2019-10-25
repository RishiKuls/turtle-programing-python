import turtle
t=turtle.Pen()
t.speed(0)
for x in range(200):
    colors=["red","black","blue","orange","green","purple","pink"]
    sides=2
    t.pencolor(colors[x%sides])
    t.width(2)
    t.forward(2*x)
    t.left(90)