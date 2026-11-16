from classes.state import State
from enums.moves import Move
import copy

"""
Takes in a State and a tuple of moves
Performs each move on a copy of the state
Returns the new State

TO DECIDE LATER: Early quit logic if snake dies. Might not work
"""
def generate_new_state(state: State, moves: tuple[Move, ...]) -> State:
    new_state = copy.deepcopy(state)
    # Pair moves with snakes (not list positions), since ids stop matching indices once snakes die
    for snake, move in zip(list(new_state.snakes), moves):
        new_state.perform_move(snake.id, move)

    return new_state