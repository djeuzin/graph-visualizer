from dataclasses import dataclass
from node import node
import os
import random
from globals import *
from pygame import draw

@dataclass
class graph:
	nodes: list[node]
	statbuf: os.stat_result
	V: int
	E: int

	def __init__(self) -> None:
		self.nodes = []
		self.statbuf = os.stat(GRAPH_PATH)
		self.V = self.E = 0

	def __read_file__(self) -> None:
		nStatbuf = os.stat(GRAPH_PATH)

		if nStatbuf.st_mtime == self.statbuf.st_mtime and len(self.nodes) != 0:
			return

		self.statbuf = nStatbuf
		self.nodes = []
		self.E = 0

		with open(GRAPH_PATH) as lines:
			for i, line in enumerate(lines):
				center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
				adjacencies = [int(x) for x in line.split()]

				for j in range(i+1):
					self.E += adjacencies[j]

				adjacencies=[i for i, val in enumerate(adjacencies) if val != 0]
				self.nodes.append(node(center, adjacencies=adjacencies))

		self.V = len(self.nodes)

	def __connect_nodes__(self, n: node, m: node) -> None:
		pygame.draw.line(DISPLAYSURF, BLACK, n.body.center, m.center)

	def draw(self) -> None:
		self.__read_file__()

		DISPLAYSURF.fill(WHITE)

		for node in self.nodes:
			for a in node.adjacencies:
				self.__connect_nodes__(node, self.nodes[a])

		for node in self.nodes:
			node.draw_node(DISPLAYSURF)
			node.visited = False

		text_surface = my_font.render(f"Number of vertices: {self.V}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0,0))
		text_surface = my_font.render(f"Number of edges: {self.E}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0,20))

	def move_node(self, idx: int, rel_pos: (int, int)) -> None:
		self.nodes[idx].body.move_ip(rel_pos)
		self.nodes[idx].center = self.nodes[idx].body.center