import pygame


white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

class Score():
	def __init__(self,w,h):
		self.score = 0
		self.font = pygame.font.Font('freesansbold.ttf', 24)
		self.text = self.font.render('0',True,green,blue)
		self.rect = self.text.get_rect()
		self.rect.center = (w*0.1,h*0.1)

	def update(self,score,screen):
		self.text = self.font.render(score,True,green,blue)
		screen.blit(self.text,self.rect)

