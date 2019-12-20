#imports
import pygame
from classes import poll
from functions import logic
from classes import dot
from functions import event_handler
#end of imports

#pygame game template:
bg_img = pygame.image.load('imgs/bg.png')

pygame.init()

#load logo img
logo = pygame.image.load('imgs/logo.png')
pygame.display.set_icon(logo)

pygame.display.set_caption('flapy bird')

#control screen properties/create a canvas
height = 700
width = 1000
screen = pygame.display.set_mode((width,height))

#variable to control game loop
game_is_running = True

#create polls
pol1 = poll.Poll(width,height)
pol2 = poll.Poll(width,height)
polls = [pol1,pol2]

#create dot
dot_spite =dot.Dot(height*0.48,width*0.48) 
x_change = 0
y_change = 3
gravity = 0
speed = 1
clock = pygame.time.Clock()
white = (0,100,255)

while game_is_running:
	screen.blit(bg_img,[0,0])
	#handle events
	logic.check_collision(polls,dot_spite)
	#print('change: ',x_change)
	for event in pygame.event.get():
		#handle the quitting event
		(x_change,y_change)=event_handler.handle(event,x_change,y_change,game_is_running)
	

	dot_spite.rect.x += x_change
	dot_spite.rect.y += y_change

	for poll in polls:
		poll.move(speed)

	#print('moving...')
	logic.logic(dot_spite,width,height,game_is_running,polls,speed)
	
	dot_spite.blit(screen)

	for poll in polls:
		poll.blit(screen)

	#update screen (frame)
	pygame.display.update()
	clock.tick(60)


