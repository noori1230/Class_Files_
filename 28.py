# amazing_flower.py
# A colorful animated flower using Python's turtle
# Made friendly for kids — try changing colors and sizes!


        angle_offset = step * 3
        for i in range(positions):
            ang = math.radians(i * (360 / positions) + angle_offset)
            x = math.cos(ang) * radius
            y = math.sin(ang) * radius
            ring.goto(x, y)import turtle
import math
import random

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#0b1020")   # dark background so colors pop
screen.title("Amazing Flower 🌸 - by Lex")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)
t.penup()

# Nice palette — change these if you like!
layer_colors = ["#FF5C8A", "#FF9F68", "#FFD166", "#9EE493", "#7ADFF0"]
center_colors = ["#FFF5A5", "#FFF1C2", "#FFE887"]

# Helper to draw a petal as an ellipse-like shape
def draw_petal(turtle_obj, radius, angle):
    turtle_obj.pendown()
    # draw one side of petal
    turtle_obj.circle(radius, angle)
    # curve back to start making a mirrored arc
    turtle_obj.left(180 - angle)
    turtle_obj.circle(radius, angle)
    turtle_obj.left(180 - angle)
    turtle_obj.penup()

# Draw a layer of petals rotated evenly around center
def draw_layer(turtle_obj, petal_count, radius, angle, color, scale=1.0):
    turtle_obj.color(color)
    step = 360 / petal_count
    for i in range(petal_count):
        turtle_obj.setheading(i * step)
        turtle_obj.forward(20 * scale)
        draw_petal(turtle_obj, radius * scale, angle)
        turtle_obj.backward(20 * scale)

# Draw multiple layered petals
def draw_flower():
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.width(2)

    # outer to inner layers (big to small)
    layers = [
        (20, 120, 60, layer_colors[0], 1.6),
        (16, 90, 65, layer_colors[1], 1.25),
        (12, 70, 70, layer_colors[2], 0.95),
        (10, 50, 75, layer_colors[3], 0.7),
        (8, 40, 80, layer_colors[4], 0.45),
    ]

    for petals, radius, angle, color, scale in layers:
        draw_layer(t, petals, radius, angle, color, scale)

# Draw center with many little circles that twinkle
def draw_center():
    center = turtle.Turtle()
    center.hideturtle()
    center.speed(0)
    center.penup()
    center.goto(0, -10)
    for r in range(50, 0, -8):
        c = random.choice(center_colors)
        center.color(c)
        center.begin_fill()
        center.circle(r)
        center.end_fill()
        center.goto(0, -r - 10)

# Optional: add rotating little dots around the center
def animate_ring():
    ring = turtle.Turtle()
    ring.hideturtle()
    ring.speed(0)
    ring.penup()
    ring.width(3)
    positions = 16
    radius = 120
    for step in range(120):  # frames
        ring.clear()
            ring.dot(8 + (i % 3))  # vary size a bit
        screen.update()

# Main draw
screen.tracer(False)   # draw instantly for nicer result
draw_flower()
draw_center()
screen.tracer(True)

# animate the ring (uncomment to see animation; it'll run then stop)
try:
    animate_ring()
except turtle.Terminator:
    pass

# Finish: make the window close on click
turtle.done()
