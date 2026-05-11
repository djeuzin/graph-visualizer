from dataclasses import dataclass
from pygame import Rect, draw
from globals import *

@dataclass
class Node:
	center: (int, int)
	radius: float
	color:  (int, int, int)
	body: Rect
	visited: bool
	name: str

	def __init__(self, 
				center: (int, int),
				name: str, 
				radius: float = NODE_RADIUS, 
				color: (int, int, int) = NODE_COLOR):
		self.center = center
		self.name = name
		self.radius = radius
		self.color  = color
		rect_center = (center[0] - radius, center[1] - radius)
		self.body = Rect(rect_center, (self.radius*2, self.radius*2))
		self.visited = False

	def draw_node(self, surface) -> None:
		draw.circle(surface, self.color, self.body.center, self.radius)