import timeit
from day_1.solution import d1_p1, d1_p2

master_dict = {
    'Part 1':[d1_p1],
    'Part 2':[d1_p2],
    'Time 1':[],
    'Time 2':[],
}

timeit_repetitions = 10

for i,_ in enumerate(master_dict['Part 1']):
    print(f'Day {i+1}, part 1: {master_dict["Part 1"][i]()}')
    print(f'Day {i+1}, part 2: {master_dict["Part 2"][i]()}')
    t1 = timeit.timeit('master_dict["Part 1"][i]()', number=timeit_repetitions, globals=globals())/timeit_repetitions
    t2 = timeit.timeit('master_dict["Part 2"][i]()', number=timeit_repetitions, globals=globals())/timeit_repetitions
    master_dict['Time 1'].append(t1)
    master_dict['Time 2'].append(t2)
    print(f'Execution time: {t1+t2:.3e} s\n')

print(f'Total execution time: {sum(master_dict["Time 1"]) + sum(master_dict["Time 2"]):.3f} s')