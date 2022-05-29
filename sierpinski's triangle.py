import turtle as t
import random
t.setworldcoordinates(-1, -1, t.window_width() - 1, t.window_height() - 1) #sets world coordinates to the bottom left corner
t.turtlesize(0.25)# changes size of turtle
#setting up the points location
p1x = 0
p1y = 0
p2x = 800
p2y = 0
p3x = 400
p3y = 700
#drawing the firts 3 points, going x, y
t.speed(100000000000)
t.shape("circle")
t.penup()
t.goto(p1x,p1y)
t.stamp()
t.goto(p2x,p2y)
t.stamp()
t.goto(p3x,p3y)
t.stamp()
rpx = 200 # making a "random" point so that the program can then start
rpy = 200
for i in range(1,10000): #runs many times
    x = random.randint(1,3)# choose a random point from the first 3 points.
    a = 0 # a and b are set so that it draws a new dot there
    b = 0
    if x == 1:
        #bunch on maths and hiculdy piculdy to calulate the middle between two dots
        if rpx > p1x: 
            a = (rpx + p1x) / 2
        else:
            a = (p1x + rpx) / 2 
        if rpy > p1y:
            b = (rpy + p1y) / 2
        else:
            b = (p1y + rpy) / 2
        t.goto(a, b) # goes to the middle location and makes a dot. 
        t.stamp()
        rpx = a # set the random point to now the last point so it continues the algorithm
        rpy = b
    if x == 2:
        #bunch on maths and hiculdy piculdy to calulate the middle between two dots
        if rpx > p2x:
            a = (rpx + p2x) / 2
        else:
            a = (p2x + rpx) / 2  
        if rpy > p2y:
            b = (rpy + p2y) / 2
        else:
            b = (p2y + rpy) / 2
        t.goto(a, b)# goes to the middle location and makes a dot. 
        t.stamp()
        rpx = a# set the random point to now the last point so it continues the algorithm
        rpy = b
    if x == 3:
        #bunch on maths and hiculdy piculdy to calulate the middle between two dots
        if rpx > p3x:
            a = (rpx + p3x) / 2
        else:
            a = (p3x + rpx) / 2
        if rpy > p3y:
            b = (rpy + p3y) / 2
        else:
            b = (p3y + rpy) / 2
        t.goto(a, b)# goes to the middle location and makes a dot. 
        t.stamp()
        rpx = a# set the random point to now the last point so it continues the algorithm
        rpy = b
