import turtle as turt

def drawline(x1, y1, x2, y2):
    """
        Draws a line.
        :params: coordinates for the two ends of the line.
    """
    turt.up()
    turt.setpos(x1, y1)
    turt.down()
    turt.setpos(x2, y2)

def drawrec(x1, x2, y1, y2):
    """
        Draws a rectangle.
        x1: left x coord
        x2: right x coord
        y1: bottom y coord
        y2: top y coord
    """
    turt.up()
    turt.setpos(x1, y1)
    turt.down()
    turt.setpos(x1, y2)
    turt.setpos(x2, y2)
    turt.setpos(x2, y2)
    turt.setpos(x2, y1)
    turt.setpos(x1, y1)

def drawtri(x1, y1, x2, y2, x3):
    """
        Draws a triangle.
        x1: left x coord
        y1: bottom y coord
        x2: intermediate x coord
        y2: top y coord
        x3: right x coord
    """
    turt.up()
    turt.setpos(x1, y1)
    turt.down()
    turt.setpos(x2, y2)
    turt.setpos(x3, y1)
    turt.setpos(x1, y1)

def drawcircle(x, y, radius = 50, color = 'black', fill = True):
    """
        Draws a circle.
        x: x coord of center
        y: y coord of center
        radius: radius
        color: fill color
    """
    turt.setpos(x, y)
    turt.down()
    turt.color(color)
    if fill:
        turt.begin_fill()
    turt.circle(radius)
    if fill:
        turt.end_fill()
    turt.color('black')
    turt.up()

def drawwindow(x, y):
    drawrec(x, x+50, y, y+50)
    drawline(x+25, y, x+25, y+50)
    drawline(x, y+25, x+50, y + 25)

def drawgarage(x, y):
    drawrec(x, x+125, y, y+125)
    r = y
    while r + 10 < y+125:
        drawline(x + 5, r + 10, x + 120, r + 10)
        r += 10

def drawdoor(x, y):
    drawrec(x, x+50, y, y+100)
    turt.up()
    turt.setpos(x+40, y+40)
    turt.down()
    turt.circle(4)

def drawtree(x,y):
    # Draw the tree lines
    turt.up()
    turt.setpos(x, y)
    turt.down()
    turt.setpos(x, y+200)
    turt.up()
    turt.setpos(x+50, y+200)
    turt.down()
    turt.setpos(x + 50, y)

    # Draw the tree top
    turt.up()
    drawcircle(x - 25, y+200, color='green')
    drawcircle(x, y+200, color='green')
    drawcircle(x + 25, y+200, color='green')
    drawcircle(x + 50, y+200, color='green')
    drawcircle(x + 75, y+200, color='green')
    turt.down()

def drawcloud(x,y):
    # Draw the tree top
    turt.up()
    drawcircle(x - 50, y, color = 'grey')
    drawcircle(x, y, color = 'grey')
    drawcircle(x + 50, y, color = 'grey')
    drawcircle(x - 25, y + 35, color = 'grey')
    drawcircle(x + 25, y + 35, color = 'grey')
    turt.down()

def drawhouse(x, y):
    turt.Screen()
    drawrec(x, x+400, y, y+300)
    drawcloud(x - 150, y+400)
    drawcloud(x + 500, y+400)

    drawtree(x - 150, y)
    drawtree(x + 500, y)

    drawtri(x-50, y+300, x+200, y+400, x+450)
    drawwindow(x+50, y+200)
    drawwindow(x+125, y+200)
    drawwindow(x+225, y+200)
    drawwindow(x+300, y+200)
    drawgarage(x+25, y)
    drawgarage(x+250, y)
    drawdoor(x+175, y)
    turt.exitonclick()

drawhouse(-200, -200)

