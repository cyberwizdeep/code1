from turtle import *
speed(5)
width(5)

color('red', 'yellow')

begin_fill()
for i in range(7):  # Changed to 7
    right(180 - (180/7)) # Adjust this angle
    forward(200)
end_fill()

    
hideturtle()
bye()