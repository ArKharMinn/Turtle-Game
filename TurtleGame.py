import turtle as t
import random as r

screen=t.Screen()
screen.bgcolor("gold")

avator=t.Turtle()
avator.shape("turtle")
avator.color('white')
avator.penup()

en=t.Turtle()
en.shape("turtle")
en.color('black')
en.penup()

score=0
myscore=t.Turtle()
myscore.hideturtle()
myscore.goto(0,290)
myscore.write(f"Score : {score}",font=(25),align=("center"))

def run():
    x=r.randint(-290,290)
    y=r.randint(-290,290)
    en.goto(x,y)

def check():
    global score
    if avator.distance(en)<20:
        score += 1
        myscore.clear()
        myscore.write(f"Score : {score}",font=(25),align="center")
        run()

def up():
    avator.sety(avator.ycor() +10)
    check()

def down():
    avator.sety(avator.ycor()-10)
    check()

def right():
    avator.setx(avator.xcor()+10)
    check()

def left():
    avator.setx(avator.xcor()-10)
    check()


screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(right,"Right")
screen.onkey(left,"Left")

screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")

screen.mainloop()