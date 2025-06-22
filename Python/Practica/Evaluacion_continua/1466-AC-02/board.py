# from utils import Utils


class Board:
    """
    Class that represents the Connect Four game board.\n
    Attr:
        _row (int): Number of rows of the board.
        _col (int): Number of columns of the board.
        _board (list): Matrix that represents the board.
    """
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._board = []
        self._empty_cell = ".   "
        self.create_board()


    def create_board(self) -> list:
        """
        Creates a board game grid\n
        Args:
            x (int): ROWS
            y (int): COLUMNS

        Returns:
            (list): 2D array with the board generated
        """
        # Generamos el board de juego.
        for i in range(self._row):
            row = []
            for j in range(self._col):
                row.append(self._empty_cell)

            self._board.append(row)

        return self._board


    def print_board(self):
        """
        Muestra el tablero por pantalla\n
        Args:
            (list): 2D List

        Returns:
            (list): 2D array rendered in CMD.
        """
        from utils import Utils
        Utils.clear_terminal()

        # Board header:
        print("   ".join(str(n + 1) for n in range(self._col)))
        # Board
        for row in self._board:
            print("".join(row))


    def get_board_copy(self):
        """
        Returns a copy of the current game board.

        Returns:
            list: A new list of lists representing the current state of the board.
        """
        return [row[:] for row in self._board]


    def is_valid_column(self, col: int) -> bool:
        """
        Checks if a column is valid for inserting a piece.
        Args:
            col (int): The index of the column to check.

        Returns:
            (bool): True if the column is valid for a move, False otherwise.
        """
        if col < 0 or col >= self._col:
            return False

        if self._board[0][col] == self._empty_cell:
            return True

        else:
            return False


    def get_valid_columns(self) -> list:
        """
        Returns a list of valid columns where a piece can be played.

        Uses the is_valid_column method to filter and collect all columns
        that are available for a move.

        Returns:
            list: A list of column indices (int) that are valid for a move.
        """
        valid_columns = []

        for col in range(self._col):
            if self.is_valid_column(col):
                valid_columns.append(col)

        return valid_columns


    def get_available_row(self, col: int) -> int:
        """
        Returns the lowest row index in the specified column where a piece can be placed.

        Args:
            col (int): The column index to check for available space.

        Returns:
            int: The row index where the piece can be inserted, or -1 if the column is full.
        """
        for row in reversed(range(self._row)):
            if self._board[row][col] == self._empty_cell:
                return row

        return -1


    def insert_piece(self, col: int, piece: str) -> bool:
        """
        Inserts a piece into the specified column of the board.

        Args:
            col (int):
            piece (str):

        Returns:
            (bool): True if the piece was successfully inserted, False if the column is full.
        """
        from utils import Utils
        Utils.clear_terminal()

        for row in reversed(range(self._row)):
            if self._board[row][col] == self._empty_cell:
                self._board[row][col] = piece
                return True

        print(self._board)
        return False  # La columna está llena