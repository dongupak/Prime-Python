#Program to draw chessboard in Python Turtle
import turtle

chessboard = turtle.Turtle()
chessboard.speed(8) #for speedily drawing chessboard

chessboard_size = 400
chessboard_turn = 90
grid_size = chessboard_size / 8
chessboard.penup()
offset_x = -chessboard_size/2
offset_y = chessboard_size/2
chessboard.goto(offset_x, offset_y)
chessboard.pendown()
chessboard.hideturtle()

chessboard.width(4)
for i in range(4): #for loop will run 4 times
    chessboard.forward(chessboard_size) #forward turtle by 800 units
    chessboard.right(chessboard_turn) #turn turtle clockwise by 90 degree
a = 0 #for controlling alternate colors in a row
b = 0 #for controlling alternate colors in a column

chessboard.width(1)
for i in range(8): #for loop will run 8 times as there are 8 rows in the chessboard
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(8): #for loop will run 8 times as there are 8 columns in the chessboard
        chessboard.penup()
        chessboard.goto(j*grid_size+offset_x, i*grid_size*(-1)+offset_y)
        chessboard.pendown()
        if(a==0):
            chessboard.fillcolor('black')
            a=1
        else:
            chessboard.fillcolor('white')
            a=0
        chessboard.begin_fill()
        for k in range(4):
            chessboard.forward(grid_size)
            chessboard.right(chessboard_turn)
        chessboard.end_fill()
    if(b==0):
        b=1
    else:
        b=0
