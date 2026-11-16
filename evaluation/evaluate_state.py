from enums.eval_weights import Weights
from classes.snake import Snake
from classes.board import Board
from classes.state import State
from evaluation.evaluation_helpers.user_dead import user_dead
from evaluation.evaluation_helpers.user_win import user_win
from evaluation.evaluation_helpers.free_space import free_space
from evaluation.evaluation_helpers.distance_from_big_snakes import distance_from_big_snakes
from evaluation.evaluation_helpers.distance_from_closest_food import distance_from_closest_food
from evaluation.evaluation_helpers.big_snake_bonus import big_snake_bonus

"""
Takes in a state
Calculates the evaluation for the user at that state
User is always index 0 of the state's snake array
Returns the evaluation
"""

def evaluate_state(state: State):
    # Create score variable
    expected_score = 0

    # # Evaluate based on if user loses
    if user_dead(state):
        return Weights.USER_DEAD


    # # Evaluate based on if user wins
    if user_win(state):
        return Weights.USER_WIN

    # Evaluate radius of free space
    expected_score += free_space(state) * Weights.FREE_SPACE

    # Evaluate distance from bigger snakes
    # Evaluate distance from big snakes (exponential penalty for being close)
    max_dist = (state.board.width - 1) + (state.board.height - 1)
    big_snake_dist = distance_from_big_snakes(state) * max_dist  # back to steps

    expected_score += Weights.BIG_SNAKE_CLOSENESS_PENALTY * Weights.BIG_SNAKE_DISTANCE_GROWTH ** -big_snake_dist

    # Evaluate hp
    expected_score += (100 - state.snakes[0].health) * Weights.MISSING_ONE_HP

    # Evaluate distance from closest food
    food_dist = distance_from_closest_food(state)
    max_dist = (state.board.width - 1) + (state.board.height - 1)
    food_dist = min(food_dist, max_dist)  # cap it, see below

    expected_score += Weights.PUNISHMENT_PER_STEP_FROM_FOOD * (Weights.FOOD_DISTANCE_GROWTH ** food_dist - 1)

    # Evaluate relative size
    expected_score += big_snake_bonus(state) * Weights.BIG_ALPHA_SNAKE_BONUS

    # Evaluate dead opponents
    expected_score += state.death_count * Weights.DEAD_OPPONENT_BONUS

    # Return evaluation
    return expected_score