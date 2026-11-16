from classes.state import State
from classes.board import Board
from classes.snake import Snake
from helpers.manhattan_distance import manhattan_distance
import math

def distance_from_closest_food(state: State):
    closest_food_index = 0
    closest_food_distance = state.board.width * state.board.height

    if not state.board.food:
        return 0

    for food, food_index in zip(state.board.food, range(len(state.board.food))):
        dist = manhattan_distance(state.snakes[0].my_head, food)
        if dist < closest_food_distance:
            closest_food_index = food_index
            closest_food_distance = dist

    for snake in state.snakes[1:]:
        if manhattan_distance(snake.my_head, state.board.food[closest_food_index]) < closest_food_distance:
            closest_food_distance = state.board.width * state.board.height

    return closest_food_distance
