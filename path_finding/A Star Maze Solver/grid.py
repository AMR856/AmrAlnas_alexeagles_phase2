from typing import List, Tuple
from colors import *
from maze_solver import MazeSolver
from spot import Spot
from global_values import window
import pygame
import random

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

    @staticmethod
    def is_valid_move(x: int, y: int, rows: int, grid: List[List[Spot]]):
            return 0 <= x < rows and 0 <= y < rows and grid[x][y].is_wall()

    @staticmethod
    def maze_generation(grid: List[List[Spot]], rows: int) -> None:
        DIRECTIONS = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        for i in range(rows):
            for j in range(rows):
                grid[i][j].make_wall()

        def dfs(x, y):
            grid[x][y].reset()
            random.shuffle(DIRECTIONS)
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if Grid.is_valid_move(nx, ny, rows, grid):
                    grid[x + dx // 2][y + dy // 2].reset()
                    dfs(nx, ny)
        dfs(1, 1)
        start_spot = grid[1][1]
        end_spot = grid[rows-2][rows-2]
        start_spot.make_start()
        end_spot.make_end()
        return (start_spot, end_spot)
