#!/usr/bin/python
 
import sys
import pygame
from carrom import * 
pygame.init()
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
yellow2 = (238,199,94)
 
class MenuItem(pygame.font.Font):
    def __init__(self, text, font="Arial", font_size=30,
                 font_color=WHITE, (pos_x, pos_y)=(0, 0)):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size

        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
 
class GameMenu():
    def __init__(self, screen, items, funcs, bg_color=BLACK, font=None, font_size=60,
                 font_color=WHITE):
        self.screen = screen

        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + (index * menu_item.height)
 
            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
 
        self.mouse_is_visible = True
        self.cur_item = None
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_keyboard_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(yellow2)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()
 
    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            item.set_font_color(yellow2)
            item.set_italic(True)
        else:
            item.set_font_color(WHITE)
            item.set_italic(False)
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
            
            mpos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            self.funcs[item.text]()
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
 
            # Redraw the background
            self.screen.fill(self.bg_color)
            myfont = pygame.font.SysFont("Comic Sans MS", 100)
            myfont1 = pygame.font.SysFont("Comic Sans MS", 50)
            myfont2 = pygame.font.SysFont("Comic Sans MS", 30)
            label = myfont.render("Carrom Board", 1, yellow2)
            ins = myfont1.render("Instructions", 1, yellow2)
            ins1 = myfont2.render("1. In order to direct the striker click on the striker a line would come to show direction.", 1, yellow2)
            ins2 = myfont2.render("2. In order to hit a peg from directed striker left click again striker would shoot.", 1, yellow2)
            ins3 = myfont2.render("3. In order to remove a striker from directed state right again you would be able to move striker and direct it", 1, yellow2)
            ins4 = myfont2.render("4. For covering every black peg player1 would get +10 points and for yellow opponent would get +10 points and vice versa.", 1, yellow2)
            ins5 = myfont2.render("5. For covering a queen, player would get +50 points", 1, yellow2)
            self.screen.blit(label, (500,100))
            self.screen.blit(ins, (50,550))
            self.screen.blit(ins1, (50,590))
            self.screen.blit(ins2, (50,630))
            self.screen.blit(ins3, (50,670))
            self.screen.blit(ins4, (50,710))
            self.screen.blit(ins5, (50,750))
 
            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)
 
            pygame.display.flip()
 
if __name__ == "__main__":
    def hello_world():
        main()
 
    # Creating the screen
    screen = pygame.display.set_mode((1500, 1000), 0, 32)
 
    menu_items = ('Start', 'Quit')
    funcs = {'Start': hello_world,
             'Quit': sys.exit}
 
    pygame.display.set_caption('Carrom Board')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()
