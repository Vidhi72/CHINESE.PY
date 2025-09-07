import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
screen = turtle.Screen()
screen.bgcolor("Red")
turtle.title("Teacher Teaching Student Chinese")

def circle(x, y, r, color):
    """Draw filled circle"""
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# --- Blackboard ---
t.penup()
t.goto(-200, 150)
t.pendown()
t.pensize(4)
t.fillcolor("black")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# Write Chinese on board
t.penup()
t.goto(-120, 70)
t.pencolor("white")
t.write("你好", font=("Arial", 48, "bold"))  # Means "Hello" in Chinese

# --- Teacher ---
circle(-100, -50, 40, "#f7cba4")   # head
circle(-115, -40, 5, "black")      # left eye
circle(-85, -40, 5, "black")       # right eye

t.pensize(15)
t.pencolor("blue")
t.penup()
t.goto(-100, -90)
t.pendown()
t.goto(-100, -160)  # body

# teacher hand pointing to board
t.goto(-40, -100)

# --- Student ---
circle(120, -50, 35, "#f7cba4")    # head
circle(110, -45, 5, "black")       # left eye
circle(130, -45, 5, "black")       # right eye

t.pensize(15)
t.pencolor("green")
t.penup()
t.goto(120, -80)
t.pendown()
t.goto(120, -140)  # body

# Student holding book
t.pensize(3)
t.pencolor("brown")
t.penup()
t.goto(90, -100)
t.pendown()
t.fillcolor("lightyellow")
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

# --- Title ---
t.penup()
t.goto(-150, -220)
t.pencolor("darkred")
t.write("Teacher teaching Student Chinese", font=("Arial", 18, "bold"))

t.hideturtle()
turtle.done()
