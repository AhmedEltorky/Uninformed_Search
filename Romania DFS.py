romania = [['Arad', 'Sibiu', 140], ['Arad', 'Timisoara', 118], ['Arad', 'Zerind', 75], ['Sibiu', 'Fagaras', 99],
           ['Sibiu', 'Rimnicu Vilcea', 80], ['Fagaras', 'Bucharest', 211], ['Bucharest', 'Urziceni', 85],
           ['Bucharest', 'Giurgiu', 90], ['Urziceni', 'Vaslui', 142], ['Urziceni', 'Hirsova', 98],
           ['Hirsova', 'Eforie', 86], ['Vaslui', 'Iasi', 92], ['Iasi', 'Neamt', 87], ['Rimnicu Vilcea', 'Pitesti', 97],
           ['Rimnicu Vilcea', 'Craiova', 146], ['Craiova', 'Pitesti', 138], ['Pitesti', 'Bucharest', 101],
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

test_graph = romania.copy()
path = [start_city]
goal_found = False

while len(test_graph) > 0 and goal_found is False:
    change_flag = False
    for branch in test_graph:
        if branch[0] == path[-1]:  # path[len(path) - 1] ==> means the last element of the path
            if branch[1] == goal_city:
                path.append(branch[1])
                goal_found = True
                break
            else:
                change_flag = True
                path.append(branch[1])
                test_graph.remove(branch)
                print(path)
    if goal_found is True:
        break
    if change_flag is False:  # when reaching to the leaf node and does not find the goal == means there is no more children
        path.pop()

if goal_found is True:
    print("\nthe DFS path is :", path)
    total_cost = 0
    for x in range(len(path) - 1):
        for b in romania:
            if path[x] == b[0] and path[x + 1] == b[1]:
                total_cost += b[2]
                break
    print("total cost of path =", total_cost)
else:
    print("\nthere is no path exist")
