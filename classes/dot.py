import pygame
#the dot class, champ
dotImg = pygame.image.load('imgs/dot.png')

class Dot:
	#init
	def __init__(self,xloc,yloc):
		self.img = dotImg
		self.rect = self.img.get_rect()
		self.rect.x = xloc
		self.rect.y = yloc
		
		
	#blitting to screen
	def blit(self,screen):
		screen.blit(self.img,(self.rect.x,self.rect.y))
		#print('bird:',self.rect)





