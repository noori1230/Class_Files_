import turtle
import random
import os
import pyttsx3

# -------------------------
# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text using pyttsx3"""
    engine.say(text)
    engine.runAndWait()

# -------------------------
# Game Variables
delay = 100  # Game update delay in milliseconds
score = 0
high_score = 0
paused = False

# Load high score from file if exists
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as file:
        try:
            high_score = int(file.read())
        except ValueError:
            high_score = 0

# -------------------------
# Set up the screen
wn = turtle.Screen()
wn.title("🐍 Lex & Misi's Snake Game 🐍")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# -------------------------
# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# List for snake body segments
segments = []

# Create scoreboard pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def update_score():
    """Update the scoreboard text and save high score if needed"""
    global high_score
    if score > high_score:
        high_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(high_score))
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Comic Sans MS", 24, "bold"))

# -------------------------
# Movement functions
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
    if paused:
        speak("Game paused")
        pen.goto(0, 0)
        pen.write("Paused", align="center", font=("Comic Sans MS", 36, "bold"))
    else:
        pen.clear()
        update_score()
        speak("Game resumed")

# -------------------------
# Move the snake head one step in the current direction
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        hea
