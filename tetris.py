import pygame
from gameboard import GameBoard

def main():
     
    pygame.init()
    pygame.display.set_caption("Tetris")
    
    screen = pygame.display.set_mode((400,600), 0, 32)
    screen.fill((255, 255, 255))

    block_length = 20
    height = 25 # min 20
    width = 8 # min 8
    padding_left = 20
    padding_top = 20
    border_width = 5
    
    gameboard = GameBoard(width, height)
    
    board_rect = ((padding_left, padding_top), (width * block_length + border_width * 2, height * block_length + border_width * 2))
    grid_origin = ((padding_left + border_width), (padding_top + height * block_length + border_width))
    screen.fill((0, 0, 0), board_rect)
    gameboard.draw_blocks(screen, grid_origin, block_length)
    pygame.display.flip()
    
    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

 
     
if __name__=="__main__":
    main()