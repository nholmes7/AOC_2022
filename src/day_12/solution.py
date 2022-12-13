import numpy as np

data = []
with open('src/day_12/input','r') as file:
    for line in file:
        line_vals = []
        for character in line:
            if character == 'S':
                line_vals.append(0)
            elif character == 'E':
                line_vals.append(27)
            elif character == '\n':
                continue
            else:
                line_vals.append(ord(character)-96)
        data.append(line_vals)

data = np.array(data)

def flood_down(r,c,flooded):
    lowest_point_reached = False
    newly_flooded = np.copy(flooded)
    height = data[r,c]
    
    if not flooded[r,c]:
        return newly_flooded, lowest_point_reached
    
    for coords in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
        if (coords[0] < 0) or (coords[1] < 0):
            continue
        if (coords[0] > len(flooded)-1) or (coords[1] > len(flooded[0])-1):
            continue
        if flooded[coords[0],coords[1]]:
            continue
        if data[coords[0],coords[1]] >= height-1:
            newly_flooded[coords[0],coords[1]] = 1
            if data[coords[0],coords[1]] == 1:
                lowest_point_reached = True

    return newly_flooded, lowest_point_reached

def p1():
    flooded = np.zeros(np.shape(data))
    start_row = np.where(data == 27)[0][0]
    start_col = np.where(data == 27)[1][0]
    end_row = np.where(data == 0)[0][0]
    end_col = np.where(data == 0)[1][0]

    flooded[start_row,start_col] = 1

    path_length = 0
    while True:
        path_length += 1
        prev_state = np.copy(flooded)
        for r, row in enumerate(data):
            for c, col in enumerate(row):
                local_newly_flooded, _ = flood_down(r,c,prev_state)
                flooded = np.logical_or(local_newly_flooded,flooded)
        if flooded[end_row,end_col]:
            break

    return path_length

def p2():
    flooded = np.zeros(np.shape(data))
    start_row = np.where(data == 27)[0][0]
    start_col = np.where(data == 27)[1][0]

    flooded[start_row,start_col] = 1
    path_length = 0
    exit_flag = False
    while True:
        path_length += 1
        prev_state = np.copy(flooded)
        for r, row in enumerate(data):
            for c, col in enumerate(row):
                local_newly_flooded, lowest_point_reached = flood_down(r,c,prev_state)
                if lowest_point_reached:
                    exit_flag = True
                flooded = np.logical_or(local_newly_flooded,flooded)
        if exit_flag:
            break

    return path_length
    

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')