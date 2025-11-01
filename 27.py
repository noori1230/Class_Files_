import turtle
import time
import random
import os

# ----------------------------
# 🐍 Game Settings
# ----------------------------
delay = 100  # milliseconds (10 fps)
score = 0
high_score = 0
paused = False

# ----------------------------
# 💾 Load High Score
# ----------------------------
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        try:
            high_score = int(f.read())
        except:
            high_score = 0

# ----------------------------
# 🖥️ Set up screen
# ----------------------------
wn = turtle.Screen()
wn.title("🐍 Lex & Misi's Snake Game 🐍")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0)

# 🐍 Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 🍎 Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# 🏆 Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Comic Sans MS", 24, "bold"))

# ----------------------------
# 📋 Score Update
# ----------------------------
def update_score():
    global high_score
    if score > high_score:
        high_score = score
        with open("highscore.txt", "w") as f:
            f.write(str(high_score))
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Comic Sans MS", 24, "bold"))

# ----------------------------
# 🕹️ Controls
# ----------------------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def toggle_pause():
    global paused
    paused = not paused

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(toggle_pause, "p")

# ----------------------------
# 🚀 Movement
# ----------------------------
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# ----------------------------
# 🎮 Game Reset
# ----------------------------
def reset_game():
    global score, delay, segments
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    update_score()

# ----------------------------
# 🔁 Game Loop Function
# ----------------------------
def game_loop():
    global score, delay

    if not paused:
        wn.update()

        # 🧱 Border collision
        if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):
            reset_game()

        # 🍎 Food collision
        if head.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            # Add new segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)

            score += 10
            update_score()

        # Move segments
        for i in range(len(segments)-1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)
        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # 💥 Self-collision
        for segment in segments:
            if segment.distance(head) < 20:
                reset_game()

    # Run again after `delay` ms
    wn.ontimer(game_loop, delay)

# ----------------------------
# 🎮 Start Game
# ----------------------------
update_score()
game_loop()
wn.mainloop()
