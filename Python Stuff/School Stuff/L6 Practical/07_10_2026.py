import turtle as t

screen = t.Screen()

screen.onkey(lambda: t.forward(10), "Up")
screen.onkey(lambda: t.backward(10), "Down")
screen.onkey(lambda: t.left(10), "Left")
screen.onkey(lambda: t.right(10), "Right")

screen.listen()
screen.mainloop()