import turtle
t=turtle.Pen()
t.speed(0)
colors=["red","black","blue","orange","green","purple","pink"]
sides=7
number_of_circles=int(turtle.numinput("number of circles","how many circles in your rosett/?,1"))
for x in range(number_of_circles):
        t.pencolor(colors[x%sides])
        t.forward(x)
        t.left(60)
        t.circle(100)
        t.width(2)