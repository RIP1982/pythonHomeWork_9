from check_win import *
from game_play import *
from game_end import *

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (indent + size_block)
            row = y_mouse // (indent + size_block)
            if mas[row][column] == 0:
                if query % 2 == 0:
                    mas[row][column] = 'x'
                else:
                    mas[row][column] = 'o'
            query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        game_play(event, mas)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        game_end(game_over)
    pygame.display.update()

