# When a snake is created in the snakes list, it's index is passed in

class Snake:
    def __init__(self, head, body, health, index):
        self.my_head = head
        self.my_body = body
        self.health = health
        self.has_eaten_this_turn = False
        self.id = index
    
    
