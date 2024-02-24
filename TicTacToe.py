import random

def display_board(board):
    print('     |     |   ')
    print('  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+' ')
    print('     |     |   ')
    print('-----------------')
    print('     |     |   ')
    print('  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+' ')
    print('     |     |   ')
    print('-----------------')
    print('     |     |   ')
    print('  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+' ')
    print('     |     |   ')

def player_input():
    
    marker=''
    
    while marker!='X' and marker!='O':
        marker=input("Player 1: Choose X or O: ").upper()
        
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board, marker, pos):
    board[pos]=marker

def win_check(board,marker):
    win_combinations=[
        [1,2,3],[4,5,6],[7,8,9], #All rows
        [1,4,7],[2,5,8],[3,6,9], #All columns
        [1,5,9],[3,5,7] #All diagonals
    ]
    
    for combination in win_combinations:
        if all(board[pos]==marker for pos in combination):
            return True
    return False


def choose_first():
    first=random.randint(0,1)
    
    if first==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,pos):
    return board[pos]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    pos=0
    
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
        pos=int(input('Choose a position: (1-9) '))
        
    return pos

def replay():
    choice=input("Would you like to play again? (Yes or No) ")
    
    return choice.lower()=='yes'

if __name__ == "__main__":        
    
    print("Welcome to Tic Tac Toe")
    
    print("This is a sample board with positions for your reference:")
    
    test_board=["#",'1','2','3','4','5','6','7','8','9']
    
    display_board(test_board)
    
    name1=input("Player 1 Name: ")
    name2=input("Player 2 name: ")
    score1=0
    score2=0
    print(f'{name1}: Score {score1} and {name2}: Score {score2}')
    
    while True:
        
        board=[' ']*10
        player1_marker, player2_marker= player_input()
        
        print(f'{name1} marker: {player1_marker}')
        print(f'{name2} marker: {player2_marker}')
        
        turn=choose_first()
        if turn=='Player 1':
            print(f'{name1} will go first')
        else:
            print(f'{name2} will go first')
            
        play_game=input('Ready to play? (Yes or No) ')
        
        if play_game.lower()=='yes':
            game_on=True
        else:
            game_on=False
            
        while game_on:
            
            if turn=='Player 1':
                
                display_board(board)
                pos=player_choice(board)
                place_marker(board,player1_marker,pos)
                
                if win_check(board,player1_marker):
                    display_board(board)
                    print(f'{name1} WON!!')
                    score1+=1
                    print(f'{name1}: Score {score1} and {name2}: Score {score2}')
                    game_on=False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("TIE GAME!!")
                        score1+=1
                        score2+=1
                        print(f'{name1}: Score {score1} and {name2}: Score {score2}')
                        break
                    else:
                        turn='Player 2'
            else:
                display_board(board)
                pos=player_choice(board)
                place_marker(board,player2_marker,pos)
                
                if win_check(board,player2_marker):
                    display_board(board)
                    print(f'{name2} WON!!')
                    score2+=1
                    print(f'{name1}: Score {score1} and {name2}: Score {score2}')
                    game_on=False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("TIE GAME!!")
                        score1+=1
                        score2+=1
                        print(f'{name1}: Score {score1} and {name2}: Score {score2}')
                        break
                    else:
                        turn='Player 1'
                
        if not replay():
            print("Final scores")
            if score1>score2:
                print(f'{name1} HAS THE HIGHEST SCORES!!')
            elif score2>score1:
                print(f'{name2} HAS THE HIGHEST SCORES!!')
            else:
                print("TIE SCORES!!")
            break