class TicTacToe:
    EMPTY='-'
    def __init__(self):
        self.board=[[self.EMPTY]*3 for _ in range(3)]
        self.curr_player='X'
        self.moves=0
    def display_board(self):
        print('\nBoard:')
        for row in self.board:
            print(' | '.join(row))
        print()
    def make_move(self,row,col):
        if not (0<=row<3 and 0<=col<3):
            print('Invalid row or column number')
            return False
        if self.board[row][col]!=self.EMPTY:
            print('Cell Already Filled')
            return False
        self.board[row][col]=self.curr_player
        self.moves+=1
        return True
    def switch_player(self):
        self.curr_player='O' if self.curr_player=='X' else 'X'
    def check_win_condition(self):
        b=self.board
        for i in range(3):
            #row check
            if (b[i][0]==b[i][1]==b[i][2]==self.curr_player):
                return self.curr_player
            #column check
            if (b[0][i]==b[1][i]==b[2][i]==self.curr_player):
                return self.curr_player
        #diagonal check
        if b[0][0]==b[1][1]==b[2][2]==self.curr_player:
            return self.curr_player
        #antidiagonal check
        if b[0][2]==b[1][1]==b[2][0]==self.curr_player:
            return self.curr_player
        if self.moves==9:
            return "DRAW"
        return None
def play():
    game=TicTacToe()
    while True:
        game.display_board()
        print(f"player {game.curr_player}'s turn")
        try:
            row,col=map(int,input('Enter row and column you want to place (eg:1 0):-').split())
        except ValueError:
            print("Enter the position properly")
            continue
        if game.make_move(row,col):
            result=game.check_win_condition()
            if result=='DRAW':
                print("It's a Draw!!!")
                break
            elif result:
                game.display_board()
                print(f'Player {game.curr_player} is the winner!!!')
                break
            game.switch_player()
play()