import random

def board_display():
    print('\n')
    for x in board:
        print(''.join(x))
    print('\n')

def board_check():
    #Checks Columms First
    col = 0
    while(col <= 4):
        if(board[0][col] == board[1][col] == board[2][col]):
            for x,y in players.items():
                if(board[0][col] == y):
                    print('\nThe ' + x + ' Wins')
                    return True
        col += 2

    #Checks Rows Second
    for row in board:
        for x,y in players.items():
            if(row.count(y) == 3):
                print('\nThe ' + x + ' Wins')
                return True

    #Checks Diagonals last
    if(board[0][0] == board[1][2] == board[2][4]):
        for x,y in players.items():
            if(board[0][0] == y):
                print('\nThe ' + x + ' Wins')
                return True
    elif(board[0][4] == board[1][2] == board[2][0]):
        for x,y in players.items():
            if(board[0][4] == y):
                print('\nThe ' + x + ' Wins')
                return True

def game_over():
    if(board_check()):
        return True
    else:
        empty = 0
        for x in board:
            if(x.count('_') == 0 or x.count(' ') == 0):
                empty += 1
                continue
            else:
                break
        if(empty == 0):
            print('\nThe Cat Wins')
            return True
        return False

def player_turn():
    decided = True
    row_answers = ['top','middle','bottom']
    row_sub = {'top':0,'middle':1,'bottom':2}
    col_answers = ['right','middle','left']
    col_sub = {'right':0,'middle':2,'left':4}
    while(decided):
        print('To pick a row, please enter either "Top","Middle", or "Bottom"')
        row_input = input('Now, which row on the board do you pick?:')
        print('To pick a columm, please enter either "Right","Middle", or "Left"')
        col_input = input('Now, which columm on the board do you pick?:')

        if(row_input.lower() not in row_answers):
            print("'" + row_input + "'" + " is an invalid row answer, please try again")
        elif(col_input.lower() not in col_answers):
            print("'" + col_input + "'" + " is an invalid columm answer, please try again")
        else:
            if(board[row_sub[row_input.lower()]][col_sub[col_input.lower()]] not in 'XO'):
                board[row_sub[row_input.lower()]][col_sub[col_input.lower()]] = players['Player']
                decided = False
            else:
                print('This spot has been filled, please try again.')

def bot_turn():
    go = True
    tries = 0
    while(go):
        row = random.randrange(3)
        spot = random.randrange(5)
        if(spot % 2 == 0):
            if(board[row][spot] not in 'XO'):
                board[row][spot] = players['Computer']
                go = False

def main():
    game = True
    while(game):
        top_row = list('_|_|_')
        mid_row = list('_|_|_')
        bot_row = list(' | | ')
        global board, players
        board = [top_row,mid_row,bot_row]
        players = {'Computer':'X','Player':'O'}
        play = True
        user_input = input('Do you want to be "X" or "O"?(enter x or enter o):')

        if(user_input.upper() == 'X'):
            players['Player'] = 'X'
            players['Computer'] = 'O'
        elif(user_input.upper() == 'O'):
            players['Computer'] = 'X'
            players['Player'] = 'O'

        while(play):
            board_display()
            player_turn()
            if(game_over()):
                board_display()
                break
            bot_turn()
            if(game_over()):
                board_display()
                break
        user_input = input('Do want to play again?(Enter y or n):')
        if(user_input.lower() == 'y'):
            print('Ok, let me reset the board\n')
        else:
            print('Goodbye')
            game = False

if(__name__ == "__main__"):
    main()
