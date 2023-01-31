#!/usr/bin/env python3

import turtle


def draw_line(x1, y1, x2, y2):
    """
        Draws a line.
        :params: coordinates for the two ends of the line.
    """
    turtle.up()
    turtle.setpos(x1, y1)
    turtle.down()
    turtle.setpos(x2, y2)


def draw_rec(x1, y1, x2, y2, color='black', fill=True):
    """
        Draws a rectangle
        composed of vertical
        and horizontal lines.
        x1: left x coord
        x2: right x coord
        y1: bottom y coord
        y2: top y coord
    """
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    draw_line(x1, y1, x1, y2)
    draw_line(x1, y2, x2, y2)
    draw_line(x2, y2, x2, y1)
    draw_line(x2, y1, x1, y1)
    if fill:
        turtle.end_fill()


def draw_tri(x1, y1, x2, y2, x3, color='black', fill=True):
    """
        Draws a triangle.
        x1: left x coord
        y1: bottom y coord
        x2: intermediate x coord
        y2: top y coord
        x3: right x coord
    """
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    draw_line(x1, y1, x2, y2)
    draw_line(x2, y2, x3, y1)
    draw_line(x3, y1, x1, y1)
    if fill:
        turtle.end_fill()


def draw_circle(x, y, radius=50, color='black', fill=True):
    """
        Draws a circle.
        x: x coord of center
        y: y coord of center
        radius: radius
        color: fill color
    """
    turtle.up()
    turtle.setpos(x, y)
    turtle.color(color)
    turtle.down()
    if fill:
        turtle.begin_fill()
    turtle.circle(radius)
    if fill:
        turtle.end_fill()


def draw_window(x, y, color='blue', fill=True):
    """
        Draws a window.
        :params: coordinates for bottom left corner of window.
    """
    draw_rec(x, y, x + 0.5*d, y + 0.5*d, color, fill)
    turtle.color('black')
    draw_line(x + 0.25*d, y, x + 0.25*d, y + 0.5*d)
    draw_line(x, y + 0.25*d, x + 0.5*d, y + 0.25*d)


def draw_garage(x, y, color='gray', fill=True):
    """
    Draws a garage.
    :params: coordinates for bottom left corner of garage.
    """
    draw_rec(x, y, x + 1.25*d, y + 1.25*d, color, fill)
    r = y
    turtle.color('black')
    while r + 0.1*d < y + 1.25*d:
        draw_line(x + 0.05*d, r + 0.1*d, x + 1.2*d, r + 0.1*d)
        r += 0.1*d


def draw_door(x, y, color='black', fill=True):
    """
        Draws a door.
        :params: coordinates for bottom left corner of door.
    """
    draw_rec(x, y, x + 0.5*d, y + d, color, fill)
    draw_circle(x + 0.4*d, y + 0.4*d, int(0.04*d), color='yellow', fill=True)


def draw_tree(x, y):
    """
        Draws a tree.
        :params: coordinates for bottom left corner of tree.
    """

    # Draw the tree trunk
    draw_rec(x, y, x + 0.5*d, y + 2*d, color='brown')

    # Draw the tree top
    draw_circle(x - 0.25*d, y + 2*d, color='green')
    draw_circle(x, y + 2*d, color='green')
    draw_circle(x + 0.25*d, y + 2*d, color='green')
    draw_circle(x + 0.5*d, y + 2*d, color='green')
    draw_circle(x + 0.75*d, y + 2*d, color='green')


def draw_cloud(x,y):
    """
        Draws a garage.
        :params: coordinates for bottom left of cloud.
    """

    draw_circle(x - 0.5*d, y, color = 'grey')
    draw_circle(x, y, color = 'grey')
    draw_circle(x + 0.5*d, y, color = 'grey')
    draw_circle(x - 0.25*d, y + 35, color = 'grey')
    draw_circle(x + 0.25*d, y + 35, color = 'grey')


def draw_house(x, y):
    """
           Draws a house.
           :params: coordinates for bottom left corner of house.
       """

    turtle.Screen()
    draw_rec(x, y, x + 4*d, y + 3*d, color='yellow')
    draw_cloud(x - 1.5*d, y + 4*d)
    draw_cloud(x + 5*d, y + 4*d)

    draw_tree(x - 1.5*d, y)
    draw_tree(x + 5*d, y)

    draw_tri(x - 0.5*d, y + 3*d, x + 2*d, y + 4*d, x + 4.5*d, color='brown')
    draw_window(x + 0.5*d, y + 2*d)
    draw_window(x + 1.25*d, y + 2*d)
    draw_window(x + 2.25*d, y + 2*d)
    draw_window(x + 3*d, y + 2*d)
    draw_garage(x + 0.25*d, y)
    draw_garage(x + 2.5*d, y)
    draw_door(x + 1.75*d, y, color='brown')

    turtle.exitonclick()

if __name__ == "__main__":
    d = 100
    draw_house(-2*d, -2*d)
