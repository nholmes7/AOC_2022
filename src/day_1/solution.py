def calculate_elf_cals():
    elves = []
    calorie_counter = 0

    with open('src/day_1/input', 'r') as file:
        for line in file:
            try:
                item_cal = int(line)
                calorie_counter += item_cal
            except ValueError:
                elves.append(calorie_counter)
                calorie_counter = 0
    
    return elves

def p1():
    elves = calculate_elf_cals()
    return max(elves)

def p2():
    elves = calculate_elf_cals()
    elves.sort()
    return sum(elves[-3:])

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')