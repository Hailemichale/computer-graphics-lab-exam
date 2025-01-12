import pygame 
from pygame.locals import*
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  
    glVertex2f(-0.5, 0.0)  
    glVertex2f(0.5, 0.0)   
    glEnd()
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)  
    glVertex2f(-0.5, -0.5)  
    glVertex2f(0.5, -0.5)   
    glVertex2f(0.0, 0.5)    
    glEnd()
def draw_point():
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)  
    glVertex2f(0.0, 0.0)  
    glEnd()
pygame.init()
Canvas = pygame.display.set_mode((500, 400)) 
pygame.display.set_caption("main")

glClearColor(0.0, 0.0, 0.0, 1.0)  
glOrtho(-1, 1, -1, 1, -1, 1)
glPointSize(5.0)

running=True
Canvas.fill((255, 255, 255))
running=True

while not running: 
    for event in pygame.event.get(): 
        if event.type == KEYDOWN: 
            running = False 
        elif event.type == KEYDOWN:
            if event.Key == K_F1:
                print("F1")
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    draw_triangle()
    draw_point()
    pygame.display.flip() 
    pygame.time.wait=20
pygame.quit() 