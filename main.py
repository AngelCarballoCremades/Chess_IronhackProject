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
        """This functions is for kings only, takes actual position on the board [row,column] and returns an array of possible moves not considering friends or foes"""
        if self.type != "king":
            raise TypeError('Not "king" piece type')

        a_r,a_c = actual_position #piece actual row and column indexes
        pos_mov = [] #array containing possible moves of piece

        # 8 possible moves of a king.
        pos_mov = [[1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,0],[-1,1],[-1,-1]]

        #Possible movement array, not considering friends or foes. Considering board limits.
        pos_mov = [[a_r+row,a_c+column] for row,column in pos_mov if a_r+row>=0 and a_r+row<=7 and a_c+column>=0 and a_c+column<=7]

        return pos_mov

    def move_pawn(self,actual_position):
        """This functions is for pawns only, takes actual position on the board [row,column] and returns an array of possible moves not considering friends or foes"""
        if self.type != "pawn":
            raise TypeError('Not "pawn" piece type')

        a_r,a_c = actual_position #piece actual row and column indexes
        pos_mov = [] #array containing possible moves of piece

        #Checking which rows the piece can move to, preventing out of board positions
        if a_r == 0:
            rows = [0,1]
        elif a_r == 7:
            rows = [-1,0]
        else:
            rows = [-1,0,1]

        if self.team == 'White':
            columns = [1]
            if a_c == 1: # considering first pawn movement can be 2 squares
                columns.append(2)

        if self.team == 'Black':
            columns = [-1] #Blacks move in negative direction, left
            if a_c == 6: # considering first pawn movement can be 2 squares
                columns.append(-2)

        #Possible movement array, not considering friends or foes. White pawn moves +column, Black pawn moves -column.
        pos_mov = [[a_r+row,a_c+column] for row in rows for column in columns if not (row!=0 and column in [2,-2])]

        return pos_mov

    def move_knight(self,actual_position):
        """This functions is for knights only, takes actual position on the board [row,column] and returns an array of possible moves not considering friends or foes"""
        if self.type != "knight":
            raise TypeError('Not "knight" piece type')

        a_r,a_c = actual_position #piece actual row and column indexes
        pos_mov = [] #array containing possible moves of piece

        # Building the 8 possible places for the knight
        pos_mov = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]

        #Possible movement array, not considering friends or foes. Conditional to avoid out of board places.
        pos_mov = [[a_r+row,a_c+column] for row,column in pos_mov if a_r+row>=0 and a_c+column>=0 and a_r+row<=7 and a_c+column<=7]

        return pos_mov

    def move_queen_rook_bishop(self,actual_position):
        """This functions is for queens, bishops or rooks only, takes actual position on the board [row,column] and returns an array of possible moves not considering friends or foes"""
        if self.type not in ["queen","rook","bishop"]:
            raise TypeError('Not "queen", "rook" or "bishop" piece type')

        a_r,a_c = actual_position #piece actual row and column indexes

        # Run to get arrays of possible movements
        # print('h_p = ', [[0,i] for i in range(1,8)])
        # print('h_n = ', [[0,-i] for i in range(1,8)])
        # print('v_p = ', [[-i,0] for i in range(1,8)])
        # print('v_n = ', [[i,0] for i in range(1,8)])
        # print('d_pp = ', [[-i,i] for i in range(1,8)])
        # print('d_pn = ', [[i,-i] for i in range(1,8)])
        # print('d_np = ', [[i,i] for i in range(1,8)])
        # print('d_nn = ', [[-i,-i] for i in range(1,8)])

        # Possible movements, h:horizontal, v:vertical, d_p:diagonal+slope, d_n:diagonal-slope. aditional p and n is to indicate direction.
        # p = up or right move, n = down or left move
        h_p =  [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
        h_n =  [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]
        v_p =  [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0]]
        v_n =  [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
        d_pp =  [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]]
        d_pn =  [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]
        d_np =  [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
        d_nn =  [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]

        #Possible movement array, not considering friends or foes. Conditional to avoid out of board places.
        h_p = [[a_r+row,a_c+column] for row,column in h_p if a_c+column<=7]
        h_n = [[a_r+row,a_c+column] for row,column in h_n if a_c+column>=0]
        v_p = [[a_r+row,a_c+column] for row,column in v_p if a_r+row>=0]
        v_n = [[a_r+row,a_c+column] for row,column in v_n if a_r+row<=7]
        d_pp = [[a_r+row,a_c+column] for row,column in d_pp if a_r+row>=0 and a_c+column<=7]
        d_pn = [[a_r+row,a_c+column] for row,column in d_pn if a_c+column>=0 and a_r+row<=7]
        d_np = [[a_r+row,a_c+column] for row,column in d_np if a_r+row<=7 and a_c+column<=7]
        d_nn = [[a_r+row,a_c+column] for row,column in d_nn if a_r+row>=0 and a_c+column>=0]

        # Returning possible movements for each type of piece
        if self.type == 'queen':
            return [h_p,h_n,v_p,v_n,d_pp,d_pn,d_np,d_nn]
        elif self.type == 'rook':
            return [h_p,h_n,v_p,v_n]
        elif self.type == 'bishop':
            return [d_pp,d_pn,d_np,d_nn]


    def possible_moves(self, actual_position:list, board):
        """This function returns the positions the piece can be moved to, uses possible moves of move_* functions (board borders), allies and enemies positions."""
        a_r,a_c = actual_position #piece actual row and column indexes
        board_pos_mov = [] #array containing possible moves of piece within board
        pos_mov = [] #array containing possible moves of piece within board and analyzing allies and enemies

        # Getting possible moves from moves_* methods.
        if self.type == 'king':
            board_pos_mov = self.move_king(actual_position)
        elif self.type == 'pawn':
            board_pos_mov = self.move_pawn(actual_position)
        elif self.type == 'knight':
            board_pos_mov = self.move_knight(actual_position)
        elif self.type in ['queen','rook','bishop']:
            board_pos_mov = self.move_queen_rook_bishop(actual_position)

        # Analyzing possible moves with friends and foes for pawn
        if self.type == 'pawn':
            for row,column in board_pos_mov:

                # Checking for moves in horizontal direction
                if row == a_r:
                    if board[row][column] == None: #Checking for empty square
                        pos_mov.append([row,column])
                    else:
                        pass # if there is a piece in the square the pawn cannot be moved

                # Checking for moves in diagonal (attacks)
                else:
                    if board[row][column] != None: #Checking if there is a piece in the square
                        if board[row][column].team != self.team: # Checking wether the piece is ally or enemy
                            pos_mov.append([row,column]) # Append if it is enemy
                        else:
                            pass # If the piece is an ally the piece cannot be moved

        # Analyzing possible moves with friends and foes for king and knight
        if self.type in ['king','knight']:
            for row,column in board_pos_mov:
                if board[row][column] == None: #Checking for empty square
                    pos_mov.append([row,column])
                elif board[row][column].team != self.team: #Checking for ally or enemy
                    pos_mov.append([row,column])
                else:
                    pass
        # Analyzing possible moves with friends and foes for queen, rook and bishop
        elif self.type in ['queen','rook','bishop']:
            for direction in board_pos_mov: # testing for every movement direction
                for row,column in direction:
                    if type(board[row][column]) == type(self): # checking if there is a piece in the square
                        if board[row][column].team != self.team: # checking piece's team
                            pos_mov.append([row,column])
                            break # Movement stops because there is a enemy
                        else:
                            break # if the piece in the square is an ally the analyzed piece cannot move further in that direction

                    else:
                        pos_mov.append([row,column]) # If the square is empty (None) the piece can move in that direction

        return pos_mov


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
        print('\t0\t\t1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7')
        r = 0
        for row in self.board:
            print(r, end = '\t')
            for piece in row:
                print(piece, end = '\t')
            print(r)
            r+=1
        print('\t0\t\t1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7')
        return ""

    def kill_piece(self,position:list):
        """This method kills a piece located at the position [row,column]. Board location becomes None"""
        r,c = position
        if self.board[r][c] != None: #Checking if square is empty
            print(f'{self.board[r][c].team} {self.board[r][c]} at {r},{c} killed')
            self.board[r][c] = None
        else:
            raise Exception("The indicated position is empty (None)")


    def move_piece(self,actual_position,new_position):
        """Changes a piece location to the one indicated"""
        pass









board = Board()

print(board)
# board.kill_piece([3,1])
# board.board[3][0].possible_moves([3,0],board.board)
# print(board)

# print(board.board[3][7].move_king([3,7]))
# print(board.board[6][1].move_pawn([6,1]))
# print(board.board[1][0].move_knight([1,0]))
# print(board.board[6][0].move_knight([6,0]))
# print(board.board[1][7].move_knight([1,7]))
# print(board.board[6][7].move_knight([6,7]))
# print(board.board[4][0].move_queen_rook_bishop([4,0]))
# print(board.board[2][0].move_queen_rook_bishop([2,0]))

row = 0
for row in range(8):
    board.kill_piece([row,0])
    board.kill_piece([row,6])

print(board)

# print(board.board[4][6].possible_moves([4,6],board.board))
# print(board.board[6][1].move_pawn([6,1]))
# print(board.board[1][0].move_knight([1,0]))
# print(board.board[6][0].move_knight([6,0]))
# print(board.board[1][7].move_knight([1,7]))
# print(board.board[6][7].move_knight([6,7]))
# print(board.board[4][0].move_queen_rook_bishop([4,0]))
# print(board.board[2][0].move_queen_rook_bishop([2,0]))





