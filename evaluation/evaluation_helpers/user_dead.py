from classes.state import State

"""
Return 1 if user is dead
Return 0 if neither
"""
def user_dead(state: State):
    if state.did_user_die == True:
        return True
    else:
        return False