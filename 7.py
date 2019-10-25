import turtle
t=turtle.Pen()
t.speed(0)
t.pencolor("red")
for x in range(100):
    t.width(2)
    t.circle(2*x)
    t.left(90)