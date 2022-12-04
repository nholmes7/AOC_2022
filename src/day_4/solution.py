def generate_section_set(range_string):
    lb, ub = range_string.split('-')
    lb = int(lb)
    ub = int(ub)
    section_set = {i for i in range(lb, ub+1)}
    return section_set

def p1():
    answer = 0

    with open('src/day_4/input', 'r') as file:
        for line in file:
            elf1, elf2 = line.split(',')
            elf1 = generate_section_set(elf1)
            elf2 = generate_section_set(elf2)
            combined_set = elf1.union(elf2)
            if len(combined_set) == max(len(elf1),len(elf2)):
                answer += 1

    return answer

def p2():
    answer = 0

    with open('src/day_4/input', 'r') as file:
        for line in file:
            elf1, elf2 = line.split(',')
            elf1 = generate_section_set(elf1)
            elf2 = generate_section_set(elf2)
            combined_set = elf1.union(elf2)
            if len(combined_set) != (len(elf1) + len(elf2)):
                answer += 1

    return answer

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')