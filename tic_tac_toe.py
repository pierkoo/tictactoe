'''Tic Tac Toe Game for 2 players or player vs bot'''

import random

def get_input(cor_h):
    '''Getting coordinates of the player move with validation if move is
    allowed.
    Expected input - 'x,y' in range 1 to 3 (game board is 3x3)
    Validation checks if:
    -input is in proper format
    -input corresponds to rows & columns
    -move wasn't already made '''

    valid = [1, 2, 3]

    while True:
        while True:
            cor = input('Make a move (x,y) ')
            try:
                cor = [int(e) for e in cor.split(',')]
                break
            except ValueError:
                print('Wrong input, choose again')

        if  len(cor) == 2:
            if cor[0] in valid and cor[1] in valid:
                if cor not in cor_h:
                    cor_h.append(cor)
                    break
        print('Wrong move, choose again')

    return cor, cor_h

def bot_input(cor_h):
    ''' Returns move for bot. For now just generationg random move
    within requirement. Some logic to  be implemented in the future'''

    while True:

        cor = [random.randrange(1, 4), random.randrange(1, 4)]

        if cor not in cor_h:
            cor_h.append(cor)
            break

    return cor, cor_h

def update_board(cor, player, board):
    ''' Returns updated board, based on move coordinates and player
    id '''

    if player == 1:
        mark = 'x'
    else:
        mark = 'o'

    board[cor[0]-1][cor[1]-1] = mark

    return board

def print_board(board):
    ''' Simplest posiible solution to print board-like table '''

    print('', board[0], '\n', board[1], '\n', board[2])

def draw_board(board):
    ''' 'Draws' board in the console '''

    size = range(len(board))
    top = ''.join([' ___' for e in size])
    for i in size:
        print(top)
        side = ''
        for j in size:
            elem = str(board[i][j])
            if elem == '0':
                elem = ' '
            side = side + '| ' + elem + ' '
        side = side + '|'
        print(side)
    print(top)

def check_winner(board):
    ''' Checks board to determine if there is a winner.
        Prints message and returns bool value result to determine if
        game should be continued
    '''

    rows_cols = board[:]

    for i in range(3):
        rows_cols.append([rows_cols[0][i], rows_cols[1][i],
                          rows_cols[2][i]])

    rows_cols.append([rows_cols[0][2], rows_cols[1][1],
                      rows_cols[2][0]])
    rows_cols.append([rows_cols[0][0], rows_cols[1][1],
                      rows_cols[2][2]])

    if [e for e in rows_cols if 'x' in e and 0 not in e and 'o'
            not in e]:
        print('1 wins!')
        result = False

    elif [e for e in rows_cols if 'o' in e and 0 not in e and 'x'
          not in e]:
        print('2 wins!')
        result = False

    elif not [e for e in rows_cols if 0 in e]:
        print('Draw!')
        result = False
    else:
        print('No winner - game continues!')
        result = True
    return result

def players():
    ''' Ask for input to determine game mode - PvP or PvBot
        Returns sigle value:
        0 - 2 player game
        1- 1 player game, bot starts
        2 - 1 player game, player starts
    '''

    bot = 0
    while True:
        try:
            players_qty = int(input('How many players? '))
            if players_qty == 2:
                break
            if players_qty == 1:
                print('You will play vs computer!')
                while True:
                    start = (input('Do you want to start? y/n? '))
                    if start == 'y':
                        print('You wil play as Player 1!')
                        bot = 2
                        break
                    if start == 'n':
                        bot = 1
                        print('You wil play as Player 2!')
                        break
                    print('Incorrect input')

                break
        except ValueError:
            print('Please specify correct number of players: 1 or 2')
    return bot

def swap(to_swap):
    ''' Return 0 for odd(1) and 1 for even(0) input.
        Used to iterate between 0 and 1.
        '''

    return to_swap%2 + 1

def game(game_mode):
    ''' Game. Accepts single argument to specify game mode:
        0 - 2 player game
        1- 1 player game, bot starts
        2 - 1 player game, player starts
     '''

    # Intro - welcoming message and empty board.
    print(' ')
    if game_mode == 0:
        print('Welcome in Tic Tac Toe for 2 players!')
    else:
        print('Welcome in Tic Tac Toe for 1 player!')


    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
            ]
    player = 0
    cor_h = []
    cont = True
    draw_board(board)

    # Step in game. Iterates beetwen players based on 'player' value.
    while cont:
        player = swap(player)
        print('Player', player)

        if game_mode == 0:
            cors = get_input(cor_h)
        elif game_mode == player:
            cors = bot_input(cor_h)
        else:
            cors = get_input(cor_h)

        cor = cors[0]
        cor_h = cors[1]
        board = update_board(cor, player, board)
        draw_board(board)
        cont = check_winner(board)
        #counter+=1

def tic_tac_toe():
    '''Main method of the game'''
    game_mode = players()
    game(game_mode)


if __name__ == '__main__':
    tic_tac_toe()
