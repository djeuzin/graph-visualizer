import pygame
import sys
import typing
from pygame.locals import *
import random
import os

BLUE: (int, int, int) = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
NODE_RADIUS = 15
NODE_COLOR = BLUE
GRAPH_PATH = "graph.txt"
statbuf = os.stat(GRAPH_PATH)

class node:
	def __init__(self, 
				center: (int, int), 
				radius: float = NODE_RADIUS, 
				color: (int, int, int) = NODE_COLOR,
				adjacencies: list[int] = []):
		self.center = center
		self.radius = radius
		self.color  = color
		self.adjacencies = adjacencies

node_list: list[node] = []

def draw_node(n: node) -> None:
	pygame.draw.circle(DISPLAYSURF, n.color, n.center, n.radius)

def connect_nodes(n: node, m: node) -> None:
	pygame.draw.line(DISPLAYSURF, BLACK, n.center, m.center)

def init_screen():
	pygame.init()
	DISPLAYSURF.fill(WHITE)
	FPS = pygame.time.Clock()
	FPS.tick(60)
	pygame.display.set_caption("Graph visualizer")

def read_graph() -> None:
	nStatbuf = os.stat(GRAPH_PATH)
	global node_list
	global statbuf

	if nStatbuf.st_mtime == statbuf.st_mtime and len(node_list) != 0:
		return

	statbuf = nStatbuf
	node_list = []
	V: int = 0
	i: int = 0
	DISPLAYSURF.fill(WHITE)

	with open(GRAPH_PATH) as lines:
		for line in lines:
			if V == 0:
				V = int(line)
				continue

			center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
			node_list.append(node(center, adjacencies=[int(x) for x in line.split()]))
			i += 1

def draw_graph() -> None:
	for i, node in enumerate(node_list):
		for a in node.adjacencies:
			connect_nodes(node_list[i], node_list[a])
		draw_node(node_list[i]);

def main():
	init_screen()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			read_graph()

			draw_graph()

			pygame.display.update()

if __name__ == "__main__":
	main()