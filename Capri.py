
# By Elizabeth Kuleshova

import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Capri")
turtle.bgcolor("light green")

HEAD_COLOR = 'purple'
HEAD_SHADOW = ''
EYE_COLOR = 'yellow'
EYE_SHADOW = ''
HORNS_COLOR = 'slategray'
HORNS_SHADOW = ''
JAW_COLOR = 'slategray'
JAW_SHADOW = ''
BODY_COLOR = 'purple'
BODY_SHADOW = ''
#LEG_COLOR = 'purple'
#LEG_SHADOW = ''
#TAIL_COLOR = 'purple'
#TAIL_SHADOW = ''

t.pensize(5)
t.speed(20)

def body():

    t.pencolor("purple")
    t.right(10)
    t.forward(80)

    t.pencolor("black")
    t.begin_fill()
    t.fillcolor(BODY_COLOR)
    t.left(70)
    t.circle(-50, 170)   #(radius, length)
    t.right(180)
    t.circle(38, -150)
    t.left(170)
    t.circle(-30, 100)
    t.right(175)
    t.end_fill()

    t.up()
    t.forward(54)
    t.left(55)

    
    t.down()
    t.circle(70, 160)
    t.left(175)
    t.circle(-70, -50)
    t.left(165)
    t.circle(70, 90)
    t.right(20)
    t.circle(70, 30)
    t.forward(130)
    t.left(10)
    t.circle(-70, 70)
    t.circle(70, 70)

def head():

    t.begin_fill()
    t.right(140)
    t.circle(10, 70)
    t.forward(10)
    t.right(240)
    t.forward(30)
    t.right(30)
    t.circle(-180, 20)
    t.right(30)
    t.forward(35)
    t.right(240)
    t.circle(40, 70)
    t.right(70)
    t.forward(10)
    t.circle(40, 50)
    t.circle(-28, 60)
    t.circle(20, 100)
    t.circle(10, 80)
    t.forward(30)
    t.right(40)
    t.circle(60, 70)
    t.right(55)
    t.circle(60, 30)
    t.end_fill()
    
    t.fillcolor(JAW_COLOR)
    t.right(190)
    t.up()
    t.forward(115)
    t.left(50)
    t.down()
    t.begin_fill()
    t.circle(-48, 40)
    t.left(150)
    t.circle(48, 70)
    t.end_fill()
    t.right(-120)
    t.forward(20)

    t.up()
    t.right(50)
    t.forward(24)
    t.left(50)

    t.down()
    t.circle(20, 20)

def eye():

    t.right(180)
    t.up()
    t.forward(42)

    t.fillcolor(EYE_COLOR)
    t.begin_fill()
    t.down()
    t.left(20)
    t.circle(-40, 60)
    t.right(100)
    t.circle(-40, 30)
    t.right(25)
    t.circle(-40, 35)
    t.end_fill()

def horns():

    t.begin_fill()
    t.fillcolor(HORNS_COLOR)
    t.right(93)
    t.up()
    t.forward(70)
    t.down()
    t.right(30)
    t.circle(-75, 58)
    t.right(-5)
    t.circle(-50, 30)
    t.forward(45)
    t.right(10)
    t.circle(70, 60)
    t.forward(10)
    t.left(200)
    t.circle(-150, 10)
    t.circle(-50, 70)
    t.right(-10)
    t.forward(50)
    t.right(-10)
    t.circle(60, 80)
    t.right(90)
    t.circle(-45, 30)
    t.end_fill()

    t.begin_fill()
    t.right(155)
    t.up()
    t.forward(40)
    t.down()
    t.right(-90)
    t.circle(-55, 50)
    t.right(25)
    t.forward(30)
    t.right(20)
    t.forward(30)
    t.right(-10)
    t.circle(80, 90)
    t.right(125)
    t.circle (-20, 70)
    t.right(-5)
    t.circle(-90, 90)
    t.forward(20)
    t.right(-22)
    t.circle(40, 63)
    t.right(70)
    t.forward(15)
    t.end_fill()

#def body2():

    #t.fillcolor(BODY_COLOR)
    #t.begin_fill()
    t.left(-258)
    t.up()
    t.forward(70)
    #t.end_fill()
   
body()
head()
eye()
horns()
#body2()

t.screen.exitonclick()