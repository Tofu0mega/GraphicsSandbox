import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
#fix center for circle
x_center=600
y_center=600

def starterbuffer():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, x_center*2 ,y_center*2, 0, 0, 1)
    glColor3f(1.0, 1.0, 1.0)
    
    