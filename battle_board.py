class Battle_Board():
    def __init__(self) -> None:
        self.row_label = ['A','B','C','D','E','F','G','H','I','J','K'/
            'L','M','N','O','P','Q','R','S','T']
        self.column_label = [str(range(1,21))]
        
        self.grid = []
        for row in range(20):
             for column in range(20):
                 self.grid[row][column] = '.'


        pass


self = Battle_Board()