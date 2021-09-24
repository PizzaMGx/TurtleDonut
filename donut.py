import turtle

turtle.speed(0.1)
for i in range(12):
    for colours in ["red", "yellow", "green", "blue", "purple", "black"]:
        turtle.color(colours)
        # moves in direction, can be also foward and backwards
        turtle.circle(150)
        turtle.left(5)  # turn certain amount of degrees
        turtle.backward(10)
turtle.done()
