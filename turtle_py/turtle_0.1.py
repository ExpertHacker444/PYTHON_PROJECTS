import turtle

# Configura la pantalla y el lápiz
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.color("pink")

# Ajusta el tamaño de la flor
t.pensize(30)

def petal():
    for _ in range(3):
        t.forward(150)
        t.right(120)
    t.right(30)

# Dibuja los pétalos de la rueda
for _ in range(100):
    petal()

# Dibuja el centro de l
t.color("pink")
t.goto(0, 0)
t.dot(100)

# Ajusta el tamaño del centro de la rueda
t.pensize(5)
t.dot(40)

# Finaliza el programa
turtle.done()