from turtle import *
color('red', 'orange')
begin_fill()
while True:
    forward(426)
    left(129)
    forward(200)
    left(129)
    if abs(pos()) < 1:
        break
end_fill()
color('blue', 'purple')
begin_fill()
while True:
    forward(250)
    left(80)
    forward(100)
    left(5)
    forward(250)
    left(80)
    forward(100)
    left(5)
    if abs(pos()) < 1:
        break
done()
