import turtle
t= turtle.Turtle()
t.shape("turtle")

size=int(input("집의 크기는 얼마로 할까요? "))

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

t.right(90)

t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)

t.right(120)
t.forward(30)

t.up()
t.goto(60,0)
t.down()

t.left(120)

