class Board:
    # I understand the basics of classes is used to create an object, but I am needing to study what is the point.
    def __init__(self, board):
        self.board = board

    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = "|".join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append("║")

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace("0", " ")
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += (
                        f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                    )
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    # FCC did not always explain items because it would say something like recall that all() syntax is which it was not covered once
    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))
