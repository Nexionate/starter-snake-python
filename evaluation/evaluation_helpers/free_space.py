from classes.state import State
from classes.board import Board, BoardStatus

"""
Calculate % of free spaces in a 7x7 grid around the user's head
Return the %
"""
def free_space(state: State):
    our_head_x = state.snakes[0].my_head["x"]
    our_head_y = state.snakes[0].my_head["y"]
    board_width = state.board.width
    board_height = state.board.height

    free_space_count = 0

    for i in range(max(our_head_x - 3, 0), min(our_head_x+4, board_width)):
        for j in range(max(our_head_y - 3, 0), min(our_head_y + 4, board_height)):
            if state.board.grid[i][j] == BoardStatus.EMPTY:
                free_space_count += 1

    return free_space_count / 49