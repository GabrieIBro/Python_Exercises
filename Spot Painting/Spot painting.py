import colorgram as cg
import turtle as tt
import random as rd

colors = cg.extract("hirst.jpg", 10)
rgb = []

for pos, item in enumerate(colors):
    color = colors[pos]
    rgb.append(color.rgb)


bob = tt.Turtle()
screen = tt.Screen()
screen.colormode(255)
screen.bgcolor("black")

bob.speed(11)
pos_y = 240

for a in range(9):
    bob.penup()
    bob.goto(-305, pos_y)
    pos_y -= 60
    bob.pendown()

    for _ in range(11):
        bob.color(rd.choice(rgb))
        bob.dot(34)
        bob.penup()
        bob.forward(60)

screen.exitonclick()
