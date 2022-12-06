def parse_input():
    with open('src/day_5/input', 'r') as file:
        data = file.readlines()

    # find the point where the file stops describing the crate positions
    # and switches to moving instructions
    split_loc = data.index('\n')

    # find the crate data
    crate_data = data[:split_loc]

    # find the instructions
    instructions = data[split_loc+1:]
    # split the instructions into a nested list
    vals = []
    for instruction in instructions:
        val_group = []
        for i in instruction.split(' '):
            try:
                val_group.append(int(i))
            except ValueError:
                pass
        vals.append(val_group)

    instructions = vals

    # find the number of stacks to parse - this is the last number
    # in the line before where the file is split
    stacks = crate_data[-1].split(' ')
    stacks.reverse()
    for index in stacks:
        try:
            num = int(index)
            break
        except ValueError:
            pass

    stacks = num

    # convert the crate stack data into a nested list
    crate_info = [[] for i in range(stacks)]
    for i in range(split_loc-1):
        line = crate_data[split_loc-2-i]
        for j in range(stacks):
            crate_label = line[1 + j*4]
            if crate_label != ' ':
                crate_info[j].append(crate_label)
    
    return crate_info, instructions

def generate_answer(crate_stacks):
    answer = ''
    for stack in crate_stacks:
        answer += stack[-1]
    return answer

def p1():
    crate_info, instructions = parse_input()

    for instruction in instructions:
        repeats = instruction[0]
        from_pos = instruction[1]-1
        dest_pos = instruction[2]-1
        for _ in range(repeats):
            crate_info[dest_pos].append(crate_info[from_pos].pop())

    return generate_answer(crate_info)

def p2():
    crate_info, instructions = parse_input()

    for instruction in instructions:
        repeats = instruction[0]
        from_pos = instruction[1]-1
        dest_pos = instruction[2]-1
        temp = []
        for _ in range(repeats):
            temp.append(crate_info[from_pos].pop())
        temp.reverse()
        crate_info[dest_pos] += temp

    return generate_answer(crate_info)

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')