import turtle
t=turtle.Pen()
t.speed(0)
colors=["red","black","blue","orange","green","purple","pink"]
for x in range(200):
    sides=6
    t.pencolor(colors[x%sides])
    t.width(2)
    t.forward(x)
    t.left(60)