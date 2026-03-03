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

	def __init__(self) -> None:
		self.nodes = []
		self.statbuf = os.stat(GRAPH_PATH)

	def __read_file(self) -> None:
		nStatbuf = os.stat(GRAPH_PATH)

		if nStatbuf.st_mtime == self.statbuf.st_mtime and len(self.nodes) != 0:
			return

		self.statbuf = nStatbuf
		self.nodes = []

		with open(GRAPH_PATH) as lines:
			for line in lines:
				center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
				adj = [int(x) for x in line.split()]
				self.nodes.append(node(center, 
									   adjacencies=[i for i, val in enumerate(adj) if val != 0]))

	def __connect_nodes(self, n: node, m: node) -> None:
		pygame.draw.line(DISPLAYSURF, BLACK, n.body.center, m.center)

	def draw(self) -> None:
		self.__read_file()

		DISPLAYSURF.fill(WHITE)

		for node in self.nodes:
			for a in node.adjacencies:
				self.__connect_nodes(node, self.nodes[a])

		for node in self.nodes:
			node.draw_node(DISPLAYSURF)

	def move_node(self, idx: int, rel_pos: (int, int)) -> None:
		self.nodes[idx].body.move_ip(rel_pos)
		self.nodes[idx].center = self.nodes[idx].body.center