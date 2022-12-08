import numpy as np

def determine_visibility(input):
    rows, columns = input.shape
    for row, row_vals in enumerate(input):
        row_max = -1
        for column, column_val in enumerate(row_vals):
            if column == 0:
                row_max = column_val
                continue
            if column_val > row_max:
                row_max = column_val
            input[row,column] = row_max

    offset_input = input[:,:columns-1]
    offset_input = np.insert(offset_input, obj=0, values=-1, axis=1)
    visibility = (input - offset_input) > 0

    return visibility

def define_views(r,c,data):
    right = data[r,c+1:]
    up = np.flip(data[:r,c])
    down = data[r+1:,c]
    left = np.flip(data[r,:c])
    return [right,up,down,left]

def calculate_view_score(r,c,data):
    house_height = data[r,c]
    views = define_views(r,c,data)
    view_score = 1
    for direction in views:
        if len(direction) == 0:
            return 0
        if len(set(direction)) == 1:
            if direction[0] <= house_height:
                view_score *= len(direction)
                continue
        if max(direction) < house_height:
            view_score *= len(direction)
            continue
        for i, tree_height in enumerate(direction):
            if tree_height >= house_height:
                view_score *= i + 1
                break
    return view_score

def p1():
    data = np.genfromtxt('src/day_8/input',delimiter=1)
    boolean_arrays = []

    for i in range(4):
        input = np.copy(data)
        # rotate the input array
        for _ in range(i):
            input = np.rot90(input)

        visibility = determine_visibility(input)

        # rotate the array back to the original
        if i != 0:
            for _ in range(4-i):
                visibility = np.rot90(visibility)

        boolean_arrays.append(visibility)

    # logical OR to compare all boolean arrays
    answer = np.zeros(data.shape)
    for visibility in boolean_arrays:
        answer = np.logical_or(answer,visibility)

    return np.count_nonzero(answer)

def p2():    
    data = np.genfromtxt('src/day_8/input',delimiter=1)

    view_scores = []
    for row, row_vals in enumerate(data):
        for column, column_val in enumerate(row_vals):
            view_scores.append(calculate_view_score(row,column,data))

    return max(view_scores)

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')