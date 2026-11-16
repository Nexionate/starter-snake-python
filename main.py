
import random
import typing
from classes.board import Board
from classes.snake import Snake
from classes.state import State
from search_moves.get_move import get_move
from enums.moves import Move


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")







# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:
    # Create the snakes list
    you = game_state["you"]
    others = [s for s in game_state["board"]["snakes"] if s["id"] != you["id"]]

    all_snakes = [
        Snake(s["head"], s["body"], s["health"], index)
        for index, s in enumerate([you] + others)
    ]
    
    
    # Create the board
    game_board = Board(game_state["board"]["width"], game_state["board"]["height"], game_state["board"]["food"])
    # Create State
    game_state = State(all_snakes, game_board)
    # call get_move()
    next_move, score = get_move(game_state)
    # Log and return the move
    print(f"Performing move {next_move.name} with expected score {score}")
    
    if next_move == Move.UP:
        return {"move": "up"}
    elif next_move == Move.DOWN:
        return {"move": "down"}
    elif next_move == Move.LEFT:
        return {"move": "left"}
    else:
        return {"move": "right"}

# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
    
