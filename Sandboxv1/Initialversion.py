import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, sqrt, pi

#to test proper placement coordinates (preferebly delete when submitting)
testcordx=600
testcordy=600
testsize=100
testsize2=100
precision=1
def key_callback(window, key, scancode, action, mods):
    
    global testcordx,testcordy,testsize,testsize2,precision
    if key == glfw.KEY_ESCAPE and (action == glfw.PRESS or action == glfw.REPEAT):
        glfw.set_window_should_close(window, True)
    elif key == glfw.KEY_LEFT and (action == glfw.PRESS or action == glfw.REPEAT):
        testcordx=testcordx-precision
    elif key == glfw.KEY_RIGHT and (action == glfw.PRESS or action == glfw.REPEAT):
        testcordx=testcordx+precision
    elif key == glfw.KEY_UP and (action == glfw.PRESS or action == glfw.REPEAT):
       testcordy=testcordy-precision
    elif key == glfw.KEY_DOWN and (action == glfw.PRESS or action == glfw.REPEAT):
        testcordy=testcordy+precision
    elif key == glfw.KEY_PAGE_UP and (action == glfw.PRESS or action == glfw.REPEAT):
        testsize=testsize+precision
    elif key == glfw.KEY_PAGE_DOWN and (action == glfw.PRESS or action == glfw.REPEAT):
        testsize=testsize-precision
    elif key == glfw.KEY_HOME and (action == glfw.PRESS or action == glfw.REPEAT):
        testsize2=testsize2+precision
    elif key == glfw.KEY_END and (action == glfw.PRESS or action == glfw.REPEAT):
        testsize2=testsize2-precision
    elif key == glfw.KEY_INSERT and (action == glfw.PRESS or action == glfw.REPEAT):
        precision=(precision+1)%6
        print("current precison:",precision)
    elif key == glfw.KEY_SPACE and (action == glfw.PRESS or action == glfw.REPEAT):
        print(testcordx,",",testcordy,",",testsize,",",testsize2)

#colors associated with logo
blue = [0., 0., 0.9, 1.0]
yellow = [1.0, 1.0, 0.0, 1.0]
black = [0.0, 0.0, 0.0, 1.0]
red = [1.0, 0.0, 0.0, 1.0]
light_pink = [1.0, 0.714, 0.757, 1.0]
white=[1.0,1.0,1.0,1.0]
off_white = [0.96, 0.96, 0.96, 1.0]




#fix center for circle
x_center=600
y_center=600


#draws circle
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

    glColor4fv(off_white)  
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
    

def draw_rectangle(x, y, width, height,color):
    glColor4fv(color)  
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
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


    

def main():
    if not glfw.init():
        print("Failed to initialize GLFW")
        return -1

    window = glfw.create_window(1000, 1000, "NTB_LOGOS", None, None)
    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, x_center*2 ,y_center*2, 0, 0, 1)
        glColor3f(1.0, 1.0, 1.0)
        #draw here
        #layered work xa no option for opacity
        #move by layers lower the value lower the layer
        
        glfw.set_key_callback(window, key_callback)
        
        
        
        
        
    
            
            
        
       
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()