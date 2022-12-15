data = []
with open('src/day_15/input','r') as file:
    for line in file:
        sensor_pos, beacon_pos = line.split(':')
        sensor_x, sensor_y = sensor_pos.split(',')
        beacon_x, beacon_y = beacon_pos.split(',')
        _, sensor_x = sensor_x.split('=')
        _, sensor_y = sensor_y.split('=')
        _, beacon_x = beacon_x.split('=')
        _, beacon_y = beacon_y.split('=')
        data.append([int(sensor_x),int(sensor_y),int(beacon_x),int(beacon_y)])

def manhattan_distance(p1,p2):
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return abs(p2_x-p1_x) + abs(p2_y-p1_y)

def beacon_free_cols(sensor_pos,beacon_pos,target_row):
    sensor_x, sensor_y = sensor_pos
    beacon_dist = manhattan_distance(sensor_pos,beacon_pos)
    min_col = sensor_x-(beacon_dist-abs(sensor_y-target_row))
    max_col = sensor_x+(beacon_dist-abs(sensor_y-target_row))
    if min_col > max_col:
        return ()
    return min_col, max_col

def invalid_beacon_ranges_in_row(row,data):
    ranges = []
    for pair in data:
        sensor_pos = pair[0:2]
        beacon_pos = pair[2:]
        pair_range = beacon_free_cols(sensor_pos,beacon_pos,row)
        if pair_range != ():
            ranges.append(pair_range)
    return ranges

def find_uncovered_position(ranges):
    for pair1 in ranges:
        no_overlap = True
        _, max1 = pair1
        
        if max1 >= 4000000:
            continue
        
        # check for complete coverage by another range at the top
        # end of the range
        for pair2 in ranges:
            min2, max2 = pair2
            if min2 <= max1+1:
                if max1 < max2:
                    # no other range covers the position immediately
                    # above the top end of the range
                    no_overlap = False
                    break

        if no_overlap:
            missing_val = max1 + 1
            return missing_val

def p1():
    row = 2000000
    invalid_ranges = invalid_beacon_ranges_in_row(row,data)

    # create a set of invalid positions
    invalid_positions = set()
    for invalid_range in invalid_ranges:
        range_min, range_max = invalid_range
        span = range_max - range_min + 1
        invalid_set = set([i+range_min for i in range(span)])
        invalid_positions = invalid_positions.union(invalid_set)
    
    # remove any position that has a beacon on it
    for pair in data:
        beacon_pos = pair[2:]
        if beacon_pos[1] == row:
            if beacon_pos[0] in invalid_positions:
                invalid_positions.remove(beacon_pos[0])

    return len(invalid_positions)

def p2():
    search_rows = 4000000
    for i in range(search_rows):
        invalid_ranges = invalid_beacon_ranges_in_row(i+1,data)
        x_position = find_uncovered_position(invalid_ranges)
        if x_position:
            return x_position*4000000 + i + 1

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')