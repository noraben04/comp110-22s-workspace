from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()
leo.penup()
leo.goto(-160, -100)
leo.pendown()
colormode(255)
leo.color(143, 82, 41)
leo.begin_fill()
i:int = 0
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.speed(50)
bob.hideturtle()
bob.penup()
bob.goto(-140, -90)
bob.pendown()
colormode(255)
bob.color(56, 36, 22)
bob.begin_fill()

side_length: int = 300

i: int = 0
while(i<3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    #side_length = side_length * 0.97
bob.end_fill()

done()