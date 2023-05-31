import turtle
from random import random

# -----------------------------------------------------initialisation

# screen
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("#302e28")
# wind.bgpic("wall1.gif")
width = 1350
height = 700
wind.setup(width=width, height=height)
wind.tracer(0)

# racquet 1
racquet1 = turtle.Turtle()
racquet1.speed(0)
racquet1.shape("square")
racquet1.color("#244ac7")
racquet1.shapesize(stretch_wid=5, stretch_len=1)
racquet1.penup()
racquet1.goto(-(width // 2 - 50), 0)

# racquet 2
racquet2 = turtle.Turtle()
racquet2.speed(0)
racquet2.shape("square")
racquet2.color("#c43421")
racquet2.shapesize(stretch_wid=5, stretch_len=1)
racquet2.penup()
racquet2.goto((width // 2 - 50), 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
x = 0.9
y = 0.2
ball.dx = x
ball.dy = y

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("0\t:\t0", align="center", font=("Courier", 24, "normal"))


# -----------------------------------------------functionality
def racquet1_up():
    if racquet1.ycor() + 50 < height / 2:
        y = racquet1.ycor()
        y += 20
        racquet1.sety(y)


def racquet1_down():
    if racquet1.ycor() - 50 > -(height / 2):
        y = racquet1.ycor()
        y -= 20
        racquet1.sety(y)


def racquet2_up():
    if racquet2.ycor() + 50 < (height / 2):
        y = racquet2.ycor()
        y += 20
        racquet2.sety(y)


def racquet2_down():
    if racquet2.ycor() - 50 > -(height / 2):
        y = racquet2.ycor()
        y -= 20
        racquet2.sety(y)


# # other racquet
# racquet = turtle.Turtle()
# racquet.speed(10)
# racquet.shape("square")
# racquet.color("white")
# racquet.shapesize(stretch_wid=5, stretch_len=1)
# racquet.penup()
# racquet.goto(0, 0)

# def racquet_degre():
#     # racquet.setheading(40)
#     # racquet.left(45)
#     racquet.forward(100)
#     # racquet.backward(100)
#     # racquet.circle(30)

# pressing
wind.listen()
wind.onkeypress(racquet1_up, "a")
wind.onkeypress(racquet1_down, "q")
wind.onkeypress(racquet2_up, "6")
wind.onkeypress(racquet2_down, "3")

'''''''''
def fastShootR1(racquet2_position):
    ball.dy = random() * ball.dx
    ball.dx = ball.dx + 2
    if ball.dx >= racquet2_position - 10:
        ball.dx = x
        ball.dy = y
'''
'''''''''
def fastShootR2(racquet1_position):
    ball.dy = random() * ball.dx
    ball.dx = ball.dx + 2
    if ball.dx <= racquet1_position + 10:
        ball.dx = x
        ball.dy = y
'''
i = 0
while True:
    wind.update()
    i += 1

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > (height / 2 - 10):
        ball.dy *= -1

    if ball.ycor() < -(height / 2 - 10):
        ball.dy *= -1

    if ball.xcor() < (racquet1.xcor() + 20):
        i += 1
        if racquet1.ycor() + 50 >= ball.ycor() >= racquet1.ycor() - 50:
            ball.dx *= -1
        elif ball.xcor() < -670:
            score2 += 1
            score.clear()
            score.write(f"{score1}\t:\t{score2}", align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)

    if ball.xcor() > (racquet2.xcor() - 20):
        i += 1
        if racquet2.ycor() + 50 >= ball.ycor() >= racquet2.ycor() - 50:
            ball.dx *= -1
        elif ball.xcor() > 670:
            score1 += 1
            score.clear()
            score.write(f"{score1}\t:\t{score2}", align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
