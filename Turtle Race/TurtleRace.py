import turtle as tt
from random import randint

screen = tt.Screen()
screen.bgcolor("black")

screen.textinput("BET", "Choose your color: Pink | Red | Green | Blue | Yellow")

blue_turtle = tt.Turtle()
green_turtle = tt.Turtle()
red_turtle = tt.Turtle()
yellow_turtle = tt.Turtle()
pink_turtle = tt.Turtle()
white_turtle = tt.Turtle()

white_turtle.color("white")
white_turtle.speed(11)
white_turtle.pensize(4)
white_turtle.penup()
white_turtle.goto(270, 270)
white_turtle.pendown()
white_turtle.goto(270, -260)
white_turtle.hideturtle()

turtles = [pink_turtle, red_turtle, green_turtle, blue_turtle, yellow_turtle]
colors = ["pink", "red", "green", "blue", "yellow"]
y_pos = 100
stop = 0

for index, item in enumerate(turtles):
    item.color(colors[index])
    item.shape("turtle")
    item.speed(11)
    item.penup()
    item.goto(-300, y_pos)
    y_pos -= 40
    item.speed(1)

while stop != 250:
    for item in turtles:

        item.pendown()
        item.forward(randint(5, 15))
        if item.xcor() > 250:
            stop = 250
            print(f"The {item.color()[0]} turtle won!")
screen.exitonclick()
