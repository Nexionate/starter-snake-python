"""
Takes in the shape of the array and the default value
Shape an array of lengths for each dimension. To create a 1x2x3x4, pass [1,2,3,4]
Return the n_dimensional list
"""

def create_n_dimensional_list(shape, default_value=None):
    if not shape:
        return default
    return [make_nd_list(shape[1:], default) for _ in range(shape[0])]