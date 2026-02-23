from dataclasses import dataclass
from pygame import Rect, draw
from globals import *

@dataclass
class node:
	center: (int, int)
	radius: float
	color:  (int, int, int)
	adjacencies: list[int]
	body: Rect

	def __init__(self, 
				center: (int, int), 
				radius: float = NODE_RADIUS, 
				color: (int, int, int) = NODE_COLOR,
				adjacencies: list[int] = []):
		self.center = center
		self.radius = radius
		self.color  = color
		self.adjacencies = adjacencies
		rect_center = (center[0] - radius, center[1] - radius)
		self.body = Rect(rect_center, (self.radius*2, self.radius*2))

	def draw_node(self, surface) -> None:
		draw.circle(surface, self.color, self.body.center, self.radius)