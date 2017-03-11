import pygame
import sys
from waves import Wave

# def handle_events(events):
#     for event in events:
#         if event.type == pygame.QUIT:
#             print("Closing the simulation..")
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 print("Closing the simulation..")
#                 sys.exit()
#         if event.type == pygame.USEREVENT:



if __name__ == '__main__':    

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    clock.tick(40)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    w = Wave(screen, 320, 240)

    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing the simulation..")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Closing the simulation..")
                    sys.exit()
            if event.type == pygame.USEREVENT:
                w.create_particles()
        # handle_events(pygame.event.get())
        # print(pygame.time.get_ticks())
        # pygame.time.get_ticks()//1000
        w.update()
        w.draw()
        # pygame.time.wait(100)
        pygame.display.update()
