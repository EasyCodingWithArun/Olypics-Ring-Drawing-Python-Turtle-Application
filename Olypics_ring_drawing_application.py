import turtle

# --- Screen Setup ---
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Olympic Rings")

# --- Turtle Setup ---
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(2)

# --- Ring Positions and Colors ---
rings = [
    {"color": "blue",   "x": -110, "y": 0},
    {"color": "black",  "x": 0,    "y": 0},
    {"color": "red",    "x": 110,  "y": 0},
    {"color": "yellow", "x": -55,  "y": -50},
    {"color": "green",  "x": 55,   "y": -50}
]

# --- Draw the Rings ---
def draw_ring(color, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pencolor(color)
    pen.circle(50)

# --- Loop through and draw all rings ---
for ring in rings:
    draw_ring(ring["color"], ring["x"], ring["y"])

# --- Finish ---
pen.hideturtle()
screen.mainloop()
