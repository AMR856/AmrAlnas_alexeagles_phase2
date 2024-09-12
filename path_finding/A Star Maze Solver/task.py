import pygame
from global_values import *
from grid import Grid
from maze_solver import MazeSolver
import sys

if __name__ == '__main__':
	try:
		rows = int(sys.argv[1])
	except Exception as err:
		rows = 30
	try:
		random_or_manual = sys.argv[2]
	except Exception as err:
		random_or_manual = 'random'
	try:
		algorithm_type = sys.argv[3]
	except Exception as err:
		algorithm_type = 'a'

	grid = Grid.make_grid(rows, WIDTH)
	generated = False
	start_spot = None
	end_spot = None
	run = True
	while run:
		Grid.draw(grid, rows, WIDTH)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if random_or_manual.lower() == 'man' or random_or_manual.lower() == 'manual':
				if pygame.mouse.get_pressed()[0]:
					mouse_pos_pygame = pygame.mouse.get_pos()
					row, col = Grid.get_clicked_pos(mouse_pos_pygame, rows, WIDTH)
					spot = grid[row][col]
					if not start_spot and spot != end_spot:
						start_spot = spot
						start_spot.make_start()

					elif not end_spot and spot != start_spot:
						end_spot = spot
						end_spot.make_end()
					
					elif spot != start_spot and spot != end_spot:
						spot.make_wall()

				elif pygame.mouse.get_pressed()[2]:
					mouse_pos_pygame = pygame.mouse.get_pos()
					row, col = Grid.get_clicked_pos(mouse_pos_pygame, rows, WIDTH)
					spot  = grid[row][col] 
					spot.reset()
					if spot != start_spot:
						start_spot = None
					elif spot != end_spot:
						end_spot = None


			elif (random_or_manual.lower() == 'ran' or random_or_manual.lower() == 'random') and not generated:
				start_spot, end_spot = Grid.maze_generation(grid, rows)
				generated = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start_spot and end_spot:
					for row in grid:
						for spot in row:
							spot.update_neigbours(grid)
					if algorithm_type.lower() == 'a':
						MazeSolver.a_star(lambda: Grid.draw(grid, rows, WIDTH), grid, start_spot, end_spot)
					elif algorithm_type.lower() == 'd':
						MazeSolver.dijkstra(lambda: Grid.draw(grid, rows, WIDTH), grid, start_spot, end_spot)

				if event.key == pygame.K_c:
					start_spot = None
					end_spot = None
					grid = Grid.make_grid(rows, WIDTH)
			
	pygame.quit()
