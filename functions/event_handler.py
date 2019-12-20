import pygame


#handle all keys
def handle(event,x_change,y_change,game_is_running):

	if event.type == pygame.QUIT:
		game_is_running = False
		exit()
		x_change = 0

	if event.type == pygame.KEYUP:
		x_change = 0
		y_change = 3


	elif event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_change = -5
		elif event.key == pygame.K_RIGHT:
			x_change = 5
		elif event.key == pygame.K_UP:
			y_change = -2
		elif event.key == pygame.K_DOWN:
			y_change = 4

	return (x_change,y_change)


