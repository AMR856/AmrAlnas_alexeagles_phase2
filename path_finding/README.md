## Path Finding Program using Dijkstra and A Star

This is a simple maze solver program that uses [A Star](https://en.wikipedia.org/wiki/A*_search_algorithm)  mainly Algorithm to solve the maze and [Pygame](https://www.pygame.org/news) to make the GUI

### The Program Main Function

First of all, I try to take the number of rows from the user using command line parameters and here are they:
- Number of rows
- Type of the maze creation (random or manual)
- Algorithm type (A Star or Dijkstra)

Example:
```
    python3 task.py 30 random a
```
The main program file keeps running until the user exits it

### Spot Class

This is the class that represents the cells in the grid, It has many proprites that will let us know its status which are:
- Opened
- Closed
- Path
- Path
- Not Determined Yet

It also has a method to determine its neigbours to know where it can go next
```
def update_neigbours(self, grid) -> None:
    if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
        self.neigbours.append(grid[self.row + 1][self.col])
    if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
        self.neigbours.append(grid[self.row - 1][self.col])
    if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
        self.neigbours.append(grid[self.row][self.col + 1])
    if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
        self.neigbours.append(grid[self.row][self.col - 1])
```

### Grid Class

This the class that will contain the grid of our application and the grid is just a list of lists of Spot Objects.

The class has many methods from making the grid and drawing it to find the clicked position in the grid.

Here is the main function which is making the grid:
```
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
```
### Determining the Used Algorithm
The third parameter in the command line arguments is determining the used algorithm which can be a for `A Star` or d for `Dijkstra` and here is the code that is doing this logic
```
if algorithm_type.lower() == 'a star' or algorithm_type.lower() == 'a':
    MazeSolver.a_star(lambda: Grid.draw(grid, rows, WIDTH), grid, start_spot, end_spot)
elif algorithm_type.lower() == 'dijkstra' or algorithm_type.lower() == 'd':
    MazeSolver.dijkstra(lambda: Grid.draw(grid, rows, WIDTH), grid, start_spot, end_spot)
```
### Cleaning the Grid
The user can clean the grid by pressing C.
```
if event.key == pygame.K_c:
    start_spot = None
    end_spot = None
    grid = Grid.make_grid(rows, WIDTH)
```

