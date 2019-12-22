import pygame
from functions import poll_generator
from time import sleep

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
#rules and logic of the game

def logic(dot_spite,width,height,game_running,polls,speed):
	if (dot_spite.rect.x >= width or dot_spite.rect.x <= 0 or dot_spite.rect.y >= height or dot_spite.rect.y <= 0):
		game_running = False
		sleep(2)
		exit()
	if (polls[0].rect.x <=0 ):
		poll_generator.generate_set_of_polls(polls,width,height)
		speed += 1
def check_collision(polls,dot,w,h,screen):

	if(dot.rect.colliderect(polls[1].rect)):
		print("collided")
		sleep(2)
		exit()

		
def check_for_score(score_,poll):
	if (poll.rect.x <=0 ):
		score_ += 10
		return score_
	else:
		return score_
		
