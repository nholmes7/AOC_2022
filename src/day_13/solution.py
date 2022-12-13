import ast
import copy

def compare(input1,input2,future_inputs1=[],future_inputs2=[]):
    if len(input1) == 0 and len(input2) == 0:
        return compare(future_inputs1.pop(0),future_inputs2.pop(0),future_inputs1,future_inputs2)
    if len(input1) == 0:
        return True
    if len(input2) == 0:
        return False
    new_input1 = input1.pop(0)
    new_input2 = input2.pop(0)
    future_inputs1.insert(0,input1)
    future_inputs2.insert(0,input2)
    if type(new_input1) == int and type(new_input2) == int:
        if new_input1 == new_input2:
            return compare(future_inputs1.pop(0),future_inputs2.pop(0),future_inputs1,future_inputs2)
        return new_input1<new_input2
    if type(new_input1) == list and type(new_input2) == list:
        return compare(new_input1,new_input2,future_inputs1,future_inputs2)
    if type(new_input1) == list:
        return compare(new_input1,list([new_input2]),future_inputs1,future_inputs2)
    if type(new_input2) == list:
        return compare(list([new_input1]),new_input2,future_inputs1,future_inputs2)

def p1():
    data = [[]]
    with open('src/day_13/input','r') as file:
        for line in file:
            if line == '\n':
                data.append([])
                continue
            data[-1].append(ast.literal_eval(line[:-1]))
    
    indicies = []

    for i, pair in enumerate(data):
        if compare(pair[0],pair[1]):
            indicies.append(i+1)

    return sum(indicies)

def p2():
    data = []
    with open('src/day_13/input','r') as file:
        for line in file:
            if line == '\n':
                continue
            data.append(ast.literal_eval(line[:-1]))
    data.append([[6]])
    data.append([[2]])

    sorted = []

    # naive sorting algorithm
    for i, item in enumerate(data):
        if i == 0:
            sorted.append(item)
            continue
        item_added = False
        for j, sorted_item in enumerate(sorted):
            # we have to make deepcopies here to avoid modifying
            # item and sorted item in the compare function
            item_copy = copy.deepcopy(item)
            sorted_item_copy = copy.deepcopy(sorted_item)
            if compare(sorted_item_copy,item_copy):
                sorted.insert(j,item)
                item_added = True
                break
        # catch if it should go at the end of the list
        if not item_added:
            sorted.append(item)
    sorted.reverse()

    return (sorted.index([[6]])+1)*(sorted.index([[2]])+1)

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')