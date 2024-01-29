from turtle import *
from time import *

for n in range(1, 11):
    ht()
    speed(7)
    pencolor('purple')
    penup()
    sety(-250)
    setx((n-1)*25)
    pendown()
    number = 0
    for i in range(1, n + 1):
        number += i
    write(number, align='center', font=('Arial', 15, 'bold'))
    penup()
    sety(-200)
    setx(-200)
    pendown()
    for x in range(n, 0, -1):
        penup()
        sety(50 * (n - x) - 200)
        setx(25 * (n - x) - 200)
        pendown()
        for y in range(x, 0, -1):
            penup()
            setx(50 * (x - y) + 25 * (n - x))
            pendown()
            begin_fill()
            circle(10)
            end_fill()
    sleep(1)
    reset()
