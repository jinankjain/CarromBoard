import pygame, sys
from pygame.locals import *
import math

red=(255,0,0)
blue=(0,0,255)
wooden = (192, 64, 0)
yellow=(255,204,154)
black = (0,0,0)
pink = (242,4,105)
yellow2 = (238,199,94)

class CarromBoard():
	def __init__(self, width=1000, height=1000, caption="Carrom Board"):
		pygame.init()
		self.width, self.height, self.caption = width, height, caption
		self.screen=pygame.display.set_mode((self.width, self.height))
	 	pygame.display.set_caption(self.caption)
	 	self.screen.fill(yellow)
		self.draw()

	def draw(self):
		pygame.draw.rect(self.screen,wooden,(0,0,self.width,self.height),50)
		#pygame.draw.rect(self.screen,black,(0,0,20,20),50)
		pygame.draw.circle(self.screen, black, (47,47), 30)
		pygame.draw.circle(self.screen, black, (953,47), 30)
		pygame.draw.circle(self.screen, black, (47,953), 30)
		pygame.draw.circle(self.screen, black, (953,953), 30)
		pygame.draw.circle(self.screen, pink, (500,500), 25)
		pygame.draw.circle(self.screen, black, (500,550), 25)
		pygame.draw.circle(self.screen, yellow2, (543,525), 25)
		pygame.draw.circle(self.screen, black, (587,550), 25)
		pygame.draw.circle(self.screen, yellow2, (543,575), 25)
		pygame.draw.circle(self.screen, yellow2, (457,575), 25)
		pygame.draw.circle(self.screen, yellow2, (413,575), 25)
		pygame.draw.circle(self.screen, yellow2, (457,425), 25)
		pygame.draw.circle(self.screen, black, (500,600), 25)
		pygame.draw.circle(self.screen, yellow2, (457,525), 25)
		pygame.draw.circle(self.screen, black, (457,475), 25)
		pygame.draw.circle(self.screen, black, (543,475), 25)
		pygame.draw.circle(self.screen, yellow2, (500,450), 25)

	def run(self):
		while True:
	 		for event in pygame.event.get():
	 			if event.type==QUIT:
	 				pygame.quit()
	 				sys.exit()
	 		pygame.display.update()

def main():
    game = CarromBoard()
    while game.run():
        pass

if __name__ == '__main__':
    main()
	

