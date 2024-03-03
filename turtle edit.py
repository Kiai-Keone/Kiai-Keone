import turtle

def DrawBar(t, height):
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def draw():
    data = [60, 180, 200, 120, 70, 240]

    t = turtle.Turtle()
    wn = turtle.Screen()

    for height in data:
        DrawBar(t, height)

    wn.mainloop()

draw()
