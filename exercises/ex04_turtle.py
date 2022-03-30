"""Smooth spongebob."""

__author__ = "730437270"

from turtle import Turtle, colormode, done


def sponge(sponge: Turtle, x: float, y: float, fill: str) -> None:
    """Spongebob's head."""
    sponge.speed(50)
    sponge.hideturtle()
    sponge.penup()
    sponge.goto(x, y)
    sponge.pendown()
    colormode(255)
    sponge.color(fill)
    sponge.begin_fill()
    i: int = 0
    while (i < 4):
        sponge.forward(400)
        sponge.left(90)
        i = i + 1
    sponge.end_fill()


def eye_one(eye_one: Turtle, x: float, y: float, radius: float, fill: str) -> None:
    """Spongebob's left eye."""
    eye_one.speed(50)
    eye_one.hideturtle()
    eye_one.penup()
    eye_one.goto(x, y)
    eye_one.pendown()
    colormode(255)
    eye_one.color(fill)
    eye_one.begin_fill()
    eye_one.circle(radius)
    eye_one.end_fill()


def smile(smile: Turtle, x: float, y: float, radius: float, fill: str) -> None:
    """Spongebob's smile :)."""
    smile.speed(50)
    smile.hideturtle()
    smile.penup()
    smile.goto(x, y)
    smile.pendown()
    colormode(255)
    smile.color(fill)
    smile.begin_fill()
    smile.left(270)
    smile.circle(radius, 180)
    smile.end_fill()


def teeth(teeth: Turtle, x: float, y: float, fill: str) -> None:
    """Spongebob's buck teeth."""
    teeth.speed(50)
    teeth.hideturtle()
    teeth.penup()
    teeth.goto(x, y)
    teeth.pendown()
    colormode(255)
    teeth.color(fill)
    teeth.begin_fill()
    i: int = 0
    while (i < 4):
        teeth.forward(40)
        teeth.left(90)
        i = i + 1
    teeth.end_fill()


def legs(legs: Turtle, x: float, y: float, fill: str) -> None:
    """Spongebob's legs."""
    legs.speed(50)
    legs.hideturtle()
    legs.pensize(30)
    legs.penup()
    legs.goto(x, y)
    legs.pendown()
    colormode(255)
    legs.color(fill)
    legs.begin_fill()
    legs.goto(x, y - 180)
    legs.end_fill()


def feet(feet: Turtle, x: float, y: float, radius: float, fill: str) -> None:
    """Spongebob's feet."""
    feet.speed(50)
    feet.hideturtle()
    feet.penup()
    feet.goto(x, y)
    feet.pendown()
    colormode(255)
    feet.color(fill)
    feet.begin_fill()
    feet.circle(radius)
    feet.end_fill()


def pants(pants: Turtle, x: float, y: float, fill: str) -> None:
    """Spongebob's pants."""
    pants.speed(50)
    pants.hideturtle()
    pants.penup()
    pants.goto(x, y)
    pants.pendown()
    colormode(255)
    pants.color(fill)
    pants.pensize(1)
    pants.begin_fill()
    pants.forward(60)
    pants.left(90)
    pants.forward(400)
    pants.left(90)
    pants.forward(60)
    pants.left(90)
    pants.forward(400)
    pants.end_fill()


def tie(tie: Turtle, x: float, y: float, fill: str) -> None:
    """Spongebobs tie."""
    tie.speed(50)
    tie.hideturtle()
    tie.pensize(20)
    tie.penup()
    tie.goto(x, y)
    tie.pendown()
    colormode(255)
    tie.color(fill)
    tie.begin_fill()
    tie.goto(x, y - 30)
    tie.end_fill()


def main() -> None:
    """Caling all parts of the function."""
    turtle: Turtle = Turtle()
    sponge(turtle, -200, -100, "yellow")
    eye_one(turtle, -100, 100, 60, "white")
    eye_one(turtle, 100, 100, 60, "white")
    eye_one(turtle, -100, 100, 30, "black")
    eye_one(turtle, 100, 100, 30, "black")
    smile(turtle, -100, 60, 100, "black")
    teeth(turtle, -10, 20, "white")
    teeth(turtle, 60, 20, "white")
    legs(turtle, -100, -100, "yellow")
    legs(turtle, 100, -100, "yellow")
    feet(turtle, -100, -280, 10, "brown")
    feet(turtle, 100, -280, 10, "brown")
    pants(turtle, 200, -120, "brown")
    tie(turtle, 10, -70, "red")
    done()


if __name__ == "__main__":
    main()
    