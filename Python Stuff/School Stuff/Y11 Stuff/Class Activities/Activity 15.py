#Activity 15

import turtle as t

t.speed(0)

keys = {"W": False, "A": False, "S": False, "D": False, "Q": False}

def key_press(key):
    keys[key] = True

def key_release(key):
    keys[key] = False

def keystuff():
    if keys["W"]:
        t.forward(10)
    if keys["S"]:
        t.backward(10)
    if keys["A"]:
        t.left(10)
    if keys["D"]:
        t.right(10)
    if keys["Q"]:
        t.bye()
    t.ontimer(keystuff, 50)

screen = t.Screen()
screen.listen()

screen.onkeypress(lambda: key_press("W"), "w")
screen.onkeypress(lambda: key_press("A"), "a")
screen.onkeypress(lambda: key_press("S"), "s")
screen.onkeypress(lambda: key_press("D"), "d")
screen.onkeypress(lambda: key_press("Q"), "q")

screen.onkeyrelease(lambda: key_release("W"), "w")
screen.onkeyrelease(lambda: key_release("A"), "a")
screen.onkeyrelease(lambda: key_release("S"), "s")
screen.onkeyrelease(lambda: key_release("D"), "d")
screen.onkeyrelease(lambda: key_release("Q"), "q")


keystuff()
t.done()