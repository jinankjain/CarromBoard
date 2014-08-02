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
		
		pygame.draw.lines(self.screen, black, False, [(160,100),(830,100)],2)
		pygame.draw.lines(self.screen, black, False, [(160,140),(830,140)],2)
		pygame.draw.lines(self.screen, black, False, [(160,860),(830,860)],2)
		pygame.draw.lines(self.screen, black, False, [(160,900),(830,900)],2)
		pygame.draw.circle(self.screen, black, (160,120), 20)
		pygame.draw.circle(self.screen, black, (160,880), 20)
		pygame.draw.circle(self.screen, black, (830,120), 20)
		pygame.draw.circle(self.screen, black, (830,880), 20)


		pygame.draw.lines(self.screen, black, False, [(100,160),(100,830)],2)
		pygame.draw.lines(self.screen, black, False, [(140,160),(140,830)],2)
		pygame.draw.lines(self.screen, black, False, [(900,160),(900,830)],2)
		pygame.draw.lines(self.screen, black, False, [(860,160),(860,830)],2)
		pygame.draw.circle(self.screen, black, (120,160), 20)
		pygame.draw.circle(self.screen, black, (120,830), 20)
		pygame.draw.circle(self.screen, black, (880,160), 20)
		pygame.draw.circle(self.screen, black, (880,830), 20)
		
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
		pygame.draw.circle(self.screen, black, (414,552), 25)
		pygame.draw.circle(self.screen, yellow2, (457,425), 25)
		pygame.draw.circle(self.screen, black, (500,600), 25)
		pygame.draw.circle(self.screen, yellow2, (457,525), 25)
		pygame.draw.circle(self.screen, black, (457,475), 25)
		pygame.draw.circle(self.screen, black, (543,475), 25)
		pygame.draw.circle(self.screen, yellow2, (500,450), 25)
		pygame.draw.circle(self.screen, yellow2, (410,500), 25)
		pygame.draw.circle(self.screen, yellow2, (590,500), 25)
		pygame.draw.circle(self.screen, black, (412,450), 25)
		pygame.draw.circle(self.screen, black, (585,450), 25)
		pygame.draw.circle(self.screen, yellow2, (542,425), 25)
		pygame.draw.circle(self.screen, black, (500,400), 25)

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
	

