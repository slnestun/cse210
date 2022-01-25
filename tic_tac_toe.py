def main():
    player = player_turn('')
    table = create_table()
    winner = False
    draw = False
    movements = 0
    
    while winner != True and draw == False:
        movements = movements + 1
        print_table(table)
        player_choose = int(input(f'{player}\'s turn to choose a square (1-9):'))
        player_move(table,player_choose,player)
        player = player_turn(player)
        winner = game(table)
        draw = draw_game(movements)
        print(draw)
        print(movements)
        
    print_table(table)
    print('Good game. Thanks for playing!') 
        

#create table for tic tac toe
def create_table():
    table = []
    for i in range (9):
        table.append(i +1)
    return table

#function to print the table of the game
def print_table(table):
    print()
    print(f'{table[0]}|{table[1]}|{table[2]}')
    print('-+-+-')
    print(f'{table[3]}|{table[4]}|{table[5]}')
    print('-+-+-')
    print(f'{table[6]}|{table[7]}|{table[8]}')
    print()

#define player turn
def player_turn(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'


#insert player move on table
def player_move(table, position, player):
    table [position-1]= player

#function to define winnner

def game(table):
    for i in range (9):
        if (table[0] ==table[1] ==table[2] or
            table[3] ==table[4] ==table[5] or
            table[6] ==table[7] ==table[8] or
            table[0] ==table[4] ==table[8] or
            table[2] ==table[4] ==table[6] or
            table[0] ==table[3] ==table[6] or
            table[1] ==table[4] ==table[7] or
            table[2] ==table[5] ==table[8]):
            return True
    return False

#condition to draw a game
def draw_game(movements):
    if movements == 9:
        return True
    else:
        return False


if __name__ =='__main__':
    main()