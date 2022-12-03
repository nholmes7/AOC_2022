def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

priority_map = {c: i+1 for i, c in enumerate(char_range('a','z'))}
priority_map.update({c: i+27 for i, c in enumerate(char_range('A','Z'))})

def p1():
    items = []
    with open('src/day_3/input', 'r') as file:
        for line in file:
            # print(type(line))
            length = len(line)-1
            half_1 = line[:int(length/2)]
            half_2 = line[int(length/2):]
            for item in half_1:
                if item in half_2:
                    items.append(item)
                    break

    answer = sum([priority_map[item] for item in items])

    return answer

def p2():
    items = []
    group = []
    with open('src/day_3/input', 'r') as file:
        for line in file:
            group.append(line)
            if len(group) == 3:
                e1, e2, e3 = group
                for item in e1:
                    if item in e2:
                        if item in e3:
                            items.append(item)
                            break
                group = []

    answer = sum([priority_map[item] for item in items])

    return answer

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')