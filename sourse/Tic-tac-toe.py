import os
import colorama
colorama.init()
white_color = colorama.Fore.WHITE
green_color = colorama.Fore.GREEN
blue_color = colorama.Fore.BLUE
red_color = colorama.Fore.RED

board = list(range(0, 9))
celles = 3
dashes = 13
spase = 10
clear = lambda: os.system('cls')

counter = 0
is_win = False
wins_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
)
print(white_color)
print('Tic-tac toe- the game for two players')

def draw_board():
    for i in range(celles):
        print(' ' * spase, end='')
        print(green_color + '-' * dashes)
        print(' ' * spase, end='')
        print(f'{green_color}| {white_color}{board[0 + i * 3]} {green_color} | {white_color}{board[1 + i * 3]} {green_color} | {white_color}{board[2 + i * 3]}{green_color} |')
        print(' ' * spase, end='')
        print('-' * dashes)

player_token = ''

while not is_win:
    draw_board()

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    player_answer = input(f'Where we put a {player_token} ')
    player_answer = int(player_answer)

    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print(f'{red_color}This call is alredy token!')
        continue
    counter += 1

    if counter > 4:
        for each in wins_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break
        if is_win:
            print(f'{player_token} is win!')
            draw_board()
            exit = input("Pres Enter to exit")
            if exit == '':
                break
    if counter == 9:
        print(f"{blue_color}Draw! You're amazing!")
        draw_board()
        exit = input("Pres Enter to exit =)")
        if exit == '':
            break