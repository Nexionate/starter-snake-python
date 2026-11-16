from helpers import create_n_dimensional_list
from generate_positions.generate_all_possible_states import generate_all_possible_states
from evaluation.evaluate_matrix import evaluate_matrix
from enums.moves import Move

"""
Takes in a board state and index of the user into the snake array whose score we want to maximize
Search all possible moves 1 level deep
Returns best move to make + top 3 move sets + their resulting board states + their evals
"""

def get_move(state):
    possible_states_dict, snake_count = generate_all_possible_states(state)
    eval_index, eval_score = evaluate_matrix(possible_states_dict, snake_count)
    return Move(eval_index), eval_score
    
