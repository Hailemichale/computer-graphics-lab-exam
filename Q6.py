import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GLU import *

def draw_line():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  
    glVertex2f(-0.5, 0.0)  
    glVertex2f(0.5, 0.0)   
    glEnd()


pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("OpenGL Line")

glClearColor(0.0, 0.0, 0.0, 1.0)  
glOrtho(-1, 1, -1, 1, -1, 1)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    pygame.display.flip()

pygame.quit()
