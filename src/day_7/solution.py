class computer_obj:
    def __init__(self, obj_type, name, obj_size, loc):
        self.obj_type = obj_type
        self.name = name
        self.obj_size = obj_size
        self.loc = loc

def parse_cd(arg, current_loc):
    if arg == '/':
        return '/'
    if arg == '..':
        while True:
            current_loc = current_loc[:-1]
            if current_loc[-1] == '/':
                return current_loc
    return current_loc + arg + '/'

def parse_input():
    things = []
    current_loc = ''
    unique_locs = set()
    with open('src/day_7/input','r') as file:
        for line in file:
            # command
            if line[0:4] == '$ cd':
                current_loc = parse_cd(line[5:-1], current_loc)
                unique_locs.add(current_loc)

            elif line[0:4] == '$ ls':
                next
            
            # directory
            elif line[:3] == 'dir':
                things.append(computer_obj('dir',line[4:-1],0,current_loc))
            
            # file
            else:
                file_size, name = line[:-1].split(' ')
                things.append(computer_obj('file',name,int(file_size),current_loc))
    return things, unique_locs

def find_size(loc, things):
    size = 0
    for thing in things:
        if thing.loc == loc:
            if thing.obj_type == 'dir':
                size += find_size(loc + thing.name + '/', things)
            size += thing.obj_size
    return size

def p1():
    things, unique_locs = parse_input()
    total_size = sum([find_size(loc, things) for loc in unique_locs if find_size(loc, things) <= 100000])
    return total_size
    

def p2():    
    things, unique_locs = parse_input()
    size_list = [find_size(loc, things) for loc in unique_locs]
    size_list.sort()
    for dir_size in size_list:
        if (size_list[-1] - dir_size) < (70000000-30000000):
            return dir_size

def solve_p1_and_p2():
    return p1(), p2()

if __name__ == "__main__":
    print(f'Part 1: {p1()}')
    print(f'Part 2: {p2()}')