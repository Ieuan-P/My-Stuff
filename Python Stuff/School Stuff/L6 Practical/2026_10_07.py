import turtle as t

screen = t.Screen()

screen.onkeypress(lambda: t.forward(10), "Up")
screen.onkeypress(lambda: t.backward(10), "Down")
screen.onkeypress(lambda: t.left(10), "Left")
screen.onkeypress(lambda: t.right(10), "Right")
screen.onkeypress(lambda: t.pensize(100), "1")
screen.onkeypress(lambda: t.pensize(10), "2")

screen.listen()
screen.mainloop()