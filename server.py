import logging
import os
import typing

from fastapi import Body, FastAPI, Request
import uvicorn


def run_server(handlers: typing.Dict):
    app = FastAPI(title="Battlesnake")

    @app.get("/")
    def on_info():
        return handlers["info"]()

    @app.post("/start")
    def on_start(game_state: dict = Body(...)):
        handlers["start"](game_state)
        return "ok"

    @app.post("/move")
    def on_move(game_state: dict = Body(...)):
        return handlers["move"](game_state)

    @app.post("/end")
    def on_end(game_state: dict = Body(...)):
        handlers["end"](game_state)
        return "ok"

    @app.middleware("http")
    async def identify_server(request: Request, call_next):
        response = await call_next(request)
        response.headers["server"] = "battlesnake/github/starter-snake-python"
        return response

    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "8000"))

    logging.getLogger("uvicorn.error").setLevel(logging.ERROR)

    print(f"\nRunning Battlesnake at http://{host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="error")