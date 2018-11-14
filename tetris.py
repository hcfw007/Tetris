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

    font = pygame.font.SysFont('arail', 64)
    title_surface = font.render('TETRIS', True, (88, 87, 86))
    screen.blit(title_surface, (215, 50))
    
    board_rect = ((padding_left, padding_top), (width * block_length + border_width * 2, height * block_length + border_width * 2))
    grid_origin = ((padding_left + border_width), (padding_top + height * block_length + border_width))
    clock = pygame.time.Clock()
    time_elapsed = 0
    
    
    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                gameboard.current_tetrominoe.rotate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                gameboard.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                gameboard.move_right()
        
        time_elapsed += clock.tick(30)
        if time_elapsed > 70 * (11 - gameboard.speed):
            time_elapsed = 0
            gameboard.next_tick()
        screen.fill((0, 0, 0), board_rect)
        gameboard.draw(screen, grid_origin, block_length)
        pygame.display.flip()
 
     
if __name__=="__main__":
    main()