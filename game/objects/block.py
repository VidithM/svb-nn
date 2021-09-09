import pygame

class Block:
    def __init__(self, val, pos, font, window):
        self.val = val 
        self.getColor()
        self.pos = pos 
        self.w = 100
        self.h = 100
        self.window = window
        self.font = font
    
    def render(self):
        pygame.draw.rect(self.window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.w, self.h))
        img = self.font.render(str(self.val), True, (255, 255, 255))
        self.window.blit(img, (self.pos[0] + 27, self.pos[1] + 25))
        
    def move_down(self, amt):
        self.pos[1] += amt 
    
    def weaken():
        self.val -= 1
        self.getColor()
    
    def getColor(self):
        if(self.val >= 50):
            self.color = (255, 255 - (255 * (self.val - 50) / 50), 0)
        else:
            self.color = (255 * (self.val / 50), 255, 0)

