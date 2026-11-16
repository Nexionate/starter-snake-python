from classes.state import State

def big_snake_bonus(state: State):
    snakes_we_are_bigger_than = len(state.snakes) - 1
    for snake in state.snakes[1:]:
        if len(snake.my_body) >= len(state.snakes[0].my_body):
            snakes_we_are_bigger_than -= 1

    return snakes_we_are_bigger_than
