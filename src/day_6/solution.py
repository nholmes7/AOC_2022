def find_start_char(buffer_size):
    with open('src/day_6/input','r') as file:
        input = file.readline()

    buffer = []
    for i, char in enumerate(input):
        buffer.append(char)
        if len(buffer) > buffer_size:
            buffer.pop(0)
        unique_vals = set(buffer)
        if len(unique_vals) == buffer_size:
            return i + 1

def p1():
    answer = find_start_char(4)
    return answer

def p2():    
    answer = find_start_char(14)
    return answer

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')