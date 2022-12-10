instructions = []

with open('src/day_9/input','r') as file:
    for line in file:
        direction = line[0]
        magnitude = int(line[2:-1])
        instructions.append([direction,magnitude])

def move_head(instruction,segment_positions, tail_position_tracker):
    direction, magnitude = instruction
    for _ in range(magnitude):
        # move the head
        if direction == 'R':
            segment_positions[0][0] += 1
        if direction == 'L':
            segment_positions[0][0] -= 1
        if direction == 'U':
            segment_positions[0][1] += 1
        if direction == 'D':
            segment_positions[0][1] -= 1

        # move the trailing segments
        for i, _ in enumerate(segment_positions):
            if i == 0:
                continue
            segment_positions[i] = move_trailing_segment(segment_positions[i-1],segment_positions[i])

        # update set of tail positions
        tail_position_tracker.add(f'{segment_positions[-1][0]},{segment_positions[-1][1]}')

    return segment_positions, tail_position_tracker

def move_trailing_segment(head_pos,tail_pos):
    tail_delta = [p1-p2 for p1, p2 in zip(head_pos,tail_pos)]
    
    # if trailing segment isn't more than 1 away in either dimension - return
    if max([abs(i) for i in tail_delta]) <= 1:
        return tail_pos

    # move the trailing segment
    for i, delta in enumerate(tail_delta):
        if delta < 0:
            tail_pos[i] -= 1
        elif delta > 0:
            tail_pos[i] += 1

    return tail_pos

def find_unique_tail_positions(rope_length):
    segment_positions = [[0,0] for _ in range(rope_length)]
    tail_position_tracker = set(['0,0'])

    for instruction in instructions:
        segment_positions, tail_position_tracker = move_head(instruction, segment_positions, tail_position_tracker)

    return len(tail_position_tracker)

def p1():
    return find_unique_tail_positions(2)

def p2():    
    return find_unique_tail_positions(10)

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')