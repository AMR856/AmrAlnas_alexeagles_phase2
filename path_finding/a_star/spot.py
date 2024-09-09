#!/usr/bin/env python3
from colors import *
from typing import Tuple
from global_values import window
import pygame

class Spot:
	def __init__(self, row: int, col: int, width: int, total_rows: int) -> None:
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neigbours = []
		self.width = width
		self.total_rows = total_rows
	
	def get_pos(self) -> Tuple[int, int]:
		return (self.x, self.y)

	def is_closed(self) -> bool:
		return self.color == RED

	def is_open(self) -> bool:
		return self.color == GREEN

	def is_wall(self) -> bool:
		return self.color == BLACK

	def is_start(self) -> bool:
		return self.color == ORANGE

	def is_end(self) -> bool:
		return self.color == TURQUOISE
	
	def reset(self) -> None:
		self.color = WHITE
	
	def make_closed(self) -> None:
		self.color = RED
	
	def make_opened(self) -> None:
		self.color = GREEN
	
	def make_wall(self) -> None:
		self.color = BLACK
	
	def make_start(self) -> None:
		self.color = ORANGE
	
	def make_end(self) -> None:
		self.color = TURQUOISE
	
	def make_path(self) -> None:
		self.color = PURPLE

	def draw(self):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
	
	def update_neigbours(self, grid) -> None:
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
			self.neigbours.append(grid[self.row + 1][self.col])
		if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
			self.neigbours.append(grid[self.row - 1][self.col])
		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
			self.neigbours.append(grid[self.row][self.col + 1])
		if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
			self.neigbours.append(grid[self.row][self.col - 1])
