"""
Autor: Ángel Carballo Cremades

Ironhack Data Analytics bootcamp

Week 1 mini project

Chess

"""

# Type of pieces tuple
PIECES =("rook","knight","bishop","king","queen","bishop","knight","rook","pawn")
TEAM = ("White","Black")

class Piece(object):
    """Chess piece class, takes inputs type, team and position on board"""
    def __init__(self, typee, team):
        self.type = typee # Type of piece, take values fron PIECES dictionary
        self.team = team # White or Black

    def __str__(self):
        return f'{self.type}'

    def move_king(self,actual_position):
        """This functions is for kings only, takes actual position on the board [row,column] and returns an array os possible moves not considering friends or foes"""
        if self.type != "king":
            raise TypeError('Not "king" piece type')

        a_r,a_c = actual_position #piece actual row and column indexes
        pos_mov = [] #array containing possible moves of piece

        #Checking which columns the piece can move to, preventing out of board positions
        if a_c == 0:
            columns = [0,1]
        elif a_c == 7:
            columns = [-1,0]
        else:
            columns = [-1,0,1]

        #Checking which rows the piece can move to, preventing out of board positions
        if a_r == 0:
            rows = [0,1]
        elif a_r == 7:
            rows = [-1,0]
        else:
            rows = [-1,0,1]

        #Possible movement array, not considering friends or foes.
        pos_mov = [[a_r+row,a_c+column] for row in rows for column in columns if not(row==0 and column==0)]

        return pos_mov




                # if board[a_r+1][a_c+c] and (not board[a_r+1][a_c+c] or board[a_r+1][a_c+c].team != self.team):
                #     pos_mov.append([a_r+1,a_c+c])

                # if board[a_r-1][a_c+c] and board[a_r-1][a_c+c].team != self.team:
                #     pos_mov.append([a_r-1,a_c+c])

                # if board[a_r][a_c+c] and board[a_r][a_c-c].team != self.team and c != a_c:
                #     pos_mov.append([a_r,a_c+c])

    def possible_moves(self, actual_position:list, board):
        """This function returns the positions the piece can move to, taking into account board size, allies and enemies position"""
        a_r,a_c = actual_position #piece actual row and column indexes
        pos_mov = [] #array containing possible moves of piece

        # if self.type == 'king':



class Board(object):
    """Chess board class, when instantiated creates a brand new board with all pieces at start position"""
    def __init__(self):
        self.board = [[None for place in range(4)] for row in range(8)]
        # Creating white pieces, 2 rows
        self.whites = []
        self.blacks = []

        # Creating initial white and black pieces, _low are pieces from rook to rook, _high are pawns
        w_low = [Piece(PIECES[i],TEAM[0]) for i in range(8)]
        w_high = [Piece(PIECES[-1],TEAM[0]) for i in range(8)]
        b_low = [Piece(PIECES[i],TEAM[1]) for i in range(8)]
        b_high = [Piece(PIECES[-1],TEAM[1]) for i in range(8)]

        # Adding white and black pieces to board in initial positions
        for i in range(8):
            self.board[i].insert(0,w_low[i])
            self.board[i].insert(1,w_high[i])
            self.board[i].insert(6,b_high[i])
            self.board[i].insert(7,b_low[i])

        # self.whites.append(w_low)
        # self.whites.append(w_high)
        # self.blacks.append(b_low)
        # self.blacks.append(b_high)

    def __str__(self):
        for row in self.board:
            for piece in row:
                print(piece, end = '\t')
            print('')
        return ""


    def kill_piece(self,position:list):
        r,c = position

        print(f'{self.board[r][c]} at {r},{c} killed')

        self.board[r][c] = None





    def move_piece(self,actual_position,new_position):
        """Changes a piece location to the one indicated"""





board = Board()

# print(new_board.board)

print(board)
# board.kill_piece([3,1])
# board.board[3][0].possible_moves([3,0],board.board)
# print(board)

print(board.board[3][0].move_king([3,0]))
