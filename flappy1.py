import turtle
import time

win=turtle.Screen()
win.title("Flappy Birds")
win.bgcolor("blue")
win.setup(width=800, height=700)
win.tracer(False)
win.bgpic('fbim.gif')

pen=turtle.Turtle()
pen.speed(0)
pen.ht()
pen.color("white")
pen.pu()
pen.goto(-200, 300)
pen.write("Score: 0", font=("verdana",24,"bold"))

player=turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.shapesize(stretch_wid=3, stretch_len=3)
player.goto(-200,0)
player.dx = 0
player.dy = 1
gravity = -0.1

pipe1_top=turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color('green')
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3)
pipe1_top.goto(300, 300)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bottom=turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color('green')
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3)
pipe1_bottom.goto(300, -300)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0

pipe2_top=turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color('green')
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3)
pipe2_top.goto(600, 300)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1

pipe2_bottom=turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color('green')
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3)
pipe2_bottom.goto(600, -300)
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0


def go_up():
    player.dy += 5
    if player.dy>5:
        player.dy=5

win.listen()
win.onkeypress(go_up,"space")


player.score = 0
print("Score: {}".format(player.score))


while True:
    time.sleep(0.02)
    win.update()
    player.dy += gravity

    y = player.ycor()
    y += player.dy
    player.sety(y)

    if player.ycor()< -320:
        player.dy = 0
        player.sety(-320)
    
    x=pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x)

    x=pipe1_bottom.xcor()
    x += pipe1_bottom.dx
    pipe1_bottom.setx(x)

    if pipe1_top.xcor() < -350:
        pipe1_top.setx(350)
        pipe1_bottom.setx(350)
        pipe1_top.value = 1

    x=pipe2_top.xcor()
    x += pipe2_top.dx
    pipe2_top.setx(x)

    x=pipe2_bottom.xcor()
    x += pipe2_bottom.dx
    pipe2_bottom.setx(x)

    if pipe2_top.xcor() < -350:
        pipe2_top.setx(350)
        pipe2_bottom.setx(350)
        pipe2_top.value = 1


    if (player.xcor() + 30 > pipe1_top.xcor() -30 ) and (player.xcor() - 30 < pipe1_top.xcor()+30 ):
        if (player.ycor()+30 > pipe1_top.ycor()-180) or (player.ycor()-30 < pipe1_bottom.ycor()+180):
            print('Game over')    
            win.update()
            time.sleep(5)
            
            pen.clear()
            player.score = 0
            pen.write(f"Score: {player.score}", font=("verdana",24,"bold"))
            
            pipe1_top.setx(300)
            pipe1_bottom.setx(300)
            pipe1_top.setx(600)
            pipe1_bottom.setx(600)
            
            player.goto(-200,0)
            player.dy = 0
    
    
    if pipe1_top.xcor() + 30 < player.xcor() -30:
        player.score += pipe1_top.value
        pipe1_top.value = 0
        print("Score: {}".format(player.score))
        pen.clear()
        pen.write(f"Score: {player.score}", font=("verdana",24,"bold"))


    if (player.xcor() + 30 > pipe2_top.xcor() - 30 ) and (player.xcor() - 30 < pipe2_top.xcor() + 30 ):
        if (player.ycor()+30 > pipe2_top.ycor() - 180) or (player.ycor() - 30 < pipe2_bottom.ycor() + 180):
            print('Game over')
            win.update()
            time.sleep(5)
           
            pen.clear()
            player.score = 0
            pen.write(f"Score: {player.score}", font=("verdana",24,"bold"))
            
            
            pipe2_top.setx(300)
            pipe2_bottom.setx(300)
            pipe2_top.setx(600)
            pipe2_bottom.setx(600)
            
            player.goto(-200,0)
            player.dy = 0   


    if pipe2_top.xcor() + 30 < player.xcor() -30:
        player.score += pipe2_top.value
        pipe2_top.value = 0
        print("Score: {}".format(player.score))
        pen.clear()
        pen.write(f"Score: {player.score}", font=("verdana",24,"bold"))

