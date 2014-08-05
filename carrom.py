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
clock = pygame.time.Clock()
green = (102,205,0)

class Goti(pygame.sprite.Sprite):
	def __init__(self,color,radius,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([2*radius, 2*radius])
		self.image.fill(yellow)
		self.image.set_colorkey(yellow)
		self.rect = self.image.get_rect()
		self.rect.x = x-radius
		self.rect.y = y-radius
		pygame.draw.circle(self.image, color,(radius,radius),radius)
		pygame.draw.circle(self.image, black,(radius,radius),radius,2)

class Striker():
	def __init__(self,screen):
		self.striker_list = pygame.sprite.Group()
		self.striker = Goti(blue,28,495,880)
		self.striker_list.add(self.striker)
		self.screen = screen

	def update(self,state):
		pos = pygame.mouse.get_pos()
		if(state==0):
	 		if(pos[0]<168):
	 			self.striker.rect.centerx = 168
	 		elif(pos[0]>822):
	 			self.striker.rect.centerx = 822
	 		else:
	 			self.striker.rect.centerx = pos[0]
	 	self.striker_list.draw(self.screen)
			
	def directStriker(self):
		pos = pygame.mouse.get_pos()
		if(pos[1]>860):
			pygame.draw.lines(self.screen,green, False,[(self.striker.rect.centerx,self.striker.rect.centery),(pos[0],pos[1])],4)
		else:
			pygame.draw.lines(self.screen,red, False,[(self.striker.rect.centerx,self.striker.rect.centery),(pos[0],pos[1])],4)

class CarromBoard():
	def __init__(self, width=1000, height=1000, caption="Carrom Board"):
		pygame.init()
		self.width, self.height, self.caption = width, height, caption
		self.screen=pygame.display.set_mode((self.width, self.height))
	 	pygame.display.set_caption(self.caption)
	 	self.striker = Striker(self.screen)
		self.draw()

	def draw(self):
		self.screen.fill(yellow)
		#side border
		pygame.draw.rect(self.screen,wooden,(0,0,self.width,self.height),50)
		
		#up and down lines and circles
		pygame.draw.lines(self.screen, black, False, [(160,100),(830,100)],2)
		pygame.draw.lines(self.screen, black, False, [(160,140),(830,140)],2)
		pygame.draw.lines(self.screen, black, False, [(160,860),(830,860)],2)
		pygame.draw.lines(self.screen, black, False, [(160,900),(830,900)],2)
		pygame.draw.circle(self.screen, red, (160,120), 20)
		pygame.draw.circle(self.screen, black, (160,120), 20,2)
		pygame.draw.circle(self.screen, red, (160,880), 20)
		pygame.draw.circle(self.screen, black, (160,880), 20,2)
		pygame.draw.circle(self.screen, red, (830,120), 20)
		pygame.draw.circle(self.screen, black, (830,120), 20,2)
		pygame.draw.circle(self.screen, red, (830,880), 20)
		pygame.draw.circle(self.screen, black, (830,880), 20,2)		

		#left and right lines and circles
		pygame.draw.lines(self.screen, black, False, [(100,160),(100,830)],2)
		pygame.draw.lines(self.screen, black, False, [(140,160),(140,830)],2)
		pygame.draw.lines(self.screen, black, False, [(900,160),(900,830)],2)
		pygame.draw.lines(self.screen, black, False, [(860,160),(860,830)],2)
		pygame.draw.circle(self.screen, red, (120,160), 20)
		pygame.draw.circle(self.screen, black, (120,160), 20,2)
		pygame.draw.circle(self.screen, red, (120,830), 20)
		pygame.draw.circle(self.screen, black, (120,830), 20,2)
		pygame.draw.circle(self.screen, red, (880,160), 20)
		pygame.draw.circle(self.screen, black, (880,160), 20,2)
		pygame.draw.circle(self.screen, red, (880,830), 20)
		pygame.draw.circle(self.screen, black, (880,830), 20,2)
		
		#four holes position at the border
		pygame.draw.circle(self.screen, black, (47,47), 30)
		pygame.draw.circle(self.screen, black, (953,47), 30)
		pygame.draw.circle(self.screen, black, (47,953), 30)
		pygame.draw.circle(self.screen, black, (953,953), 30)

		
		goti_list=pygame.sprite.Group()
		goti_list.add(Goti(black,25,500,400))
		goti_list.add(Goti(black,25,585,450))
		goti_list.add(Goti(black,25,412,450))
		goti_list.add(Goti(black,25,457,475))
		goti_list.add(Goti(black,25,500,600))
		goti_list.add(Goti(black,25,500,550))
		goti_list.add(Goti(black,25,587,550))
		goti_list.add(Goti(black,25,414,552))
		goti_list.add(Goti(black,25,542,425))
		goti_list.add(Goti(yellow2,25,590,500))
		goti_list.add(Goti(yellow2,25,410,500))
		goti_list.add(Goti(yellow2,25,500,450))
		goti_list.add(Goti(yellow2,25,543,475))
		goti_list.add(Goti(yellow2,25,457,525))
		goti_list.add(Goti(yellow2,25,457,425))
		goti_list.add(Goti(yellow2,25,457,575))
		goti_list.add(Goti(yellow2,25,543,575))
		goti_list.add(Goti(yellow2,25,543,525))
		goti_list.add(Goti(pink,25,500,500))
		goti_list.draw(self.screen)
		

		
	def run(self):
		state = 0
		while True:
	 		for event in pygame.event.get():
	 			if event.type==QUIT:
	 				pygame.quit()
	 				sys.exit()
	 			elif event.type==MOUSEBUTTONDOWN and event.button == 1:
	 				if state==0:
	 					state=1
	 				elif state==1:
	 					state=2
	 			elif event.type==MOUSEBUTTONDOWN and event.button == 3:
	 				state=0


	 			self.striker.update(state)
	 			pygame.display.update()
	 		self.draw()
	 		if(state==1):
	 			self.striker.directStriker()
	 		clock.tick(20)
	 		#pygame.display.flip()


def main():
    game = CarromBoard()

    while game.run():
        pass

if __name__ == '__main__':
    main()
	

