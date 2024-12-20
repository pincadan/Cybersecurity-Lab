import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Cybersecurity Lab")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create a turtle for drawing
lab_turtle = turtle.Turtle()
lab_turtle.speed(0)
lab_turtle.penup()
lab_turtle.goto(-300, 0)
lab_turtle.color("white")

# Draw the lab components
def draw_lab_component(name, size):
    lab_turtle.write(name, align="center", font=("Arial", 16, "normal"))
    lab_turtle.forward(size)
    lab_turtle.left(90)
    lab_turtle.forward(size)
    lab_turtle.left(90)
    lab_turtle.forward(size)
    lab_turtle.left(90)
    lab_turtle.forward(size)
    lab_turtle.penup()
    lab_turtle.forward(100)

# Draw the lab components
lab_components = [
    ("Firewall", 100),
    ("VPN Server", 80),
    ("Web Server", 120),
    ("Database Server", 150),
    ("Workstation", 100)
]

for component in lab_components:
    draw_lab_component(component[0], component[1])

# Simulate interactions
def interact_with_component(x, y):
    if -300 <= x <= -100:
        print("Interacting with Firewall")
    elif -200 <= x <= -50:
        print("Interacting with VPN Server")
    elif -100 <= x <= 50:
        print("Interacting with Web Server")
    elif 0 <= x <= 150:
        print("Interacting with Database Server")
    elif 100 <= x <= 250:
        print("Interacting with Workstation")

# Bind mouse click events
screen.onclick(interact_with_component)

# Start the turtle graphics loop
turtle.done()