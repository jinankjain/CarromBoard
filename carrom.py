# Author Jinank Jain
# Developed using PyGame Library

import pygame, sys
from pygame.locals import *
import math
import tkMessageBox


red=(255,0,0)
blue=(0,0,255)
wooden = (192, 64, 0)
yellow=(255,204,154)
black = (0,0,0)
pink = (242,4,105)
yellow2 = (238,199,94)
clock = pygame.time.Clock()
green = (102,205,0)
friction = 0.1
wid = 1000
strikerrad = 28
gotirad = 25
border = 50
pi=3.14
#for converting to radian
rad=pi/180


mod = lambda v: math.sqrt(v[0] * v[0] + v[1] * v[1])

class Goti(pygame.sprite.Sprite):
	def __init__(self,color,radius,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([2*radius, 2*radius])
		self.image.fill(yellow)
		self.color = color
		self.image.set_colorkey(yellow)
		self.rect = self.image.get_rect()
		self.rect.x = x-radius
		self.rect.y = y-radius
		pygame.draw.circle(self.image, color,(radius,radius),radius)
		pygame.draw.circle(self.image, black,(radius,radius),radius,2)
		self.velx=0
		self.vely=0
		self.collided = False

	def update(self):
		self.rect.centerx+=self.velx
	 	self.rect.centery+=self.vely
	 	if self.rect.y > wid-border/2- 2*gotirad:
	 		self.rect.y = wid - border/2-2*gotirad- 1
	 		self.vely = -1*abs(self.vely)
	 	elif (self.rect.y<border/2):
	 		self.rect.y = border/2 + 1
	 		self.vely = abs(self.vely)

	 	if self.rect.x > wid-border/2-2*gotirad:
	 		self.rect.x = wid - border/2 -2*gotirad- 1
	 		self.velx = -1*abs(self.velx)
	 	elif self.rect.x<border/2:
	 		self.rect.x = border/2 + 1
	 		self.velx = abs(self.velx)

	 	if mod([self.velx, self.vely])==0:
	 		self.velx=0
	 		self.vely=0
	 	else:
	 		self.velx = self.velx - friction * self.velx / mod([self.velx, self.vely])
	 		self.vely = self.vely - friction * self.vely / mod([self.velx, self.vely])
	 		if abs(self.velx)<friction:
	 			self.velx=0
	 		if abs(self.vely)<friction:
	 			self.vely=0	

class Striker():

	def __init__(self,screen,goti_list):
		self.striker_list = pygame.sprite.Group()
		self.striker = Goti(blue,28,495,880)
		self.striker_list.add(self.striker)
		self.player=1
		self.screen = screen
		self.vely = 0
	 	self.velx = 0
	 	self.state=0
	 	self.goti_list = goti_list

	def update(self):
		pos = pygame.mouse.get_pos()
		if(self.state==0):
	 		if(pos[0]<168):
	 			self.striker.rect.centerx = 168
	 		elif(pos[0]>822):
	 			self.striker.rect.centerx = 822
	 		else:
	 			self.striker.rect.centerx = pos[0]
	 	elif(self.state==2):
	 		self.striker.rect.centerx+=self.velx
	 		self.striker.rect.centery+=self.vely
	 		if self.striker.rect.y > wid-border/2- 2*strikerrad:
	 			self.striker.rect.y = wid - border/2-2*strikerrad- 1
	 			self.vely = -1*abs(self.vely)
	 		elif (self.striker.rect.y<border/2):
	 			self.striker.rect.y = border/2 + 1
	 			self.vely = abs(self.vely)

	 		if self.striker.rect.x > wid-border/2-2*strikerrad:
	 			self.striker.rect.x = wid - border/2 -2*strikerrad- 1
	 			self.velx = -1*abs(self.velx)
	 		elif self.striker.rect.x<border/2:
	 			self.striker.rect.x = border/2 + 1
	 			self.velx = abs(self.velx)

	 		if mod([self.velx, self.vely])==0:
	 			self.velx=0
	 			self.vely=0
	 			
	 		else:
	 			self.velx = self.velx - friction * self.velx / mod([self.velx, self.vely])
	 			self.vely = self.vely - friction * self.vely / mod([self.velx, self.vely])
	 			if abs(self.velx)<friction:
	 				self.velx=0
	 			if abs(self.vely)<friction:
	 				self.vely=0	
	 	
			
	def directStriker(self):
		pos = pygame.mouse.get_pos()
		if(pos[1]>860 and self.player==1):
			pygame.draw.lines(self.screen,green, False,[(self.striker.rect.centerx,self.striker.rect.centery),(pos[0],pos[1])],4)
		elif(pos[1]<=860 and self.player==1):
			pygame.draw.lines(self.screen,red, False,[(self.striker.rect.centerx,self.striker.rect.centery),(pos[0],pos[1])],4)
		elif(pos[1]<100):
			pygame.draw.lines(self.screen,green, False,[(self.striker.rect.centerx,self.striker.rect.centery),(pos[0],pos[1])],4)
		elif(pos[1]>=100):
			pygame.draw.lines(self.screen,red, False,[(self.striker.rect.centerx,self.striker.rect.centery),(pos[0],pos[1])],4)

def collideBalls(ball1,ball2):

	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.rect.centerx, ball2.rect.centery]
	temp = [(c1[0]-c2[0]),(c1[1]-c2[1])]
	
	dist = (46 - mod(temp))/2+3
	normal = [(c1[0]-c2[0])/mod(temp),(c1[1]-c2[1])/mod(temp)]
	tangent = [-normal[1],normal[0]]
	dist_normal = [dist*normal[0], dist*normal[1]]
	ball1.rect.centerx+=dist_normal[0]
	ball1.rect.centery+=dist_normal[1]
	ball2.rect.centerx-=dist_normal[0]
	ball2.rect.centery-dist_normal[1]
	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.rect.centerx, ball2.rect.centery]
	temp = [(c1[0]-c2[0]),(c1[1]-c2[1])]
	normal = [(c1[0]-c2[0])/mod(temp),(c1[1]-c2[1])/mod(temp)]
	tangent = [-normal[1],normal[0]]
	ball1vel = [ball1.velx,ball1.vely]
	ball2vel = [ball2.velx,ball2.vely]
	ball1vel_normal = normal[0]*ball1vel[0]+normal[1]*ball1vel[1]
	ball1vel_tangent = tangent[0]*ball1vel[0]+tangent[1]*ball1vel[1]
	ball2vel_normal = normal[0]*ball2vel[0]+normal[1]*ball2vel[1]
	ball2vel_tangent = tangent[0]*ball2vel[0]+tangent[1]*ball2vel[1]
	ball2vel_normal, ball1vel_normal = ball1vel_normal, ball2vel_normal
	normal1 = [ball1vel_normal*normal[0],ball1vel_normal*normal[1]] 
	normal2 = [ball2vel_normal*normal[0],ball2vel_normal*normal[1]]
	tangent1 = [ball1vel_tangent*tangent[0],ball1vel_tangent*tangent[1]] 
	tangent2 = [ball2vel_tangent*tangent[0],ball2vel_tangent*tangent[1]]
	ball1.velx = normal1[0]+tangent1[0]
	ball1.vely = normal1[1]+tangent1[1]
	ball2.velx = normal2[0]+tangent2[0]
	ball2.vely = normal2[1]+tangent2[1]
	#print ball2vel

