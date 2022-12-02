translation = {
    'A': 1,
    'B': 2,
    'C': 3,
}

outcome_score = {
    1: 6,
    0: 3,
    -1: 0,
}

# takes player 1 and player 2 selections (options are 1, 2, or 3)
# returns -1 for loss, 0 for tie, 1 for win
def play_game(p1, p2):
    diff = p1-p2
    outcome = 1.5*diff - 0.5*pow(diff,3)
    return outcome

def p1():
    translation.update({
        'X': 1,
        'Y': 2,
        'Z': 3,
    })

    score = 0

    with open('src/day_2/input', 'r') as file:
        for line in file:
            elf = translation[line[0]]
            me = translation[line[2]]
            outcome = play_game(me, elf)
            score += me + outcome_score[outcome]
    
    return score

def p2():
    translation.update({
        'X': -1,
        'Y': 0,
        'Z': 1,
    })

    score = 0

    with open('src/day_2/input', 'r') as file:
        for line in file:
            elf = translation[line[0]]
            outcome = translation[line[2]]
            for play in [1, 2, 3]:
                test_outcome = play_game(play, elf)
                if test_outcome == outcome:
                    break
            score += play + outcome_score[outcome]

    return score

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')