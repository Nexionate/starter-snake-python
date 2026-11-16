from classes.state import State

def user_win(state: State):
    if not state.did_user_die == True and len(state.snakes) == 1:
        return 1
    else:
        return 0