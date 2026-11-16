from enum import Enum
from classes.snake import Snake

class BoardStatus(Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2



class Board:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.grid = [[BoardStatus.EMPTY for _ in range(height)] for _ in range(width)]
        self.food = food

    
    def update_dead_snake(self, snake):
        for cell in snake.my_body:
            self.grid[cell["x"]][cell["y"]] = BoardStatus.EMPTY

    def update_any_tile_empty(self, entity):
            for cell in entity:
                self.grid[cell["x"]][cell["y"]] = BoardStatus.EMPTY

    def update_any_tile_snake(self, entity):
                for cell in entity:
                    self.grid[cell["x"]][cell["y"]] = BoardStatus.SNAKE


    def update_eaten_food(self, snake):
        self.grid[snake.my_head["x"]][snake.my_head["y"]] = BoardStatus.EMPTY

    def update_board_with_snakes(self, snakes):
        for snake in snakes:
            for cell in snake.my_body:
                self.grid[cell["x"]][cell["y"]] = BoardStatus.SNAKE

    def update_board_with_food(self, food):
        for piece in food:
                for x, y in piece: 
                    self.grid[x][y] = BoardStatus.FOOD

    def check_if_board_position_food(self, x, y):
            if self.grid[x][y] == Board.Status.FOOD:
                return True
            return False



    def check_if_board_position_snake(self, x, y):
        if self.grid[x][y] == Board.Status.SNAKE:
            return True
        return False
        
    """
    Places food onto the grid when board is initialized
    """
    def initialize_food_on_grid(self):
        for food_item in self.food:
            fi_x = food_item["x"]
            fi_y = food_item["y"]
            self.grid[fi_x][fi_y] = BoardStatus.FOOD

    """
    Places snakes onto the grid
    """
    def initialize_snakes_on_grid(self, snakes):
        for snake in snakes:
            for (x,y) in ((my_body["x"], my_body["y"]) for my_body in snake.my_body):
                self.grid[x][y] = BoardStatus.SNAKE


    """
    Initializes board grid. Wraps around snake and food inits
    """
    def initialize_board_grid(self, snakes):
        self.initialize_food_on_grid()
        self.initialize_snakes_on_grid(snakes)