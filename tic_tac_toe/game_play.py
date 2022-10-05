from data import *

def game_play(event, mas):
    for row in range(3):
        for column in range(3):
            if mas[row][column] == 'x':
                color = red
            elif mas[row][column] == 'o':
                color = green
            else:
                color = white
            x = column * size_block + (column + 1) * indent
            y = row * size_block + (row + 1) * indent
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == red:
                pygame.draw.line(screen, black, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 4)
                pygame.draw.line(screen, black, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 4)
            elif color == green:
                pygame.draw.circle(screen, black, (x + size_block / 2, y + size_block / 2), (size_block / 2 - 5), 4)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_over = False
                mas = [[0] * 3 for i in range(3)]
                query = 0
                screen.fill(black)