def inPocket(disk):
    distance = min(mod([disk.rect.x-2*border/3, disk.rect.y-2*border/3]),
                mod([disk.rect.x-2*border/3, disk.rect.y-wid+2*border/3]),
                mod([disk.rect.x-wid+2*border/3, disk.rect.y-2*border/3]),
                mod([disk.rect.x-wid+2*border/3, disk.rect.y-wid+2*border/3]))
    if distance<60:
        return True
    return False

def collideStriker(ball1,ball2):
	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.striker.rect.centerx, ball2.striker.rect.centery]
	temp = [(c1[0]-c2[0]),(c1[1]-c2[1])]
	dist = (51 - mod(temp))/2+3
	normal = [(c1[0]-c2[0])/mod(temp),(c1[1]-c2[1])/mod(temp)]
	dist_normal = [dist*normal[0], dist*normal[1]]
	ball1.rect.centerx+=dist_normal[0]
	ball1.rect.centery+=dist_normal[1]
	ball2.striker.rect.centerx-=dist_normal[0]
	ball2.striker.rect.centery-dist_normal[1]
	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.striker.rect.centerx, ball2.striker.rect.centery]
	temp = [(c1[0]-c2[0]),(c1[1]-c2[1])]
	normal = [(c1[0]-c2[0])/mod(temp),(c1[1]-c2[1])/mod(temp)]
	tangent = [-normal[1],normal[0]]
	ball1vel = [ball1.velx,ball1.vely]
	ball2vel = [ball2.velx,ball2.vely]
	ball1vel_normal = normal[0]*ball1vel[0]+normal[1]*ball1vel[1]
	ball1vel_tangent = tangent[0]*ball1vel[0]+tangent[1]*ball1vel[1]
	ball2vel_normal = normal[0]*ball2vel[0]+normal[1]*ball2vel[1]
	ball2vel_tangent = tangent[0]*ball2vel[0]+tangent[1]*ball2vel[1]
	ball2vel_normal, ball1vel_normal = ball1vel_normal, ball2vel_normal
	normal1 = [ball1vel_normal*normal[0],ball1vel_normal*normal[1]] 
	normal2 = [ball2vel_normal*normal[0],ball2vel_normal*normal[1]]
	tangent1 = [ball1vel_tangent*tangent[0],ball1vel_tangent*tangent[1]] 
	tangent2 = [ball2vel_tangent*tangent[0],ball2vel_tangent*tangent[1]]
	ball1.velx = normal1[0]+tangent1[0]
	ball1.vely = normal1[1]+tangent1[1]
	ball2.velx = normal2[0]+tangent2[0]
	ball2.vely = normal2[1]+tangent2[1]

