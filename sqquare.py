import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("lightblue")
t.color("red")
t.pensize(3)

i = 1
while i <= 4:
    t.forward(100)
    t.right(90)
    i = i + 1

t.hideturtle()
turtle.done()