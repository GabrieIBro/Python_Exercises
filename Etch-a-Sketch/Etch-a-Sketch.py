import turtle

bob = turtle.Turtle()
screen = turtle.Screen()
bob.pensize(2)

def forward():
    bob.forward(10)


def backward():
    bob.backward(10)


def left():
    bob.left(36)


def right():
    bob.right(36)


def curve_left():
    bob.forward(10)
    bob.left(10)


def curve_right():
    bob.forward(10)
    bob.right(10)


def clear():
    screen.reset()
    bob.pensize(2)


screen.listen()

screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(curve_left, "q")
screen.onkeypress(curve_right, "e")
screen.onkeypress(clear, "c")

screen.exitonclick()
