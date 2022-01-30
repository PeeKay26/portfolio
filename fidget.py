import turtle
import random

win= turtle.Screen()
win.title("Fidget Spinner")
win.bgcolor("white")

col = ["red","blue","green"]

t1 = turtle.Turtle()
t1.pencolor("black")
t1.penup()
t1.goto(0,200)
t1.write("Fidget Spinner", align="center",font=("Comic Sans MS", 24, "bold"))
t1.hideturtle()

t = turtle.Turtle()
t.pensize(random.randint(10,50))

state = {'turn':0}

def spinner():
    t.clear()
    angle = state['turn']/10
    t.right(angle)
    for i in range(3):
        t.forward(100)
        t.dot(100, col[i])
        t.backward(100)
        t.left(120)
    turtle.update()

def animate():
    if state["turn"]>0:
        state['turn'] -=1
    spinner()
    turtle.ontimer(animate, 50)

def flick():
    state["turn"]+=10

win.tracer(False)
turtle.onkey(flick,"space")
turtle.listen()
animate()


turtle.done()