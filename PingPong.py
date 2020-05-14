
import turtle

win = turtle.Screen()
win.title("ping pong game by yash")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
'''paddle a'''
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
'''ball'''
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1
'''paddle b'''
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

''' movement'''


def paddle_a_up():
    y = paddle_a.ycor()
    if(y == 200):
        return
    y += 25
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if(y ==-200):
        return
    y -= 25
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if(y == 200):
        return
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if(y == -200):
        return
    y -= 25
    paddle_b.sety(y)


'''listener'''
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if(ball.xcor() >= 200):
        ball.sety(200)
        ball.dx =  -0.1

    if(ball.xcor()<= -200):
        ball.sety(-200)
        ball.dx = 0.1



    if(ball.xcor() <= (paddle_a.xcor() + 10)):
        ball.setx(paddle_b.xcor() + 10)
        ball.dx = 0.1
    if(ball.xcor()>=(paddle_b.xcor()-10) ):
        ball.setx(paddle_b.xcor()-10)
        ball.dx = -0.1
        ball.dy = 0.1





