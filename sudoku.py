import json


def read_file(filename):
    """Read a Sudoku board from a JSON file and return it as a 2D list."""
    
    with open(filename, "r") as file:
        board_json = json.load(file)

    # Assign the key-value pair.
    board = board_json["board"]
    
    return board


def save_file(filename, board):
    """Save the Sudoku board to keep game progress."""

    board_json = {"board": board}
    with open(filename, "w") as file:
        json.dump(board_json, file)

    
def display_board(board):
    """Display the current Sudoku board to the console."""

    # Display column headers.
    print("   A B C D E F G H I")

    # Loop through all nine rows.
    for row in range(9):

        # Print horizontal separators after rows 3 and 6.
        if row == 3 or row == 6:
            print("   -----+-----+-----")

        # Print the row number.
        print(f"{row + 1}  ", end="")

        # Loop through all nine columns.
        for col in range(9):

            # Print vertical separators after columns C and F.
            if col == 3 or col == 6:
                print("|", end="")

            # Retrieve the value at the current square.
            value = board[row][col]

            # Display blank spaces instead of zeros.
            if value == 0:
                print(" ", end="")
            else:
                print(value, end="")

            # Add spacing between numbers, except the ends of the 3 x 3.
            if col not in (2, 5, 8):
                print(" ", end="")
        
        print()


def get_user_move():
    """Prompt the user for a move."""
    
    move = input("\n> ").strip()

    return move


def get_value(coordinate):
    """Prompt the user for the value at the specific coordinate."""

    try:
        value = int(input(f"What is the value at '{coordinate}': "))
        return value

    except ValueError:
        return None


def convert_coordinates(coordinate) -> tuple[int, int]:
    """convert a coordinate such as 'B5' into a column, row such as (1,4)."""
    
    # Create list to map to number.
    column_map = ["A", "B", "C", "D","E", "F", "G", "H", "I"]

    # Find the match for the column and map number to it.
    for column in range(len(column_map)):
        if column_map[column] == coordinate[0]:
            column_num = column
    
    # Get the right coordinate number for the row.
    row_int = int(coordinate[1])
    row_num = row_int - 1
    
    coordinate_pair = (column_num, row_num)

    return coordinate_pair


def check_coordinate(coordinate):
    """Handles incorrect coordinates. A0, banana, not between A-I"""

    if len(coordinate) != 2:
        return False
    
    column_letter = coordinate[0]
    row_number = coordinate[1]

    if column_letter < "A" or column_letter > "I":
        return False

    if row_number < "1" or row_number > "9":
        return False

    return True


def check_value(board, coordinate_pair, value):
    """Checks the proposed value against Sudoku rules."""

    column = coordinate_pair[0]
    row = coordinate_pair[1]

    # Check to make sure the value is between 1 and 9.
    if value < 1 or value > 9:
        return False

    # Check for duplicates in the selected row.
    for col in range(9):
        if board[row][col] == value:
            return False

    # Check for duplicates in the selected column.
    for r in range(9):
        if board[r][column] == value:
            return False

    # Find the top-left corner of the 3x3 square.
    box_row = (row // 3) * 3
    box_col = (column // 3) * 3

    # Check for duplicates inside the 3x3 square.
    for r in range(box_row, box_row + 3):
        for col in range(box_col, box_col + 3):
            if board[r][col] == value:
                return False

    # No Sudoku rules were violated.
    return True


def is_square_available(board, coordinate_pair):
    """Checks whether a square is occupied."""
    
    column = coordinate_pair[0]
    row = coordinate_pair[1]

    return board[row][column] == 0


def play_game(board):
    """Delegate game structure for playing the game."""
    
    # Game loop to keep going.
    while True:

        display_board(board)
        
        print("Specify a coordinate to edit or 'Q' to save and quit")   

        move = get_user_move()
        normalized_move = move

        if move == "Q":
            return

        if len(move) == 2:
            if move[0].isdigit():
                normalized_move = move[::-1].upper()

            else:
                normalized_move = move.upper()
            
        if not check_coordinate(normalized_move):
            print(f"ERROR: Square {move} is invalid.")
            continue

        coordinate_pair = convert_coordinates(normalized_move)

        if not is_square_available(board, coordinate_pair):
            print(f"ERROR: Square {normalized_move} is filled")
            continue
        
        value = get_value(normalized_move)

        if value is None:
            print("ERROR: The value is invalid.")
            continue


        if not check_value(board, coordinate_pair, value):
            print(f"ERROR: The value {value} is invalid.")
            continue

        board[coordinate_pair[1]][coordinate_pair[0]] = value


def main():
    filename = input("Where is your board located? ")
    
    board = read_file(filename)
    
    play_game(board)

    save_file(filename, board)


if __name__ == "__main__":
    main()