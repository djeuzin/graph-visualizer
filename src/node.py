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
	label_offset: (int, int)

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
		self.label_offset = (-7, -7)

	def draw_node(self, surface, color, label_font) -> None:
		draw.circle(surface, color, self.body.center, self.radius)

		label = label_font.render(f"{self.name}", False, WHITE)
		label_center = tuple(x + y for x, y in zip(self.center, self.label_offset))
		surface.blit(label, label_center)