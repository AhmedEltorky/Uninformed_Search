def is_parent(parent, child):
    for branch in romania:
        if branch[0] == parent and branch[1] == child:
            return True
    return False


romania = [['Arad', 'Sibiu', 140], ['Arad', 'Timisoara', 118], ['Arad', 'Zerind', 75], ['Sibiu', 'Fagaras', 99],
           ['Sibiu', 'Rimnicu Vilcea', 80], ['Fagaras', 'Bucharest', 211], ['Bucharest', 'Giurgiu', 90],
           ['Bucharest', 'Urziceni', 85], ['Urziceni', 'Hirsova', 98], ['Urziceni', 'Vaslui', 142],
           ['Hirsova', 'Eforie', 86], ['Vaslui', 'Iasi', 92], ['Iasi', 'Neamt', 87], ['Rimnicu Vilcea', 'Craiova', 146],
           ['Rimnicu Vilcea', 'Pitesti', 97], ['Craiova', 'Pitesti', 138], ['Pitesti', 'Bucharest', 101],
           ['Timisoara', 'Lugoj', 111], ['Lugoj', 'Mehadia', 70], ['Mehadia', 'Drobeta', 75],
           ['Drobeta', 'Craiova', 120], ['Zerind', 'Oradea', 71], ['Oradea', 'Sibiu', 151]]

cities = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj',
          'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui',
          'Zerind']

print(cities)
print("please make sure the spelling of city is correct.....\n")
start_city = input("please enter your current city:")
goal_city = input("please enter the destination city:")
print()

breadth_list = [start_city]
new_graph = []
goal_found = False
repeated = False
i = 0

while goal_found is False and i < len(breadth_list):
    for branch in romania:
        if branch[0] == breadth_list[i]:
            # check for repetition
            for index in range(len(breadth_list)):
                if branch[1] == breadth_list[index]:
                    repeated = True
                    break
            # append the child in breadth_list
            if repeated is False:
                breadth_list.append(branch[1])
                new_graph.append(branch) #####
                print(breadth_list)
                # check for goal
                if branch[1] == goal_city:
                    goal_found = True
                    break
            else:
                repeated = False
    i += 1

if goal_found:
    path = []
    c = breadth_list.pop()
    p = breadth_list.pop()
    path.append(c)  # append the goal in the path

    while len(breadth_list) > 0:
        if is_parent(p, c):
            path.append(p)
            c = p  # to know his parent
        p = breadth_list.pop()

    path.append(p)
    path.reverse()
    print("\nthe BFS path is :", path)
    total_cost = 0
    for x in range(len(path) - 1):
        for b in romania:
            if path[x] == b[0] and path[x + 1] == b[1]:
                total_cost += b[2]
                break
    print("total cost of path =", total_cost)
else:
    print("\nthere is no path exist")
