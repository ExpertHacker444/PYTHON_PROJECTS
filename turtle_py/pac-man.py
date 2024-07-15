import turtle

def draw_circle(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_dot(t, size, color):
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# Configura la pantalla y el lápiz
screen = turtle.Screen()
screen.bgcolor("#3DDC84")

t = turtle.Turtle()
t.speed(0)

# Cuerpo del Android
draw_circle(t, 150, "black")

# Cabeza del Android
t.penup()
t.goto(0, 100)
t.pendown()
draw_circle(t, 100, "lightgreen")

# Ojos del Android
t.penup()
t.goto(-40, 140)
t.pendown()
draw_dot(t, 20, "black")

t.penup()
t.goto(40, 140)
t.pendown()
draw_dot(t, 20, "black")

t.penup()
t.goto(0, -50)
t.color("black")
t.write("ANDI OS", align="center", font=("Arial", 24, "normal"))



# Finaliza el programa
turtle.done()