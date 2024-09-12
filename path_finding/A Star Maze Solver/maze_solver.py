from global_values import *
from spot import Spot
from queue import PriorityQueue
from typing import List, Callable, Dict, Tuple
import pygame

class MazeSolver:
    @staticmethod
    def reconstruct_path(came_from: Dict[Spot, Spot],
                         current: Spot,
                         draw: Callable[[pygame.surface.Surface, List[List[Spot]],
                                        int, int], None]) -> None:
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()

    @staticmethod
    def heuristics(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def a_star(draw: Callable[[pygame.surface.Surface, List[List[Spot]],
                               int, int], None],
               grid: List[List[Spot]],
               start_spot: Spot,
               end_spot: Spot) -> bool:
        count = 0
        pq = PriorityQueue()
        pq.put((0, count, start_spot))
        came_from = {}
        g_score = {spot: float('inf') for row in grid for spot in row}
        g_score[start_spot] = 0
        f_score = {spot: float('inf') for row in grid for spot in row}
        f_score[start_spot] = MazeSolver.heuristics(start_spot.get_pos(), end_spot.get_pos())

        spot_check_in_priority_queue = set((start_spot,))
        while not pq.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = pq.get()[2]
            spot_check_in_priority_queue.remove(current)

            if current == end_spot:
                MazeSolver.reconstruct_path(came_from, end_spot, draw)
                end_spot.make_end()
                return True

            for neighbour in current.neigbours:
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_g_score + MazeSolver.heuristics(neighbour.get_pos(), end_spot.get_pos())
                    if neighbour not in spot_check_in_priority_queue:
                        count += 1
                        pq.put((f_score[neighbour], count, neighbour))
                        spot_check_in_priority_queue.add(neighbour)
                        neighbour.make_opened()

            draw()

            if current != end_spot:
                current.make_closed()

        return False
    
    @staticmethod
    def dijkstra(draw: Callable[[pygame.surface.Surface, List[List[Spot]],
                               int, int], None],
               grid: List[List[Spot]],
               start_spot: Spot,
               end_spot: Spot) -> bool:
        count = 0
        pq = PriorityQueue()
        pq.put((0, count, start_spot))
        came_from = {}
        g_score = {spot: float('inf') for row in grid for spot in row}
        g_score[start_spot] = 0

        spot_check_in_priority_queue = set((start_spot,))
        while not pq.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = pq.get()[2]
            spot_check_in_priority_queue.remove(current)

            if current == end_spot:
                MazeSolver.reconstruct_path(came_from, end_spot, draw)
                end_spot.make_end()
                return True

            for neighbour in current.neigbours:
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = temp_g_score
                    if neighbour not in spot_check_in_priority_queue:
                        count += 1
                        pq.put((temp_g_score, count, neighbour))
                        spot_check_in_priority_queue.add(neighbour)
                        neighbour.make_opened()

            draw()

            if current != end_spot:
                current.make_closed()

        return False
