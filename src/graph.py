from dataclasses import dataclass
from node import Node
import os
import random
from globals import *
from pygame import draw
import json

@dataclass
class graph:
	adjacency_dict: dict[str, list[str]]
	V: int
	E: int
	deg_list: list[int]

	def __init__(self) -> None:
		with open(GRAPH_PATH, 'r') as file:
			self.adjacency_dict = json.load(file)

		self.deg_list = []

		self.V = self.E = 0

		for node in self.adjacency_dict.keys():
			self.deg_list.append(len(self.adjacency_dict[node]))
			self.E += self.deg_list[-1]
			self.V += 1
			center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
			self.adjacency_dict[node] = (Node(center, node), self.adjacency_dict[node])

		self.E = self.E//2

	def _connect_nodes(self, n: Node, m: Node) -> None:
		pygame.draw.line(DISPLAYSURF, BLACK, n.center, m.center)

	def draw(self) -> None:
		DISPLAYSURF.fill(WHITE)

		for node in self.adjacency_dict.keys():
			n1, _ = self.adjacency_dict[node]

			for a in self.adjacency_dict[node][1]:
				n2, _ = self.adjacency_dict[a]
				self._connect_nodes(n1, n2)

		for node in self.adjacency_dict.keys():
			n, _ = self.adjacency_dict[node]

			n.draw_node(DISPLAYSURF)
			label = label_font.render(f"{n.name}", False, WHITE)
			label_center = tuple(x + y for x, y in zip(n.center, label_offset))
			DISPLAYSURF.blit(label, label_center)
			n.visited = False

		text_surface = my_font.render(f"Number of vertices: {self.V}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0,0))
		text_surface = my_font.render(f"Number of edges: {self.E}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0,20))

	def move_node(self, node: Node, rel_pos: (int, int)) -> None:
		node.body.move_ip(rel_pos)
		node.center = node.body.center