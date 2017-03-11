import math
import pygame


class Particle:
    def __init__(self, screen, x, y, speed, acc=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 3
        self.speed = speed
        self.acc = acc
        self.window = self.screen.get_bounding_rect()

    def update(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.off_screen()

    def draw(self):
        # print("Drawing Particle")
        pygame.draw.circle(self.screen, (0,0,0),
            (int(self.x), int(self.y)), self.r
        )
        
    def off_screen(self):

        print(self.window.width, self.window.height)
        if self.x + self.r < 0 or self.x + self.r > self.window.width:
            self.speed = [-self.speed[0], self.speed[1]]
        if self.y + self.r < 0 or self.y + self.r > self.window.height:
            self.speed = [self.speed[0], -self.speed[1]]