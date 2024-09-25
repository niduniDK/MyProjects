from turtle import *
from random import *
from time import *


# Function for rolling the dice.
def roll_dice():
    speed(0)
    ht()
    penup()
    setpos(-100, 100)
    pendown()
    forward(200)
    left(-90)
    forward(200)
    left(-90)
    forward(200)
    left(-90)
    forward(200)
    left(-90)
    # Number to be returned from the dice
    number = randint(1, 6)
    if number == 1:
        penup()
        setpos(0, 0)
        pendown()
        dot(20)
    elif number == 2:
        penup()
        setpos(-80, 80)
        pendown()
        dot(20)
        penup()
        setpos(80, -80)
        pendown()
        dot(20)
    elif number == 3:
        penup()
        setpos(-80, 80)
        pendown()
        dot(20)
        penup()
        setpos(0, 0)
        pendown()
        dot(20)
        penup()
        setpos(80, -80)
        pendown()
        dot(20)
    elif number == 4:
        penup()
        setpos(-80, 80)
        pendown()
        dot(20)
        penup()
        setpos(-80, -80)
        pendown()
        dot(20)
        penup()
        setpos(80, -80)
        pendown()
        dot(20)
        penup()
        setpos(80, 80)
        pendown()
        dot(20)
    elif number == 5:
        penup()
        setpos(-80, 80)
        pendown()
        dot(20)
        penup()
        setpos(-80, -80)
        pendown()
        dot(20)
        penup()
        setpos(0, 0)
        pendown()
        dot(20)
        penup()
        setpos(80, -80)
        pendown()
        dot(20)
        penup()
        setpos(80, 80)
        pendown()
        dot(20)
    else:
        penup()
        setpos(-80, 80)
        pendown()
        dot(20)
        penup()
        setpos(0, 80)
        pendown()
        dot(20)
        penup()
        setpos(-80, -80)
        pendown()
        dot(20)
        penup()
        setpos(80, -80)
        pendown()
        dot(20)
        penup()
        setpos(0, -80)
        pendown()
        dot(20)
        penup()
        setpos(80, 80)
        pendown()
        dot(20)
    sleep(5)
    return number


# Function for creating a snake on the board.
def create_snake(x, y, color_name):
    penup()
    setpos(x, y)
    pendown()
    pensize(10)
    pencolor(color_name)
    forward(50)
    left(90)
    forward(100)
    left(-90)
    forward(50)
    begin_fill()
    circle(5)
    end_fill()


# Function for creating ladder on the board.
# x and y coordinates of the beginning of the ladder must be entered as parameters.
def create_ladder(x_beg, y_beg):
    speed(0)
    penup()
    setpos(x_beg, y_beg)
    pendown()
    # Setting the end of the ladder.
    x_end = x_beg + 50
    y_end = y_beg + 150
    pencolor('black')
    pensize(10)
    setpos(x_end, y_end)
    penup()
    setpos(x_beg+50, y_beg)
    pendown()
    pensize(10)
    setpos(x_end+50, y_end)
    for i2 in range(10, 50, 10):
        penup()
        setpos(x_beg+i2, y_beg+i2*3)
        pendown()
        pensize(5)
        setpos(x_beg+i2+50, y_beg+i2*3)


# Function for creating the board.
def create_board():
    speed(0)
    penup()
    setpos(-250, 250)
    pendown()
    fillcolor('yellow')
    begin_fill()
    forward(500)
    left(-90)
    forward(500)
    left(-90)
    forward(500)
    left(-90)
    forward(500)
    left(-90)
    end_fill()
    # Separating the board into boxes.
    for i1 in range(200, -250, -50):
        penup()
        setpos(-250, i1)
        pendown()
        forward(500)
        penup()
        setpos(i1, 250)
        pendown()
        left(-90)
        forward(500)
        left(90)
    a = 1
    y = -210
    # Labeling each box
    for j1 in range(10):
        for x in range(-240, 260, 50):
            penup()
            setpos(x, y)
            pendown()
            write(a)
            a += 1
        y += 50

# creating snake1.
    create_snake(-80, -230, 'red')
# creating snake2.
    create_snake(-30, 120, 'green')
# creating snake3.
    create_snake(120, -80, 'purple')
# creating ladder1.
    create_ladder(-200, -30)
# creating ladder2.
    create_ladder(100, 70)
    penup()


def play(c_name: str):
    t = 0
    x = 0
    y = 0
    penup()
    setpos(-230, -230)
    pendown()
    while x < 100:
        r = roll_dice()
        x += r
        t += r
        reset()
        create_board()
        if t < 100:
            if x > 10:
                x -= 10
                y += 1
                penup()
                setpos(-230+(x-1)*50, -230+y*50)
                pendown()
                if t == 26:
                    penup()
                    setpos(-80, -230)
                    pendown()
                    t = 4
                    x = 4
                    y = 0
                elif t == 60:
                    penup()
                    setpos(120, -80)
                    pendown()
                    t = 38
                    x = 8
                    y = 3
                elif t == 97:
                    penup()
                    setpos(-30, 120)
                    pendown()
                    t = 75
                    x = 5
                    y = 7
                elif t == 42:
                    penup()
                    setpos(-180, -30)
                    pendown()
                    t = 73
                    x = 3
                    y = 7
                elif t == 68:
                    penup()
                    setpos(170, 220)
                    pendown()
                    t = 99
                    x = 9
                    y = 9
                pencolor(c_name)
                pensize(5)
                stamp()
                sleep(5)
            else:
                penup()
                setpos(-230 + (x - 1) * 50, -230+y*50)
                pendown()
                if t == 26:
                    penup()
                    setpos(-80, -230)
                    pendown()
                    t = 4
                    x = 4
                    y = 0
                elif t == 60:
                    penup()
                    setpos(120, -80)
                    pendown()
                    t = 38
                    x = 8
                    y = 3
                elif t == 97:
                    penup()
                    setpos(-30, 120)
                    pendown()
                    t = 75
                    x = 5
                    y = 7
                elif t == 42:
                    penup()
                    setpos(-180, -30)
                    pendown()
                    t = 73
                    x = 3
                    y = 7
                elif t == 68:
                    penup()
                    setpos(170, 220)
                    pendown()
                    t = 99
                    x = 9
                    y = 9
                pencolor('black')
                pensize(5)
                stamp()
                sleep(5)
        elif t == 100:
            reset()
            write('Finally you won the cup!!!!', align='center', font=('Arial', 50, 'bold'))
            sleep(5)
            break
        else:
            reset()
            t -= r
        reset()


name = input('Please enter your name: ')
print('Hey', name, '!!!\n\
Please enter y or n below\n\
y -> yes\n\
n -> no')
res = input('Shall we play a game: ')
if res == 'y':
    print("Yep!!Let's Get Started!!!!")
    play('black')
else:
    print('Ok!May be next time!!!')
