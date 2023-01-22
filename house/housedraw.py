import turtle as turt

def drawline(x1,y1, x2, y2):
    turt.up()
    turt.setpos(x1, y1)
    turt.down()
    turt.setpos(x2, y2)

def drawrec(x1,x2, y1, y2):
    turt.up()
    turt.setpos(x1,y1)
    turt.down()
    turt.setpos(x1, y2)
    turt.setpos(x2, y2)
    turt.setpos(x2, y2)
    turt.setpos(x2, y1)
    turt.setpos(x1, y1)

def drawtri(x1, y1, x2, y2, x3):
    turt.up()
    turt.setpos(x1, y1)
    turt.down()
    turt.setpos(x2, y2)
    turt.setpos(x3, y1)
    turt.setpos(x1, y1)

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
    turt.up()
    turt.setpos(x, y)
    turt.down()
    turt.setpos(x, y+200)
    turt.up()
    turt.setpos(x+50, y+200)
    turt.down()
    turt.setpos(x + 50, y)

def drawhouse(x, y):
    turt.Screen()
    drawrec(x, x+400, y, y+300)
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

