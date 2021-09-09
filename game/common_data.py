import pygame 
import sys 

sys.path.append('./objects')

from objects import Snake

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 60)
agent = Snake()
blocks = []