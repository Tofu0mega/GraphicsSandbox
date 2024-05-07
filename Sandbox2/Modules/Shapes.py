from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, sqrt, pi


def draw_circle(x_cordinate, y_cordinate, radius, segment, color):
    glBegin(GL_POLYGON) 
    glColor4fv(color)
    for i in range(segment):
        theta = 2.0 * pi * i / segment
        x = radius * cos(theta) + x_cordinate
        y = radius * sin(theta) + y_cordinate
        glVertex2f(x, y)
    glEnd()



def triangle(cx, cy, r_outer, r_inner, color):
    glLineWidth(4.0) 
    glColor4fv(color) 
    glBegin(GL_LINE_LOOP) 
    x1_outer, y1_outer, x2_outer, y2_outer, x3_outer, y3_outer = cx, cy - r_outer, cx - r_outer * sqrt(3) / 2, cy + r_outer / 2, cx + r_outer * sqrt(3) / 2, cy + r_outer / 2
    glVertex2f(x1_outer, y1_outer)
    glVertex2f(x2_outer, y2_outer)
    glVertex2f(x3_outer, y3_outer)
    glEnd()
    

def filledtriangle(cx, cy, r_outer, r_inner, color):
    glLineWidth(4.0) 
    glColor4fv(color) 
    glBegin(GL_LINE_LOOP) 
    x1_outer, y1_outer, x2_outer, y2_outer, x3_outer, y3_outer = cx, cy - r_outer, cx - r_outer * sqrt(3) / 2, cy + r_outer / 2, cx + r_outer * sqrt(3) / 2, cy + r_outer / 2
    glVertex2f(x1_outer, y1_outer)
    glVertex2f(x2_outer, y2_outer)
    glVertex2f(x3_outer, y3_outer)
    glEnd()

    glColor4fv(color)  
    glBegin(GL_LINE_LOOP)
    x1_inner, y1_inner, x2_inner, y2_inner, x3_inner, y3_inner = cx, cy - r_inner, cx - r_inner * sqrt(3) / 2, cy + r_inner / 2, cx + r_inner * sqrt(3) / 2, cy + r_inner / 2
    glVertex2f(x1_inner, y1_inner)
    glVertex2f(x2_inner, y2_inner)
    glVertex2f(x3_inner, y3_inner)
    glEnd()


    #for filling white colors
    glColor4fv(color)  
    glBegin(GL_QUADS) 
    glVertex2f(x1_inner, y1_inner)
    glVertex2f(x2_inner, y2_inner)
    glVertex2f(x2_outer, y2_outer)
    glVertex2f(x1_outer, y1_outer)
    glEnd()
    

    glBegin(GL_QUADS) 
    glVertex2f(x2_inner, y2_inner)
    glVertex2f(x3_inner, y3_inner)
    glVertex2f(x3_outer, y3_outer)
    glVertex2f(x2_outer, y2_outer)
    glEnd()

    glBegin(GL_QUADS)  
    glVertex2f(x3_inner, y3_inner)
    glVertex2f(x1_inner, y1_inner)
    glVertex2f(x1_outer, y1_outer)
    glVertex2f(x3_outer, y3_outer)
    glEnd()

def draw_slant_rectangle(startx, starty,endx,endy, width, height,color):
    glColor4fv(color)  
    glBegin(GL_QUADS)
    glVertex2f(startx, starty)
    glVertex2f(startx + width, starty)
    glVertex2f(endx + width, endy + height)
    glVertex2f(endx, endy + height)
    glEnd()


def draw_semi_circle(center_x, center_y, radius,segments,start,end, color):
       
    # Adjust the starting and ending angles to rotate the semi-circle
    start_angle =-pi/2*start   # Start from the top middle
    end_angle =  -pi/2*end  # End at the bottom middle, forming an upward curve

    glBegin(GL_TRIANGLE_FAN)
    glColor4fv(color)
    glVertex2f(center_x, center_y)  # Center vertex
    
    for i in range(segments + 1):
        theta = start_angle + (end_angle - start_angle) * (i / segments)  # Interpolate angle
        x = center_x + radius * cos(theta)
        y = center_y + radius * sin(theta)
        glVertex2f(x, y)
    
    glEnd()


def draw_rectangle(x, y, width, height,color):
    glColor4fv(color)  
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()