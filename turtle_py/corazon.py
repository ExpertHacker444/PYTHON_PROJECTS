import turtle

# Configura la pantalla y el lápiz
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.color("pink")
t.begin_fill()

# Dibuja el corazón
t.left(50)
t.forward(140)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(140)
t.end_fill()

# Dibuja la palabra "Love"
t.penup()
t.goto(0, -50)
t.color("white")
t.write("Love", align="center", font=("Arial", 24, "normal"))

# Finaliza el programa
turtle.done()