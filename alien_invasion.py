import sys
import pygame

class AlienInvasion:
    "a class to manage game assests"
    def __init__(self):
        
        pygame.init()

        self.screen = pygame.display.set_mode((1550,800))
        pygame.display.set_caption("Alien invasion my first game")
    
    def run_game(self):

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
        