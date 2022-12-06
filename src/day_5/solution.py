def parse_input():
    with open('src/day_5/input', 'r') as file:
        data = file.readlines()

    split_loc = data.index('\n')

    # find the crate data
    crate_data = data[:split_loc]

    # find the instructions, and convert them to a nested list
    instructions = data[split_loc+1:]
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

    # find the number of stacks to parse
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

def p1():
    crate_info, instructions = parse_input()

    for instruction in instructions:
        repeats = instruction[0]
        from_pos = instruction[1]-1
        dest_pos = instruction[2]-1
        for i in range(repeats):
            crate_info[dest_pos].append(crate_info[from_pos].pop())

    answer = ''
    for stack in crate_info:
        answer += stack[-1]

    return answer

def p2():
    crate_info, instructions = parse_input()
    
    for instruction in instructions:
        repeats = instruction[0]
        from_pos = instruction[1]-1
        dest_pos = instruction[2]-1
        temp = []
        for i in range(repeats):
            temp.append(crate_info[from_pos].pop())
        temp.reverse()
        crate_info[dest_pos] += temp

    answer = ''
    for stack in crate_info:
        answer += stack[-1]

    return answer

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')