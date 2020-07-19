
import turtle


wn=turtle.Screen()
wn.title("Pong game by Nahin")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

score_left=0
score_right=0

#Left paddle
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid= 5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-360,0)

#right paddle
right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid= 5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(360,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=.2
ball.dy=-.2

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("Player A:0 and Player B:0", align="center",font=("Courier",24,"normal"))

#function for moving left and right paddle

def left_paddle_up(): #moving for left paddle up
    y=left_paddle.ycor()
    y+=20
    left_paddle.sety(y)


def left_paddle_down():  # moving for left paddle down
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up(): #moving for right paddle up
    y=right_paddle.ycor()
    y+=20
    right_paddle.sety(y)

def right_paddle_down():  # moving for right paddle down
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(left_paddle_up,"w") # calling the up function to moving the left paddle up
wn.onkeypress(left_paddle_down,"s") #calling the down function to moving the left paddle down
wn.onkeypress(right_paddle_up,"Up") # calling the up function to moving the right paddle up
wn.onkeypress(right_paddle_down,"Down") # calling the up function to moving the left paddle dowm





#main game loop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx*=-1
        score_left+=1
        pen.clear()
        pen.write("Player A:{} and Player B:{}".format(score_left,score_right), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right+=1
        pen.clear()
        pen.write("Player A:{} and Player B:{}".format(score_left, score_right), align="center",font=("Courier", 24, "normal"))

    #bouncing ball off the paddles
    if (ball.xcor()>340 and ball.xcor() <350) and (ball.ycor() <right_paddle.ycor() +40 and ball.ycor() >right_paddle.ycor() -40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1






