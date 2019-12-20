from classes import poll
import random

def generate_set_of_polls(polls,width,height):


	polls[0].rect.x = width +10
	polls[1].rect.x = width+10


	polls[0].rect.y = random.randint(-551,0)
	polls[1].rect.y = (polls[0].rect.y+551) + random.randint(100,120)

	



