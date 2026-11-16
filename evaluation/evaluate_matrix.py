from enums.moves import Move
from itertools import product
from evaluation.evaluate_state import evaluate_state
import math

WORST_CASE_WEIGHT = 0.5  # how much the worst outcome counts on top of the average

"""
Takes in a dictionary of states
User is always snake 0
Returns the move + evaluation of the best possible move the player can make
"""

def evaluate_matrix(possible_states: dict, dimensions):
    moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
    opponent_count = dimensions - 1
    row_length = 4 ** opponent_count

    # Create temp datastructures to track sum and worst payoff for each row
    rows_sum_evals = [0 for _ in range(4)]
    rows_min_evals = [math.inf for _ in range(4)]
    # Create a temp variable to track highest blended row score
    highest_row_score = -math.inf
    highest_row_score_index = 0

    # Iterate through each row. For each row entry...
        # Get the evaluation
        # Update the row sum and row worst case
        # If row is done, blend avg + worst case, update highest if this row is higher than current
    for user_move in moves:
        for opponent_move_combo in product(moves, repeat=opponent_count):
            current_state_key = (user_move,) + opponent_move_combo
            current_state = possible_states[current_state_key]
            current_state_eval = evaluate_state(current_state)
            rows_sum_evals[user_move] += current_state_eval
            rows_min_evals[user_move] = min(rows_min_evals[user_move], current_state_eval)

        row_avg = rows_sum_evals[user_move] / row_length
        row_score = row_avg + WORST_CASE_WEIGHT * rows_min_evals[user_move]

        if row_score > highest_row_score:
            highest_row_score = row_score
            highest_row_score_index = user_move

    # Return row index + blended score
    return (highest_row_score_index, highest_row_score)