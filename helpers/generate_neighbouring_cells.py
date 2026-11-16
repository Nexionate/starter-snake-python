# Takes in a dict of a position and returns its cardinal neighbours 
def generate_neighbouring_cells(position_dict, board_width, board_height):
    neighbouring_cells = [
        {"x": position_dict["x"], "y": position_dict["y"] + 1},  # Up
        {"x": position_dict["x"], "y": position_dict["y"] - 1},  # Down
        {"x": position_dict["x"] - 1, "y": position_dict["y"]},  # Left
        {"x": position_dict["x"] + 1, "y": position_dict["y"]}   # Right
    ]

    filtered_list = []
    for i in range(len(neighbouring_cells)):
        i_x = neighbouring_cells[i]["x"]
        i_y = neighbouring_cells[i]["y"]
        if not (i_x < 0 or i_x >= board_width or i_y < 0 or i_y >= board_height):
            filtered_list.append(neighbouring_cells[i])
            
    return filtered_list