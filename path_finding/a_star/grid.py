from typing import List, Tuple
from colors import *
from spot import Spot
from global_values import window
import pygame

class Grid:
    @staticmethod
    def make_grid(rows: int, width: int) -> List[List[Spot]]:
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                spot  = Spot(i, j, gap, rows)
                grid[i].append(spot)

        return grid

    @staticmethod
    def draw_grid_lines(rows: int, width: int) -> None:
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))

    @staticmethod
    def draw(grid: List[List[Spot]], rows: int, width: int) -> None:
        window.fill(WHITE)
        for row in grid:
            for spot in row:
                spot.draw()
            
        Grid.draw_grid_lines(rows, width)
        pygame.display.update()

    @staticmethod
    def get_clicked_pos(pos : Tuple[int, int], rows: int, width: int) -> Tuple[int, int]:
        gap = width // rows
        y, x = pos
        row = y // gap
        col = x // gap
        return (row, col)
