class Cell:
    def __init__(self, value):
        self.value=value

    def __str__(self):
        return self.value
    
class XCell(Cell):
    def __init__(self):
        super().__init__('X')

class OCell(Cell):
    def __init__(self):
        super().__init__('O')

class TicTacToe:

    def __init__(self, board):
        self.board=board

    def checkio(self):
        for row in self.board:
            if row[0]==row[1]==row[2] and row[0]!='.':
                return row[0]
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '.':
                return self.board[0][col]
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] !='.':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2]!='.':
            return self.board[0][2]
        
        return "D"
    
