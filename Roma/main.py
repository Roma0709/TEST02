from turtle import*
from random import*
t1 = Turtle()
t2=Turtle()

t1.penup()
t2.penup()


t1.goto(-50,100)
t2.goto(-50,70)


while t1.xcor()<300 and t2.xcor()<300:
    t1.forward(randint(5,10))
    t2.forward(randint(5,10))


if t1.xcor ()>300:
    t1.write("t1 won")
else:
    t2.write("t2 won")   

exitonclick()