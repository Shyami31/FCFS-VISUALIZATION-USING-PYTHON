import turtle

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CUSTOMER_WIDTH = 50
CUSTOMER_HEIGHT = 30
SPACING = 10
CUSTOMER_COLORS = ["blue", "blue", "blue", "blue", "blue"]

# Setup
wn = turtle.Screen()
wn.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
wn.title("FCFS Simulator")
t = turtle.Turtle()
t.hideturtle()

# Create list of customers
customers = []
for i in range(5):
    x = -((CUSTOMER_WIDTH + SPACING) * 2) + i * (CUSTOMER_WIDTH + SPACING)
    y = 0
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(CUSTOMER_COLORS[i])
    t.begin_fill()
    for j in range(2):
        t.fd(CUSTOMER_WIDTH)
        t.lt(90)
        t.fd(CUSTOMER_HEIGHT)
        t.lt(90)
    t.end_fill()
    customers.append(t.pos())

# Serve customers in FCFS order
for i in range(5):
    # Move customer to front of line
    customer_pos = customers.pop(0)
    customers.append(customer_pos)
    
    # Change color to gray to indicate served customer
    t.penup()
    t.goto(customer_pos[0] + CUSTOMER_WIDTH / 2, customer_pos[1] + CUSTOMER_HEIGHT / 2)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(CUSTOMER_HEIGHT / 2)
    t.end_fill()

# Add explanation
t.penup()
t.goto(0, -WINDOW_HEIGHT / 2 + 20)
t.pendown()
t.write("This is an FCFS algorithm simulation.\nThe customers are represented as blue rectangles\nThe customers arrive in left-right order and are served in the same order in which they arrived.\nA customer is marked with a red circle to indicate that they are served.", align="center", font=("Arial", 12, "normal"))

# Keep window open until user closes it
turtle.mainloop()
