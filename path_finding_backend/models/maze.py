import networkx as nx 
from typing import Tuple, List
import random
import matplotlib.pyplot as plt

class Maze:
    valid_difficulties = ['easy', 'normal', 'hard']

    def __init__(self, rows: int, cols: int, difficuity: str) -> None:
        self.rows = rows
        self.cols = cols
        self.__maze = nx.grid_2d_graph(rows, cols)
        self.difficulty = difficuity
        self.__start = None
        self.__end = None
        self.__obstacles = set()
        self.__path = list()
        self.generating_start_and_end()
        self.generating_obstacles()

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int) -> None:
        if (rows >= 0):
            self.__rows = rows
        else:
            raise ValueError('Rows must be zero or higher')
    
    @property
    def cols(self) -> int:
        return self.__cols

    @cols.setter
    def cols(self, cols: int) -> None:
        if (cols >= 0):
            self.__cols = cols
        else:
            raise ValueError('Columns must be zero or higher')
    @property
    def path(self) -> List[Tuple[int, int]]:
        return self.__path
    
    @path.setter
    def path(self, value: List[Tuple[int, int]]) -> None:
        self.__path = value

    @property
    def maze(self) -> nx.grid_2d_graph:
        return self.__maze

    @property
    def obstacles(self):
        return self.__obstacles

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty: str) -> None:
        if difficulty.lower() in Maze.valid_difficulties:
            self.__difficulty = difficulty
        else:
            raise ValueError('The input difficulty is not valid')

    def generating_start_and_end(self) -> None:
        start = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        end = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        
        while start == end:
            end = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        
        self.__start = start
        self.__end = end

    @property
    def start(self) -> int:
        return self.__start

    @property
    def end(self) -> int:
        return self.__end

    def generating_obstacles(self) -> None:
        if self.difficulty.lower() == 'easy':
            num_obstacles = round((self.rows * self.cols) / 6)
        elif self.difficulty.lower() == 'normal':
            num_obstacles = round((self.rows * self.cols) / 4)
        else:
            num_obstacles = round((self.rows * self.cols) / 3)
        while len(self.obstacles) < num_obstacles:
            obstacle = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
            if (obstacle != self.start) and (obstacle != self.end) and (obstacle not in self.obstacles):
                self.obstacles.add(obstacle)
                try:
                    self.maze.remove_node(obstacle)
                except nx.exception.NetworkXError as err:
                    raise ValueError('Out of index node')

    def update_grid_size(self) -> None:
        self.maze = nx.grid_2d_graph(self.rows, self.cols)
        self.generating_start_and_end()
        self.generating_obstacles()

    def solve_maze(self) -> List[Tuple[int, int]]:
        try:
            return nx.astar_path(self.maze, self.start, self.end, Maze.heuristics)
        except nx.NetworkXNoPath as err:
            return []

    def drawing_nodes(self) -> None:
        plt.clf()
        pos = {(x, y): (x, y) for x, y in self.maze.nodes()}
        nx.draw(self.maze, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
        nx.draw_networkx_nodes(self.maze, pos, nodelist=[self.start], node_color="green", node_size=600)
        nx.draw_networkx_nodes(self.maze, pos, nodelist=[self.end], node_color="red", node_size=600)
        if len(self.path) > 0:
            nx.draw_networkx_nodes(self.maze, pos, nodelist=self.path, node_color="purple", node_size=600)
        plt.show()

    @staticmethod
    def heuristics(point1: Tuple[int, int], point2: Tuple[int, int]) -> int: 
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)
