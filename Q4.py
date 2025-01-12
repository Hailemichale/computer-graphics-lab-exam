import pygame
from pygame.locals import*
from OpenGL.GL import *
from OpenGL.GLU import *

import sys
def draw_red_line(Canvas):
def draw_shape(Canvas):
    vertices = [(100, 200), (150, 100), (200, 200)]  # Coordinates for triangle
    pygame.draw.polygon(Canvas, (0, 255, 0), vertices)  # Green triangle
def draw_purple_point(Canvas):
    pygame.draw.circle(Canvas, (128, 0, 128), (150, 150), 5)  # Purple point
    pygame.draw.line(Canvas, (255, 0, 0), (50, 50), (250, 50), 3)
def main():
    

    pygame.init()
    Canvas = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Canvas Example")
    Canvas.fill((255, 255, 255))  # White background
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                running = False
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


