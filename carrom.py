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
friction = 0.1
wid = 1000
strikerrad = 28
gotirad = 25
border = 50


mod = lambda v: math.sqrt(v[0] * v[0] + v[1] * v[1])

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

	def __init__(self,screen):
		self.striker_list = pygame.sprite.Group()
		self.striker = Goti(blue,28,495,880)
		self.striker_list.add(self.striker)
		self.player=1
		#self.rect.centerx = self.striker.rect.centerx
		#self.rect.centery = self.striker.rect.centery 
		self.screen = screen
		self.vely = 5
	 	self.velx = 15
	 	self.state=0

	def update(self):
		#print self.state
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
	 			#self.striker.state=0
	 			
	 		else:
	 			self.velx = self.velx - friction * self.velx / mod([self.velx, self.vely])
	 			self.vely = self.vely - friction * self.vely / mod([self.velx, self.vely])
	 			if abs(self.velx)<friction:
	 				self.velx=0
	 			if abs(self.vely)<friction:
	 				self.vely=0	
	 	self.striker_list.draw(self.screen)
			
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
	#print ball1.rect.centerx

	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.rect.centerx, ball2.rect.centery]
	temp = [(c1[0]-c2[0]),(c1[1]-c2[1])]
	
	dist = (50 - mod(temp))/2+3
	normal = [(c1[0]-c2[0])/mod(temp),(c1[1]-c2[1])/mod(temp)]
	tangent = [-normal[1],normal[0]]
	dist_normal = [dist*normal[0], dist*normal[1]]
	#dist_tangent = [dist*tangent[0], dist*tangent[1]]
	ball1.rect.centerx+=dist_normal[0]
	ball1.rect.centery+=dist_normal[1]
	ball2.rect.centerx-=dist_normal[0]
	ball2.rect.centery-dist_normal[1]
	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.rect.centerx, ball2.rect.centery]
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
    if distance<80:
        return True
    return False

def collideStriker(ball1,ball2):
	#print ball1.rect.centerx
	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.striker.rect.centerx, ball2.striker.rect.centery]
	temp = [(c1[0]-c2[0]),(c1[1]-c2[1])]
	dist = (50 - mod(temp))/2+3
	normal = [(c1[0]-c2[0])/mod(temp),(c1[1]-c2[1])/mod(temp)]
	dist_normal = [dist*normal[0], dist*normal[1]]
	ball1.rect.centerx+=dist_normal[0]
	ball1.rect.centery+=dist_normal[1]
	ball2.striker.rect.centerx-=dist_normal[0]
	ball2.striker.rect.centery-dist_normal[1]
	c1 = [ball1.rect.centerx, ball1.rect.centery]
	c2 = [ball2.striker.rect.centerx, ball2.striker.rect.centery]
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

class CarromBoard():
	def __init__(self, width=1000, height=1000, caption="Carrom Board"):
		pygame.init()
		self.width, self.height, self.caption = width, height, caption
		self.screen=pygame.display.set_mode((self.width, self.height))
	 	pygame.display.set_caption(self.caption)
	 	self.striker = Striker(self.screen)
	 	self.goti_list=pygame.sprite.Group()
		self.goti_list.add(Goti(black,25,500,400))
		self.goti_list.add(Goti(black,25,585,450))
		self.goti_list.add(Goti(black,25,412,450))
		self.goti_list.add(Goti(black,25,457,475))
		self.goti_list.add(Goti(black,25,500,600))
		self.goti_list.add(Goti(black,25,500,550))
		self.goti_list.add(Goti(black,25,587,550))
		self.goti_list.add(Goti(black,25,414,552))
		self.goti_list.add(Goti(black,25,542,425))
		self.goti_list.add(Goti(yellow2,25,590,500))
		self.goti_list.add(Goti(yellow2,25,410,500))
		self.goti_list.add(Goti(yellow2,25,500,450))
		self.goti_list.add(Goti(yellow2,25,543,475))
		self.goti_list.add(Goti(yellow2,25,457,525))
		self.goti_list.add(Goti(yellow2,25,457,425))
		self.goti_list.add(Goti(yellow2,25,457,575))
		self.goti_list.add(Goti(yellow2,25,543,575))
		self.goti_list.add(Goti(yellow2,25,543,525))
		self.goti_list.add(Goti(pink,25,500,500))
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
	 					goti1.collided, goti2.collided = True, True

	 		for goti in self.goti_list:
	 			goti.collided = False
	 			if inPocket(goti):
	 				self.goti_list.remove(goti)
	 			goti.update()

	 		if self.striker.state==2:
	 			for goti in self.goti_list:
	 				if pygame.sprite.collide_circle(goti, self.striker.striker):
	 					collideStriker(goti,self.striker)
	 		stopped = True
	 		for goti in self.goti_list:
	 			if goti.velx!=0 or goti.vely!=0 or self.striker.velx!=0 or self.striker.vely!=0:
	 				stopped = False
	 				break
	 		
	 		if stopped and self.striker.state==2:
	 			self.striker.state = 0
	 			if(self.striker.player==1):
	 				self.striker.player = 2
	 				self.striker.striker.rect.centery = 120
	 			else:
	 				self.striker.player = 1
	 				self.striker.striker.rect.centery = 880

	 			print self.striker.state

	 		clock.tick(50)
	 		#pygame.display.flip()


def main():
    game = CarromBoard()

    while game.run():
        pass

if __name__ == '__main__':
    main()