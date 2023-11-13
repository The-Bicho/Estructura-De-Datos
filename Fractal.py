import turtle

def piramide_fractal(t, longitud, nivel):
    if nivel == 2:
        t.begin_fill()
        for _ in range(3):
            t.forward(longitud)
            t.left(120)
        t.end_fill()
    else:
        piramide_fractal(t, longitud / 2, nivel - 1)
        t.forward(longitud / 2)
        piramide_fractal(t, longitud / 2, nivel - 1)
        t.backward(longitud / 2)
        t.left(60)
        t.forward(longitud / 2)
        t.right(60)
        piramide_fractal(t, longitud / 2, nivel - 1)
        t.left(60)
        t.backward(longitud / 2)
        t.right(60)

def main():
    window = turtle.Screen()
    window.bgcolor("violet")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-100, -100)
    t.pendown()

    nivel = 3  # Cambia el nivel del fractal aquí

    piramide_fractal(t, 400, nivel)

    window.exitonclick()

if __name__ == "__main__":
    main()