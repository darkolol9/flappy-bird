import pygame
from functions import poll_generator


#rules and logic of the game

def logic(dot_spite,width,height,game_running,polls,speed):
	if (dot_spite.rect.x >= width or dot_spite.rect.x <= 0 or dot_spite.rect.y >= height or dot_spite.rect.y <= 0):
		game_running = False
		exit()
	if (polls[0].rect.x <=0 ):
		poll_generator.generate_set_of_polls(polls,width,height)
		speed += 1
def check_collision(polls,dot):

	if(dot.rect.colliderect(polls[1].rect)):
		print("collided")
		exit()
