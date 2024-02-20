import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

def draw_square(t,size):
    for i in range(4):
        alex.forward(size)
        alex.left(90)

size = 20
for i in range(5):
   draw_square(alex,size)
   size = size + 20
   alex.penup()
   alex.backward(10)
   alex.right(90)
   alex.forward(10)
   alex.left(90)
   alex.pendown()
   
wn.mainloop()
