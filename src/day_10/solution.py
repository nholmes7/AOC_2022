
data = []
with open('src/day_10/input','r') as file:
    for line in file:
        command = line[:4]
        if command == 'noop':
            data.append([command])
            continue
        value = int(line[4:])
        data.append([command,value])

def determine_register_X_state():
    register_X = [1]
    add_value = 0
    for instruction in data:
        register_X.append(register_X[-1]+add_value)
        add_value = 0
        if instruction[0] != 'noop':
            register_X.append(register_X[-1])
            add_value = instruction[1]
    
    return register_X

def p1():
    register_X = determine_register_X_state()
    signal_strength = [i*register_X[i] for i in [20,60,100,140,180,220]]
    
    return sum(signal_strength)

def p2():
    register_X = determine_register_X_state() 
    counter = 0
    screen_width = 40
    screen_height = 6
    screen_strings = []
    for i in range(screen_height):
        line_string = ''
        for j in range(screen_width):
            counter += 1
            sprite_position = register_X[counter]
            current_position = counter-40*i-1
            if abs(sprite_position - current_position) <= 1:
                line_string += '#'
            else:
                line_string += ' '
        screen_strings.append(line_string)

    answer = '\n'
    for row in screen_strings:
        answer += row + '\n'
    return answer

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')