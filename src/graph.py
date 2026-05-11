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
	nodes: dict[str, list[Node]]
	edit_mode: bool
	to_connect: list[Node]

	def __init__(self) -> None:
		with open(GRAPH_PATH, 'r') as file:
			self.adjacency_dict = json.load(file)

		self.deg_list = []
		self.nodes = {}
		self.V = self.E = 0
		self.edit_mode = False
		self.to_connect = []

		for node in self.adjacency_dict.keys():
			self.deg_list.append(len(self.adjacency_dict[node]))
			self.E += self.deg_list[-1]
			self.V += 1

			center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
			self.nodes[node] = Node(center, node)

		self.E = self.E//2

	def _connect_nodes(self, n: Node, m: Node) -> None:
		pygame.draw.line(DISPLAYSURF, BLACK, n.center, m.center)

	def draw(self) -> None:
		DISPLAYSURF.fill(WHITE)

		for node in self.nodes.keys():
			n1 = self.nodes[node]

			for a in self.adjacency_dict[node]:
				n2 = self.nodes[a]
				self._connect_nodes(n1, n2)

		for node in self.adjacency_dict.keys():
			n = self.nodes[node]

			color = BLUE if n not in self.to_connect else GREEN
			n.draw_node(DISPLAYSURF, color)
			label = label_font.render(f"{n.name}", False, WHITE)
			label_center = tuple(x + y for x, y in zip(n.center, label_offset))
			DISPLAYSURF.blit(label, label_center)
			n.visited = False

		text_surface = my_font.render(f"Number of vertices: {self.V}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0,0))
		text_surface = my_font.render(f"Number of edges: {self.E}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0,20))
		str_mode = "add/move" if not self.edit_mode else "connect/delete"
		text_surface = my_font.render(f"Modo: {str_mode}", False, (0, 0, 0))
		DISPLAYSURF.blit(text_surface, (0, 40))

	def move_node(self, node: Node, rel_pos: (int, int)) -> None:
		node.body.move_ip(rel_pos)
		node.center = node.body.center

	def add(self, node: Node) -> None:
		self.adjacency_dict[node.name] = []
		self.nodes[node.name] = node

		with open(GRAPH_PATH, 'w') as file:
			json.dump(self.adjacency_dict, file, indent=4)

		self.V += 1

	def connect(self, n1: Node, n2: Node) -> None:
		name1 = n1.name
		name2 = n2.name

		if name1 not in self.adjacency_dict[name2]:
			self.E += 1
			self.adjacency_dict[name1].append(name2)
			self.adjacency_dict[name2].append(name1)

			with open(GRAPH_PATH, 'w') as file:
				json.dump(self.adjacency_dict, file, indent=4)

	def remove(self, n1: Node) -> None:
		name = n1.name

		nbs = self.adjacency_dict[name]
		self.E -= len(nbs)
		self.V -= 1

		del self.nodes[name]
		
		for nb in nbs:
			self.adjacency_dict[nb].remove(name)

		del self.adjacency_dict[name]

		with open(GRAPH_PATH, 'w') as file:
			json.dump(self.adjacency_dict, file, indent=4)