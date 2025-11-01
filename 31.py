import turtle
import random

# 🏁 Set up the screen
win = turtle.Screen()
win.title("Catch the Ball 🎾 by Misi")
win.bgcolor("skyblue")
win.setup(width=600, height=600)
win.tracer(0)

# 🎾 Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(random.randint(-290, 290), 250)
ball.dy = -1.2   # 🐢 Slow speed

# 🧺 Basket
basket = turtle.Turtle()
basket.shape("square")
basket.color("black")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.penup()
basket.goto(0, -250)

# 🧮 Score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Comic Sans MS", 20, "bold"))

# 🕹️ Move basket
def move_left():
    x = basket.xcor()
    x -= 40
    if x < -280:
        x = -280
    basket.setx(x)

def move_right():
    x = basket.xcor()
    x += 40
    if x > 280:
        x = 280
    basket.setx(x)

win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# 🎯 Main game loop
while True:
    win.update()

    # Ball movement
    ball.sety(ball.ycor() + ball.dy)

    # If ball hits the bottom
    if ball.ycor() < -300:
        ball.goto(random.randint(-290, 290), 250)

    # 🎾 Catch the ball
    if (ball.ycor() < -230 and ball.ycor() > -250) and (abs(ball.xcor() - basket.xcor()) < 50):
        ball.goto(random.randint(-290, 290), 250)
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Comic Sans MS", 20, "bold"))