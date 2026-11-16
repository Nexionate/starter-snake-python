from enum import Enum
from helpers.generate_neighbouring_cells import generate_neighbouring_cells
from classes.snake import Snake
from classes.board import Board, BoardStatus
from enums.moves import Move


# TO DO: When snake array is created, make sure the user's snake is always at index 0





# TO DO: Set did_user_die if our snake is dead
class State:
    def __init__(self, snakes, board):
        self.snakes = snakes
        self.board = board
        self.death_count = 0
        self.did_user_die = False
        self.initlialize_board()

    # add all snakes positions to the board
    def initlialize_board(self):
        self.board.initialize_board_grid(self.snakes)


    

    def check_out_of_bounds(self, snake, move):
        s_x = snake.my_head["x"]
        s_y = snake.my_head["y"]
        if move == Move.RIGHT:
            s_x += 1
        elif move == Move.LEFT:
            s_x -= 1
        elif move == Move.UP:
            s_y += 1 
        elif move == Move.DOWN:
            s_y -= 1
        
        if s_x < 0 or s_x >= self.board.width or s_y < 0 or s_y >= self.board.height:
            self.snakes.remove(snake)
            self.board.update_dead_snake(snake)
            self.death_count += 1
            if (snake.id == 0):
                self.did_user_die = True
            return True
        return False


    # assume snake1 is us
    # When a snake dies, update snake list, update board.grid, update did_user_die, update dead_count
    # When removing two snakes from the list, remove US FIRST, then the OTHER AFTERWARDS
    def handle_collision(self, snake1, snake2):
        # Head-to-head is decided by length, not health
        if len(snake1.my_body) > len(snake2.my_body):
            self.snakes.remove(snake2)
            self.board.update_dead_snake(snake2)
            self.death_count += 1
            if (snake2.id == 0):
                self.did_user_die = True
            return True
        
        elif len(snake1.my_body) == len(snake2.my_body):
            self.snakes.remove(snake1)
            self.snakes.remove(snake2)
            self.board.update_dead_snake(snake1)
            self.board.update_dead_snake(snake2)
            self.death_count += 2
            if (snake2.id == 0 or snake1.id == 0):
                self.did_user_die = True
            return False
        
        elif len(snake1.my_body) < len(snake2.my_body):
            self.snakes.remove(snake1)
            self.board.update_dead_snake(snake1)
            self.death_count += 1
            if (snake1.id == 0):
                self.did_user_die = True
            return False


    def move_then_check_for_head(self, snake, move):
        s_x = snake.my_head["x"]
        s_y = snake.my_head["y"]
        if move == Move.RIGHT:
            s_x += 1
        elif move == Move.LEFT:
            s_x -= 1
        elif move == Move.UP:
            s_y += 1 
        elif move == Move.DOWN:
            s_y -= 1
        target = {"x": s_x, "y": s_y}
        # Only snakes that already moved this turn (lower id) can be head-to-head with us,
        # and only if they landed on the exact cell we're moving into
        for opp_snake in list(self.snakes):
            if opp_snake.my_head == target and opp_snake.id < snake.id:
                did_we_survive = self.handle_collision(snake, opp_snake)
                if did_we_survive == False:
                    return False

        return True
                
        
        

        
    def check_food_collision(self, snake):
        # snake.my_head is already updated to the new position
        s_x = snake.my_head["x"]
        s_y = snake.my_head["y"]

        if self.board.grid[s_x][s_y] == BoardStatus.FOOD:
            self.board.update_eaten_food(snake)
            snake.health = 100
            return True
        return False

    def check_body_collision(self, snake, move):
        s_x = snake.my_head["x"]
        s_y = snake.my_head["y"]
        if move == Move.RIGHT:
            s_x += 1
        elif move == Move.LEFT:
            s_x -= 1
        elif move == Move.UP:
            s_y += 1 
        elif move == Move.DOWN:
            s_y -= 1

        if self.board.grid[s_x][s_y] in (BoardStatus.EMPTY, BoardStatus.FOOD):
            return True
        elif self.board.grid[s_x][s_y] == BoardStatus.SNAKE:
            self.snakes.remove(snake)
            self.board.update_dead_snake(snake)
            self.death_count += 1
            if snake.id == 0:
                self.did_user_die = True
            return False

    def perform_move(self, snake_id, move):
        # Look the snake up by id; it may have already died this turn
        snake = next((s for s in self.snakes if s.id == snake_id), None)
        if snake is None:
            return
        if not self.check_out_of_bounds(snake, move):
            # Head-to-head runs before the body check, otherwise landing on an
            # already-moved snake's new head is wrongly treated as a body collision
            if self.move_then_check_for_head(snake, move):
                if self.check_body_collision(snake, move):
                    head = snake.my_body[0]
                    tail = snake.my_body[-1]
                    s_x = head["x"]
                    s_y = head["y"]

                    if move == Move.RIGHT:
                        s_x += 1
                    elif move == Move.LEFT:
                        s_x -= 1
                    elif move == Move.UP:
                        s_y += 1 
                    elif move == Move.DOWN:
                        s_y -= 1

                    new_head = {"x": s_x, "y": s_y}
                    snake.my_body.insert(0, new_head)
                    snake.my_head = new_head

                    if not self.check_food_collision(snake):
                        # Pass [tail] as a list since update_any_tile_empty iterates over entity
                        self.board.update_any_tile_empty([tail])
                        snake.my_body.pop()

                    self.board.update_board_with_snakes([snake])
                        
                        
                        
                
        
        

        






































    # # removes the dead snake from the board
    # def cleanup(self, snake_index):
    #     self.board.update_dead_snake(self.snakes[snake_index].body)
    #     self.death_count += 1
    #     return Status.DYING

    # def collision_with_head(self, snake_index):
    #     our_snake = self.snakes[0].my_head        
    #     neighbouring_cells = generate_neighbouring_cells(our_snake)


        
    #     for opp_head, opp_snake_index in zip([snake.head for snake in self.snakes], range(len(self.snakes))):
    #         if opp_head in neighbouring_cells:
    #             # Suggest helper to handle head-on collisions. Not implemented yet
    #             opp_snake = self.snakes[opp_snake_index]
    #             if our_snake.health > opp_snake.health:
    #                 self.cleanup(opp_snake_index)
    #                 return Status.ALIVE
    #             elif our_snake.health == opp_snake.health:
    #                 self.cleanup(opp_snake_index)
    #                 self.cleanup(self.snakes[0])
    #             elif our_snake.health < opp_snake.health:
    #                 self.cleanup(opp_snake_index)
                    

            

    

    # def collision_with_body(self, snake_index):
    #     # check to the right of the head for other snakes
    #     if self.board.check_if_board_position_snake(self.snakes[snake_index].my_head["x"] + 1, self.snakes[snake_index].my_head["y"]):
    #         self.cleanup(snake_index)

    #     # check to the left of the head for other snakes
    #     if self.board.check_if_board_position_snake(self.snakes[snake_index].my_head["x"] - 1, self.snakes[snake_index].my_head["y"]):
    #         self.cleanup(snake_index) 
        
    #     # check to the uppies of the head for other snakes
    #     if self.board.check_if_board_position_snake(self.snakes[snake_index].my_head["x"], self.snakes[snake_index].my_head["y"] + 1):
    #         self.cleanup(snake_index)

    #     # check to the downies of the head for other snakes
    #     if self.board.check_if_board_position_snake(self.snakes[snake_index].my_head["x"], self.snakes[snake_index].my_head["y"] - 1):
    #         self.cleanup(snake_index)


    # def head_out_of_bounds(self, snake_index):
    #     if self.snakes[snake_index].my_head["x"] + 1 > self.board["width"]:
    #         self.cleanup(snake_index) 
    #     if self.snakes[snake_index].my_head["x"] - 1 > self.board["width"]:
    #         self.cleanup(snake_index)
    #     if self.snakes[snake_index].my_head["y"] + 1 > self.board["height"]:
    #         self.cleanup(snake_index)
    #     if self.snakes[snake_index].my_head["y"] - 1 > self.board["height"]:
    #         self.cleanup(snake_index)

         
    # # resets the bool back to false at the start of every round
    # def perform_safety_checks (self, snake_index):
    #     for snake in self.snakes:
    #         snake.has_eaten_this_turn = False

    #     self.head_out_of_bounds(snake_index)

    #     self.collision_with_head(snake_index)
    #     self.collision_with_body(snake_index)
    #     return Status.ALIVE

    
    # def snake_eaten_food(self, snake_index):
    #     if self.board.check_if_board_position_food(self.snakes[snake_index].my_head["x"], self.snakes[snake_index].my_head["y"]):
    #         self.snakes[snake_index].has_eaten_this_turn = True
    #         self.board.update_eaten_food(self.snakes[snake_index].my_head["x"], self.snakes[snake_index].my_head["y"])
    #         return Status.FOOD


    # def perform_move(self, snake_index, move):
    #     #self.perform_safety_checks
    #     #update board and snakes
    #     #if snake is still alive, update health
        


