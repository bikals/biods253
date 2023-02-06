#!/usr/bin/env python3

import turtle
from affine import Affine
import sys

class BasicDrawing:
    def __init__(self, turtle):
        self._turtle = turtle
        self._affine_matrix = Affine.identity()
    
    def set_affine(self, affine_matrix=None):
        if affine_matrix is None:
            affine_matrix = Affine.identity()
        self._affine_matrix = affine_matrix
        

    def draw_line(self, x1, y1, x2, y2):
        """
            Draws a line.
            :params: coordinates for the two ends of the line.
        """
        t = self._turtle

        t.up()
        # transform the coordinates before drawing.
        x1, y1 = self._affine_matrix * (x1, y1)
        x2, y2 = self._affine_matrix * (x2, y2)

        t.setpos(x1, y1)
        t.down()
        t.setpos(x2, y2)

    def draw_circle(self, x, y, radius=50, color='black', fill=True):
        """
            Draws a circle.
            x: x coord bottom of circle
            y: y coord bottom of circle
            radius: radius
            color: fill color
        """
        t = self._turtle

        t.up()

        # transform the coordinates before drawing.

        # warning this will break with things like sheer

        # because we can have rotation as well as scaling, we find the centre of the circle
        # then map it, then back compute the radius using dist fcn
        y_rad = y + radius
        x_rad, y_rad = self._affine_matrix * (x, y_rad)
        x, y = self._affine_matrix * (x, y)

        radius = ((y - y_rad) ** 2 + (x - x_rad)**2) ** 0.5


        t.setpos(x, y)
        t.color(color)
        t.down()
        if fill:
            t.begin_fill()
        t.circle(radius)
        if fill:
            t.end_fill()

# TODO: this is really ugly. All the rest of these methods should 
# actually be in the drawing class, but I didn't want to break anything

global_basic_drawing = BasicDrawing(turtle)
draw_circle = lambda *args, **kwargs: global_basic_drawing.draw_circle(*args, **kwargs)
draw_line = lambda *args, **kwargs: global_basic_drawing.draw_line(*args, **kwargs)
#######


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




def draw_window(x, y, color='blue', fill=True, cracks=False):
    """
        Draws a window.
        :params: coordinates for bottom left corner of window.
    """
    draw_rec(x, y, x + 0.5*d, y + 0.5*d, color, fill)
    turtle.color('black')
    draw_line(x + 0.25*d, y, x + 0.25*d, y + 0.5*d)
    draw_line(x, y + 0.25*d, x + 0.5*d, y + 0.25*d)

    if cracks:
        turtle.color('white')
        draw_line(x, y, x + 0.5*d, y + 0.5*d)
        turtle.color('black')



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
    draw_circle(x - 0.25*d, y + 0.35*d, color = 'grey')
    draw_circle(x + 0.25*d, y + 0.35*d, color = 'grey')


def draw_house(x, y, clouds=True, cracks=False):
    """
           Draws a house.
           :params: coordinates for bottom left corner of house.
       """    
    turtle.Screen()
    draw_rec(x, y, x + 4*d, y + 3*d, color='yellow')
    if clouds:
        draw_cloud(x - 1.5*d, y + 4*d)
        draw_cloud(x + 5*d, y + 4*d)

    draw_tree(x - 1.5*d, y)
    draw_tree(x + 5*d, y)

    draw_tri(x - 0.5*d, y + 3*d, x + 2*d, y + 4*d, x + 4.5*d, color='brown')
    draw_window(x + 0.5*d, y + 2*d)
    draw_window(x + 1.25*d, y + 2*d, cracks=cracks)
    draw_window(x + 2.25*d, y + 2*d, cracks=cracks)
    draw_window(x + 3*d, y + 2*d)
    draw_garage(x + 0.25*d, y)
    draw_garage(x + 2.5*d, y)
    draw_door(x + 1.75*d, y, color='brown')
    turtle.color('black')
  
#    turtle.exitonclick()

if __name__ == "__main__":
    d = 100
    turtle.speed(0)
    assert len(sys.argv) == 2
    state = sys.argv[1]
    assert state in {'pre', 'post'}, ' first arg must be "pre" or "post"'
    if state == 'pre':
        clouds = False
        cracks = False
        rotate = 0
    elif state == 'post':
        clouds = True
        cracks = True
        rotate = 10
    else:
        assert 0    

    # draw houses
    for i in range(-1,2,1):
        # each house is 25% the size of the original drawing since we've zoomed out
        # we are also moving it based on its position
        affine_matrix = Affine.identity()

        if i == 1 and rotate:
            # rotate the house. Also disable clouds because they would look very funny
            # rotated.
            # todo: do not rotate clouds
            clouds = False
            affine_matrix = Affine.rotation(rotate)

        affine_matrix *= Affine.translation(-4.5 * d * i, 0) * Affine.scale(0.25)

        if i == 0:
            # smaller house
            affine_matrix *= Affine.scale(0.9)

        global_basic_drawing.set_affine(affine_matrix)
        draw_house(-2*d, -2*d, cracks=cracks, clouds=clouds)

    turtle.exitonclick()