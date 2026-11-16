from classes.state import State
from classes.snake import Snake
from classes.board import Board
from helpers.manhattan_distance import manhattan_distance

def distance_from_big_snakes(state: State):
    big_snake_count = 0
    sum_distances = 0

    for snake_id in range(1, len(state.snakes)):
        if len(state.snakes[snake_id].my_body) > len(state.snakes[0].my_body):
            manhatdist = manhattan_distance(state.snakes[snake_id].my_head, state.snakes[0].my_head)
            sum_distances += manhatdist
            big_snake_count += 1

    if big_snake_count == 0:
        return 1
    else:
        max_dist = (state.board.width - 1) + (state.board.height - 1)
        return (sum_distances / big_snake_count) / max_dist