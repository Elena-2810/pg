from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        
        self.__color = color
        self.__position = position
        self._board = None

    @abstractmethod
    def possible_moves(self):
       
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
       
        row, col = self.position
        if self.color == 'white':
            candidate = (row + 1, col)
        else:
            candidate = (row - 1, col)

        if not self.is_position_on_board(candidate):
            return []

        if self._board is not None:
            if self._board.is_occupied(candidate):
                return []
            else:
                return [candidate]
        
        return [candidate]

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
       
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final = []
        for m in moves:
            if not self.is_position_on_board(m):
                continue
            if self._board is not None:
                if self._board.is_occupied(m):
                    
                    if self._board.is_enemy(m, self.color):
                        final.append(m) 
                    else:
                        continue
                else:
                    final.append(m)
            else:
                final.append(m)
        return final

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        
        row, col = self.position
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        moves = []
        for dr, dc in directions:
            step = 1
            while True:
                new_pos = (row + dr*step, col + dc*step)
                if not self.is_position_on_board(new_pos):
                    break
                if self._board is not None and self._board.is_occupied(new_pos):
                  
                    if self._board.is_enemy(new_pos, self.color):
                        moves.append(new_pos)  
                    break  
                moves.append(new_pos)
                step += 1
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        
        row, col = self.position
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        moves = []
        for dr, dc in directions:
            step = 1
            while True:
                new_pos = (row + dr*step, col + dc*step)
                if not self.is_position_on_board(new_pos):
                    break
                if self._board is not None and self._board.is_occupied(new_pos):
                    if self._board.is_enemy(new_pos, self.color):
                        moves.append(new_pos)
                    break
                moves.append(new_pos)
                step += 1
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
       
        row, col = self.position
        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]
        moves = []
        for dr, dc in directions:
            step = 1
            while True:
                new_pos = (row + dr*step, col + dc*step)
                if not self.is_position_on_board(new_pos):
                    break
                if self._board is not None and self._board.is_occupied(new_pos):
                    if self._board.is_enemy(new_pos, self.color):
                        moves.append(new_pos)
                    break
                moves.append(new_pos)
                step += 1
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
      
        row, col = self.position
        deltas = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]
        moves = []
        for dr, dc in deltas:
            new_pos = (row + dr, col + dc)
            if not self.is_position_on_board(new_pos):
                continue
            if self._board is not None and self._board.is_occupied(new_pos):
                if self._board.is_enemy(new_pos, self.color):
                    moves.append(new_pos)
                
            else:
                moves.append(new_pos)
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


class Board:
    
    def __init__(self, pieces=None):
        self.pieces = pieces[:] if pieces else []

    def is_occupied(self, pos):
        return self.get_piece(pos) is not None

    def get_piece(self, pos):
        for p in self.pieces:
            if p.position == pos:
                return p
        return None

    def is_enemy(self, pos, color):
        p = self.get_piece(pos)
        if p is None:
            return False
        return p.color != color

    def add_piece(self, piece):
        self.pieces.append(piece)
        piece._board = self

    def remove_piece(self, piece):
        if piece in self.pieces:
            self.pieces.remove(piece)
            piece._board = None

    def move_piece(self, piece, new_pos):
        
        target = self.get_piece(new_pos)
        if target is not None:
            self.remove_piece(target)
        piece.position = new_pos


def place_board(pieces):
    
    board = Board(pieces)
    for p in pieces:
        p._board = board
    return board


if __name__ == "__main__":
 
    white_rook = Rook("white", (1,1))
    white_pawn = Pawn("white", (2,1))
    black_knight = Knight("black", (3,1)) 
    black_bishop = Bishop("black", (4,4))
    white_queen = Queen("white", (2,4))
    white_king = King("white", (1,5))

    pieces = [white_rook, white_pawn, black_knight, black_bishop, white_queen, white_king]
    board = place_board(pieces)

    
    print(white_rook)
    print("Rook possible moves (should be blocked by Pawn at (2,1)):", white_rook.possible_moves())
    print()

   
    print(white_pawn)
    print("Pawn possible moves:", white_pawn.possible_moves())
    print()

   
    print(white_queen)
    print("Queen possible moves:", white_queen.possible_moves())
    print()

    
    print(black_bishop)
    print("Bishop possible moves:", black_bishop.possible_moves())
    print()

    
    print(white_king)
    print("King possible moves:", white_king.possible_moves())
    print()
