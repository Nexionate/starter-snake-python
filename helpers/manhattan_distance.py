"""
Return the manhattan distance between two points stored as dicts with keys x and y
"""

def manhattan_distance(p1: dict, p2: dict):
    m_x = abs(p2["x"] - p1["x"])
    m_y = abs(p2["y"] - p1["y"])
    return m_x + m_y