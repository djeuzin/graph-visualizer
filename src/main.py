import pygame
import sys
import typing
from pygame.locals import *
import random
import os
from node import *
from graph import graph
from globals import *

def init_screen():
	pygame.init()
	DISPLAYSURF.fill(WHITE)
	FPS = pygame.time.Clock()
	FPS.tick(60)
	pygame.display.set_caption("Graph visualizer")

def main():
	init_screen()

	G = graph()
	active_node = None

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					for key in G.nodes.keys():
						node = G.nodes[key]

						if node.body.collidepoint(event.pos):
							active_node = node
				if event.button == 3:
					new_center = pygame.mouse.get_pos()
					new_node = Node(new_center, f"v{G.V+1}")

					G.add(new_node)

			if event.type == MOUSEBUTTONUP:
				if event.button == 1:
					active_node = None

			if event.type == pygame.MOUSEMOTION:
				if active_node != None:
					G.move_node(active_node, event.rel)

			G.draw()

			pygame.display.update()

if __name__ == "__main__":
	main()