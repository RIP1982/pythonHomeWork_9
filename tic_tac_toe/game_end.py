from data import *

def game_end(game_over):
    screen.fill(black)
    font = pygame.font.SysFont('arial', 80)
    text1 = font.render(game_over, True, white)
    text_rect = text1.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])