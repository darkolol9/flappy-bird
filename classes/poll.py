import pygame
poll_img = pygame.image.load('imgs/poll.png')

class Poll():
	#the poll class
	def __init__(self,width,height):
		self.img = poll_img
		self.rect = self.img.get_rect()
		self.rect.x = width+10
		self.rect.y = 0
		
	def move(self,speed):
		self.rect.x -= speed
	def blit(self,screen):
		screen.blit(self.img,(self.rect.x,self.rect.y))
		#print('poll:',self.rect)


