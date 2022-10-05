import pygame
pygame.init()

size_block = 100
indent = 15
width = heigth = size_block * 3 + indent * 4
size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('tic-tac-toe')

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False