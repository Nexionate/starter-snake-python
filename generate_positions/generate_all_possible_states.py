from itertools import product
from classes.state import State
from enums.moves import Move
from helpers import create_n_dimensional_list
from generate_positions.generate_new_state import generate_new_state

"""
Takes a state object. A state is composed of a board and an array of n snakes
Returns a dictionary + snakeCount where each key is the set of moves and each value is the resulting state
"""
def generate_all_possible_states(state: State):
    # Create the n-dimensional array. No helper function needed
    snake_count = len(state.snakes) # Kind of hacky
    moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
    # array_shape = [moves.count() for _ in range(snake_count)]
    possible_states = dict()

    # Iterate through each combination of moves
    possible_move_combos = product(moves, repeat=snake_count)
        # For each combination of moves, call generate_new_state()
        # Store the new state in the array
    for move_combo in possible_move_combos:
        new_state = generate_new_state(state=state, moves=move_combo)
        possible_states[move_combo] = new_state

    # Return the array
    return possible_states, snake_count



