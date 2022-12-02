import timeit
import os
from importlib import import_module

total_solve_time = 0
timeit_repetitions = 10

# generate a list of the folder names in the src/ directory
day_directories = next(os.walk('src/'))[1]
day_directories.sort()

for i, directory in enumerate(day_directories):
    solution = import_module(f'{directory}.solution')
    p1, p2 = solution.solve_p1_and_p2()
    solve_time = timeit.timeit('solution.solve_p1_and_p2()', number=timeit_repetitions, globals=globals())/timeit_repetitions
    total_solve_time += solve_time
    print(f'Day {i+1}, part 1: {p1}')
    print(f'Day {i+1}, part 2: {p2}')
    print(f'Execution time: {solve_time:.3e} s\n')

print(f'Total execution time: {total_solve_time:.3f} s')