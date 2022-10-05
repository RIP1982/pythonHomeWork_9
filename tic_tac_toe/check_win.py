
def check_win(mas, sign):
    empty_cells = 0
    for row in mas:
        empty_cells += row.count(0)
        if row.count(sign) == 3:
            return sign
    for column in range(3):
        if mas[0][column] == sign and mas[1][column] == sign and mas[2][column] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if empty_cells == 0:
        return 'Dead heat!'
    return False