with open('input.txt') as f:
    input = f.readlines()

def input_parameters_extractor(input):
    Landscape = input[2:22]
    Landscape = [s.replace("  ", " x ") for s in Landscape]
    result = []
    len_line = len(Landscape[0].split())

    j = 0
    i = 0
    x = i
    y = i + 4
    subresult = []

    for j in range(0, len_line, 4):
        x = 0
        y = 4
        for k in range(5):
            subresult = []
            for i in range(x,y):
                try :
                    values = Landscape[i].strip().split()[j:j+4]
                    subresult.append(values)
                except :
                    print(x,y)
            result.append(subresult)
            y = y + 4
            x = x + 4
            
    Landscape = result
    Tiles = input[23:25][1]
    Tiles = Tiles.strip('{|}|\n|').split(', ')

    Tiles_Dic = {}
    Tiles_Dic[Tiles[0].split('=')[0]] = Tiles[0].split('=')[1]
    Tiles_Dic[Tiles[1].split('=')[0]] = Tiles[1].split('=')[1]
    Tiles_Dic[Tiles[2].split('=')[0]] = Tiles[2].split('=')[1]
    Tiles = Tiles_Dic

    Targets = input[27:31]
    Targets_Dic = {}
    for line in Targets:
        lines = line.strip('\n').split(':')
        Targets_Dic[lines[0]] = lines[1]

    Targets = {}
    i = 1
    for element in Targets_Dic.values():
        Targets[i] = int(element)
        i = i + 1

    Solution_Key = input[36::]

    return Landscape, Tiles, Targets, Solution_Key


Landscape, Tiles, Targets, Solution_Key = input_parameters_extractor(input)

def check_target(current_state,path):

    diff = {}
    for key in Targets:
        if key in current_state:
            diff[key] = Targets[key] - current_state[key]
    
    if (path.count('L_shape') > int(Tiles['EL_SHAPE'])) or (path.count('Full_block') > int(Tiles['FULL_BLOCK'])) or  (path.count('Outer_block') > int(Tiles['OUTER_BOUNDARY'])):
        return 'tile_count_not_matching'

    if all(value == 0 for value in diff.values()):
        return 'reached'
    
    if min(diff.values()) < 0:
        return 'greater'
    
    return None

def Full_block(var):
    res = {}
    count_1=0
    count_2=0
    count_3=0
    count_4=0
    res[1] = count_1
    res[2] = count_2 
    res[3] = count_3
    res[4] = count_4
    return res

def Outer_block(var):
    res = {}
    count_1=sum(sublist[1:3].count('1') for sublist in var[1:3])
    count_2=sum(sublist[1:3].count('2') for sublist in var[1:3])
    count_3=sum(sublist[1:3].count('3') for sublist in var[1:3])
    count_4=sum(sublist[1:3].count('4') for sublist in var[1:3])
    res[1] = count_1
    res[2] = count_2 
    res[3] = count_3
    res[4] = count_4
    return res

def L_shape(var):
    res = {}
    count_1=sum(sublist[1:].count('1') for sublist in var[1:])
    count_2=sum(sublist[1:].count('2') for sublist in var[1:])
    count_3=sum(sublist[1:].count('3') for sublist in var[1:])
    count_4=sum(sublist[1:].count('4') for sublist in var[1:])
    res[1] = count_1
    res[2] = count_2 
    res[3] = count_3
    res[4] = count_4
    return res

functions = [L_shape, Outer_block, Full_block]
path = []
roadmap = []

def apply_function(funct, area):
    return funct(area)

def csp_solver(current_index, current_sum, path, roadmap, functions, Landscape):
    
    if current_index == len(Landscape):

        if check_target(current_sum,path) == 'reached':            
            return True
        else:
            return False
    else:
        # MRV implementation
        unassigned_functions = [f for f in functions]
        unassigned_functions = sorted(unassigned_functions, key=lambda f: len([v for v in f(Landscape[current_index]).values() if v > 0]))
        for func in unassigned_functions:

            path.append(func.__name__)
            applied_area = apply_function(func, Landscape[current_index])

            sum_dict = {}
            for key in applied_area:
                if key in current_sum:
                    sum_dict[key] = current_sum[key] + applied_area[key]
            
            # Check if the current sum is greater than the target
            if check_target(sum_dict, path) == 'greater':
                path.pop()
                continue
            
            if check_target(sum_dict, path) == 'tile_count_not_matching':
                path.pop()
                continue

            current_sum_total = sum_dict
                      
            result = csp_solver(current_index + 1, current_sum_total, path, roadmap, functions, Landscape)
            if result:
                roadmap.append(f' The index : {current_index}, Area : {Landscape[current_index]}, Applied Shape : {func.__name__}, Applied shape result  : {current_sum_total} \n') 
                return True
            else:
                path.pop()

        return False


result = csp_solver(0, {1:0, 2:0, 3:0, 4:0}, path, roadmap, functions, Landscape)
if result:
    for i in range(0, len(roadmap)):
        try :
            print(roadmap[len(roadmap) - i - 1])
        except:
            print('error', i)
    print('\n')
    print( 'Tiles Used Counts :' , 'L shape count :' , path.count('L_shape'), 'Full block count :' , path.count('Full_block'), 'Outer block count :' , path.count('Outer_block'))
    print('\n')
    print("Path found:", path)
    print('\n')
else:
    print("No path found.")