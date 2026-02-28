import pygame
import os

SCREEN_WIDTH:  int = 900
SCREEN_HEIGHT: int = 700
GRAPH_PATH:    str = "src/graph.txt"
NODE_RADIUS:   int = 15

BLUE:  (int, int, int) = (0, 0, 255)
RED:   (int, int, int) = (255, 0, 0)
GREEN: (int, int, int) = (0, 255, 0)
BLACK: (int, int, int) = (0, 0, 0)
WHITE: (int, int, int) = (255, 255, 255)

NODE_COLOR: (int, int, int) = BLUE

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
statbuf = os.stat(GRAPH_PATH)