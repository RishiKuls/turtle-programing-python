import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors=["red","black","blue","orange","green","purple","pink"]
your_name=turtle.textinput("enter your name","what is your name")
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.width(3)#3
    t.forward(x*4)#x
    t.left(92)#50
    t.pendown()
    t.write(your_name,font=("times",int((x+4)/4),"bold"))