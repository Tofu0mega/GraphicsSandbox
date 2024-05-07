import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, sqrt, pi
from Modules import *
import sys
import os
evalbuffer=[]
def key_callback(window, key, scancode, action, mods):
    
    global testcordx,testcordy,testsize,testsize2,precision,cycle,colorcycle,evalbuffer
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
        os.system('cls')
        print("current precison:",precision)
    elif key == glfw.KEY_Z and (action == glfw.PRESS or action == glfw.REPEAT):
        evalbuffer=evalbuffer[:-1]
    elif key == glfw.KEY_S and (action == glfw.PRESS or action == glfw.REPEAT):
       
        NewfileName=input("Save File As:")
        os.makedirs("user_shapes", exist_ok=True)
        NewfileName=NewfileName+".txt"
        file_path = os.path.join("user_shapes", NewfileName)
        
        with open(file_path,'w') as file:
            stringtowrite='\n'.join(evalbuffer)
            file.write(stringtowrite)
        
        
            
        
        
    
    elif key == glfw.KEY_SPACE and (action == glfw.PRESS or action == glfw.REPEAT):
        if cycle == 0:
            evalstring=f"draw_circle({testcordx},{testcordy},{testsize},32,colors[{colorcycle}])"
            evalbuffer.append(evalstring)       
        elif cycle == 1:
            evalstring=f"triangle({testcordx},{testcordy},{testsize},{testsize2},colors[{colorcycle}])"
            evalbuffer.append(evalstring)
        elif cycle == 2:
            evalstring=f"filledtriangle({testcordx},{testcordy},{testsize},{testsize2},colors[{colorcycle}])"
            evalbuffer.append(evalstring)
        elif cycle == 3:
            evalstring=f"draw_rectangle({testcordx},{testcordy},{testsize},{testsize2},colors[{colorcycle}])"
            evalbuffer.append(evalstring)
        elif cycle == 4:
            evalstring=f"draw_rectangle({testcordx},{testcordy},{testsize},{testsize},colors[{colorcycle}])"
            evalbuffer.append(evalstring)
        
            
            
        
    elif key == glfw.KEY_DELETE and (action == glfw.PRESS or action == glfw.REPEAT):
        cycle=cycle+1
        cycle=cycle%5
    elif key == glfw.KEY_PAUSE and (action == glfw.PRESS or action == glfw.REPEAT):
        colorcycle=colorcycle+1
        length=len(colors)
        colorcycle=colorcycle%length
    

def main():
    if not glfw.init():
        print("Failed to initialize GLFW")
        return -1

    window = glfw.create_window(1000, 1000, "Sandbox", None, None)
    if not window:
        glfw.terminate()
        return -1

    glfw.make_context_current(window)


    while not glfw.window_should_close(window):
        starterbuffer()
        #draw here
        #layered work xa no option for opacity
        #move by layers lower the value lower the layer
        for layer in evalbuffer:
            eval(layer)
        
        glfw.set_key_callback(window, key_callback)
        if cycle == 0:
            draw_circle(testcordx,testcordy,testsize,32,colors[colorcycle])           
        elif cycle == 1:
            triangle(testcordx,testcordy,testsize,testsize2,colors[colorcycle])
        elif cycle == 2:
            filledtriangle(testcordx,testcordy,testsize,testsize2,colors[colorcycle])
        elif cycle == 3:
            draw_rectangle(testcordx,testcordy,testsize,testsize2,colors[colorcycle])
        elif cycle == 4:
            draw_rectangle(testcordx,testcordy,testsize,testsize,colors[colorcycle])
        else:
            break
            
        
        
        
        
        
        
        
        
    
            
            
        
       
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()