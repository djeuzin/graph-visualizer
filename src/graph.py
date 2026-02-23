from dataclasses import dataclass
from node import node
import os
import random
from globals import *
from pygame import draw

@dataclass
class graph:
	nodes: list[node]

	def __init__(self) -> None:
		self.nodes = []

	def __read_file(self, statbuf) -> None:
		nStatbuf = os.stat(GRAPH_PATH)

		if nStatbuf.st_mtime == statbuf.st_mtime and len(self.nodes) != 0:
			return

		statbuf = nStatbuf
		self.nodes = []
		V: int = 0

		with open(GRAPH_PATH) as lines:
			for line in lines:
				if V == 0:
					V = int(line)
					continue

				center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
				self.nodes.append(node(center, adjacencies=[int(x) for x in line.split()]))

	def __connect_nodes(self, n: node, m: node) -> None:
		pygame.draw.line(DISPLAYSURF, BLACK, n.body.center, m.center)

	def draw(self) -> None:
		self.__read_file(statbuf)

		DISPLAYSURF.fill(WHITE)
		for i, node in enumerate(self.nodes):
			for a in node.adjacencies:
				self.__connect_nodes(self.nodes[i], self.nodes[a])
		for node in self.nodes:
			node.draw_node(DISPLAYSURF)

	def move_node(self, idx: int, rel_pos: (int, int)) -> None:
		self.nodes[idx].body.move_ip(rel_pos)
		self.nodes[idx].center = self.nodes[idx].body.center