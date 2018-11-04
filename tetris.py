import pygame
from gameboard import GameBoard

def main():
     
    pygame.init()
    pygame.display.set_caption("Tetris")
    
    screen = pygame.display.set_mode((400,600), 0, 32)
    screen.fill((255, 255, 255))

    block_length = 20
    height = 25
    width = 8
    
    gameboard = GameBoard(width, height)
    
    board_rect = ((20, 20), (20 + width * block_length + 10, 20 + height * block_length + 10))
    screen.fill((0, 0, 0), board_rect)
    pygame.display.flip()
    
    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

 
     
if __name__=="__main__":
    main()