class CarromBoard():
	def __init__(self, width=1500, height=1000, caption="Carrom Board"):
		pygame.init()
		self.sound = pygame.mixer.Sound("gotoholes.ogg")
		self.collide_sound = pygame.mixer.Sound("collide.ogg")
		self.width, self.height, self.caption = width, height, caption
		self.screen=pygame.display.set_mode((self.width, self.height))
	 	pygame.display.set_caption(self.caption)
	 	
	 	self.change = True
	 	self.striker_foul = False
	 	self.count=0
	 	self.pocketed=0
	 	self.game_over = False

	 	self.goti_list=pygame.sprite.Group()
		self.goti_list.add(Goti(black,23,500,400))
		self.goti_list.add(Goti(black,23,585,450))
		self.goti_list.add(Goti(black,23,412,450))
		self.goti_list.add(Goti(black,23,457,475))
		self.goti_list.add(Goti(black,23,500,600))
		self.goti_list.add(Goti(black,23,500,550))
		self.goti_list.add(Goti(black,23,587,550))
		self.goti_list.add(Goti(black,23,414,552))
		self.goti_list.add(Goti(black,23,542,425))
		self.goti_list.add(Goti(yellow2,23,590,500))
		self.goti_list.add(Goti(yellow2,23,410,500))
		self.goti_list.add(Goti(yellow2,23,500,450))
		self.goti_list.add(Goti(yellow2,23,543,475))
		self.goti_list.add(Goti(yellow2,23,457,525))
		self.goti_list.add(Goti(yellow2,23,457,425))
		self.goti_list.add(Goti(yellow2,23,457,575))
		self.goti_list.add(Goti(yellow2,23,543,575))
		self.goti_list.add(Goti(yellow2,23,543,525))
		self.goti_list.add(Goti(pink,23,500,500))
		self.striker = Striker(self.screen,self.goti_list)
		self.score = [0,0]
		self.draw()

	
	def draw(self):
		self.screen.fill(yellow)
		#side border
		pygame.draw.rect(self.screen,wooden,(0,0,self.width-500,self.height),50)
		
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

		vel1=0
		vel2=0
		vel = [self.striker.velx, self.striker.vely]
		if(self.striker.player==1):
			vel1 = mod(vel)
			vel2 = 0
		else:
			vel2 = mod(vel)
			vel1 = 0


		#Developers Note
		myfont = pygame.font.SysFont("Comic Sans MS", 50)
		myfont1 = pygame.font.SysFont("Comic Sans MS", 25)
		myfont2 = pygame.font.SysFont("Comic Sans MS", 30)
		label = myfont.render("Scoring", 1, black)
		player1 = myfont.render("Player 1: "+str(self.score[0]), 1, black)
		player2 = myfont.render("Player 2: "+str(self.score[1]), 1, black)
		vital_stats = myfont2.render("Some Vital Stats about the moves", 1, black)
		vel_play1 = myfont2.render("Player1 Strike Velocity: "+str(vel1), 1, black)
		vel_play2 = myfont2.render("Player2 Strike Velocity: "+str(vel2), 1, black)
		dev1 = myfont1.render("This game was developed as course project for", 1, black)
		dev2 = myfont1.render("Software Engineering under Dr. Gaurav Harit", 1, black)
		self.screen.blit(label, (1200, 100))
		self.screen.blit(vital_stats, (1100, 400))
		self.screen.blit(vel_play1, (1100, 450))
		self.screen.blit(vel_play2, (1100, 500))
		self.screen.blit(player1, (1100,190))
		self.screen.blit(player2, (1100,250))
		self.screen.blit(dev1, (1070,900))
		self.screen.blit(dev2, (1080,930))

		#game_over
		if(self.game_over):
			gameOver = myfont.render("Game Over", 1, black)
			self.screen.blit(gameOver, (1175, 600))
			if(self.score[0]>self.score[1]):
				winner = myfont.render("Player 1 wins", 1, black)
				self.screen.blit(winner, (1160, 650))
			elif(self.score[0]<self.score[1]):
				winner = myfont.render("Player 2 wins", 1, black)
				self.screen.blit(winner, (1175, 700))

		#four arrows
		pygame.draw.lines(self.screen, black, False, [(120,120),(270,270)],3)
		pygame.draw.lines(self.screen, black, False, [(870,120),(720,270)],3)
		pygame.draw.lines(self.screen, black, False, [(120,870),(270,720)],3)
		pygame.draw.lines(self.screen, black, False, [(870,870),(720,720)],3)

		#four arcs of arrows
		# pygame.draw.arc(self.screen, black, Rect, math.pi/2, math.3pi/4, width=1)
		pygame.draw.arc(self.screen,black,(185,185,100,100),-180*rad,90*rad,2)
		pygame.draw.arc(self.screen,black,(700,185,100,100), 90*rad,360*rad,2)
		pygame.draw.arc(self.screen,black,(190,700,100,100), -90*rad,180*rad,2)
		pygame.draw.arc(self.screen,black,(700,700,100,100),0,270*rad,2)

		
		
		self.goti_list.draw(self.screen)
		

		
	def run(self):
		state = 0
		while True:
	 		for event in pygame.event.get():
	 			if event.type==QUIT:
	 				pygame.quit()
	 				sys.exit()
	 			elif event.type==MOUSEBUTTONDOWN and event.button == 1:
	 				if self.striker.state==0:
	 					self.striker.state=1
	 					for goti in self.goti_list:
	 						if pygame.sprite.collide_circle(goti, self.striker.striker):
	 							self.striker.state=0
	 							tkMessageBox.showinfo(title="Alert", message="Invalid Position to move")
	 				elif self.striker.state==1:
	 					self.striker.state=2
	 					pos = pygame.mouse.get_pos()
	 					self.striker.velx = (self.striker.striker.rect.centerx-pos[0])/5
	 					self.striker.vely = (self.striker.striker.rect.centery-pos[1])/5
	 			elif event.type==MOUSEBUTTONDOWN and event.button == 3:
	 				self.striker.state=0

	 		self.striker.update()

	 		pygame.display.update()
	 		self.draw()
	 		if(self.striker.state==1):
	 			self.striker.directStriker()

	 		for goti1 in self.goti_list:
	 			for goti2 in self.goti_list:
	 				if goti1 is not goti2 and pygame.sprite.collide_circle(goti1, goti2) and not goti1.collided and not goti2.collided:
	 					collideBalls(goti1, goti2)
	 					self.collide_sound.play()
	 					goti1.collided, goti2.collided = True, True

	 		for goti in self.goti_list:
	 			goti.collided = False
	 			if inPocket(goti):
	 				self.pocketed=1
	 				if(self.change):
	 					self.change = False
	 				self.sound.play()
	 				if(goti.color==black):
	 					self.score[0]+=10
	 				elif(goti.color==yellow2):
	 					self.score[1]+=10
	 				self.goti_list.remove(goti)
	 				if(goti.color==pink):
	 					self.count=1
	 				elif(self.count==1 and not self.change):
	 					if(goti.color==black):
	 						self.score[0]+=50
	 						self.count=0
	 					elif(goti.color==yellow2):
	 						self.score[1]+=50
	 						self.count=0
	 			goti.update()



	 		if self.striker.state==2:
	 			for goti in self.goti_list:
	 				if pygame.sprite.collide_circle(goti, self.striker.striker):
	 					self.collide_sound.play()
	 					collideStriker(goti,self.striker)
	 		stopped = True
	 		for goti in self.goti_list:
	 			if goti.velx!=0 or goti.vely!=0 or self.striker.velx!=0 or self.striker.vely!=0:
	 				stopped = False
	 				break
	 		
	 		if stopped and self.striker.state==2:
	 			self.striker_foul = False
	 			self.striker.state = 0
	 			if(self.count==1 and self.pocketed==0):
	 				self.goti_list.add(Goti(pink,25,500,500))
	 				self.count=0
	 			self.pocketed=0
	 			if(self.striker.player==1 and self.change):
	 				self.striker.player = 2
	 				self.striker.striker.rect.centery = 120
	 			elif(self.striker.player==2 and self.change):
	 				self.striker.player = 1
	 				self.striker.striker.rect.centery = 880
	 			elif(self.striker.player==1 and not self.change):
	 				self.striker.player = 1
	 				self.striker.striker.rect.centery = 880
	 				self.change = True
	 			else:
	 				self.striker.player = 2
	 				self.striker.striker.rect.centery = 120
	 				self.change = True

	 		if(inPocket(self.striker.striker)):
	 			if(self.striker.player==1 and self.score[0]>0 and not self.striker_foul):
	 				self.goti_list.add(Goti(black,25,500,400))
	 				self.score[0]-=10
	 				self.striker.velx = 0
	 				self.striker.vely = 0
	 				self.striker_foul = True

	 			elif(self.striker.player==2 and self.score[1]>0 and not self.striker_foul):
	 				self.goti_list.add(Goti(yellow2,25,500,400))
	 				self.score[1]-=10
	 				self.striker.velx = 0
	 				self.striker.vely = 0
	 				self.striker_foul = True

	 		if(not self.striker_foul):
	 			self.striker.striker_list.draw(self.screen)

	 		if(not self.goti_list):
	 			self.striker.velx = 0
	 			self.striker.vely = 0
	 			self.game_over = True


	 		clock.tick(50)
	 		#pygame.display.flip()


def main():
    game = CarromBoard()

    while game.run():
        pass

if __name__ == '__main__':
    main()
