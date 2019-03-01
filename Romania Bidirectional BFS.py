def is_parent(parent, child):
    for branch in down_romania:
        if branch[0] == parent and branch[1] == child:
            return True
    return False


down_romania = [['Arad', 'Sibiu', 140], ['Arad', 'Timisoara', 118], ['Arad', 'Zerind', 75], ['Sibiu', 'Fagaras', 99],
                ['Sibiu', 'Rimnicu Vilcea', 80], ['Fagaras', 'Bucharest', 211], ['Bucharest', 'Giurgiu', 90],
                ['Bucharest', 'Urziceni', 85], ['Urziceni', 'Hirsova', 98], ['Urziceni', 'Vaslui', 142],
                ['Hirsova', 'Eforie', 86], ['Vaslui', 'Iasi', 92], ['Iasi', 'Neamt', 87],
                ['Rimnicu Vilcea', 'Craiova', 146],
                ['Rimnicu Vilcea', 'Pitesti', 97], ['Craiova', 'Pitesti', 138], ['Pitesti', 'Bucharest', 101],
                ['Timisoara', 'Lugoj', 111], ['Lugoj', 'Mehadia', 70], ['Mehadia', 'Drobeta', 75],
                ['Drobeta', 'Craiova', 120], ['Zerind', 'Oradea', 71], ['Oradea', 'Sibiu', 151]]

up_romania = [['Sibiu', 'Arad', 140], ['Timisoara', 'Arad', 118], ['Zerind', 'Arad', 75], ['Fagaras', 'Sibiu', 99],
              ['Rimnicu Vilcea', 'Sibiu', 80], ['Bucharest', 'Fagaras', 211], ['Giurgiu', 'Bucharest', 90],
              ['Urziceni', 'Bucharest', 85], ['Hirsova', 'Urziceni', 98], ['Vaslui', 'Urziceni', 142],
              ['Eforie', 'Hirsova', 86], ['Iasi', 'Vaslui', 92], ['Neamt', 'Iasi', 87],
              ['Craiova', 'Rimnicu Vilcea', 146],
              ['Pitesti', 'Rimnicu Vilcea', 97], ['Pitesti', 'Craiova', 138], ['Bucharest', 'Pitesti', 101],
              ['Lugoj', 'Timisoara', 111], ['Mehadia', 'Lugoj', 70], ['Drobeta', 'Mehadia', 75],
              ['Craiova', 'Drobeta', 120], ['Oradea', 'Zerind', 71], ['Sibiu', 'Oradea', 151]]

cities = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj',
          'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui',
          'Zerind']

print(cities)
print("please make sure the spelling of city is correct.....\n")
start_city = input("please enter your current city:")
goal_city = input("please enter the destination city:")
print()

down_list = [start_city]
up_list = [goal_city]
new_down_graph = []
new_up_graph = []
goal_found = False
repeated = False
i = 0
j = 0

while goal_found is False:
    if i < len(down_list):
        for branch in down_romania:
            if branch[0] == down_list[i]:
                # check for repetition
                for index in range(len(down_list)):
                    if branch[1] == down_list[index]:
                        repeated = True
                        break
                # append the child in breadth_list
                if repeated is False:
                    down_list.append(branch[1])
                    new_down_graph.append(branch)  #####
                    print("agent_one:", down_list)
                    # check for goal
                    for d in down_list:
                        for u in up_list:
                            if d == u:
                                meeting_city = d
                                goal_found = True
                                break
                        if goal_found:
                            break
                else:
                    repeated = False
        i += 1

    if goal_found:
        break

    if j < len(up_list):
        for branch in up_romania:
            if branch[0] == up_list[j]:
                # check for repetition
                for index in range(len(up_list)):
                    if branch[1] == up_list[index]:
                        repeated = True
                        break
                # append the child in breadth_list
                if repeated is False:
                    up_list.append(branch[1])
                    new_up_graph.append(branch)  #####
                    print("agent_two:", up_list)
                    # check for goal
                    for d in down_list:
                        for u in up_list:
                            if d == u:
                                meeting_city = d
                                goal_found = True
                                break
                        if goal_found:
                            break
                else:
                    repeated = False
        j += 1

    if goal_found:
        break

up_list.reverse()
# print("\n-", down_list, up_list)

# set the path
queue = []
for x in down_list:
    if x == meeting_city:
        break
    else:
        queue.append(x)

s = False
for y in up_list:
    if y == meeting_city:
        s = True
    if s:
        queue.append(y)

path = []
c = queue.pop()
p = queue.pop()
path.append(c)  # append the goal in the path

while len(queue) > 0:
    if is_parent(p, c):
        path.append(p)
        c = p  # to know his parent
    p = queue.pop()  # # calculate the cost of the path

path.append(p)
path.reverse()

total_cost = 0
for c in range(len(path) - 1):
    for b in down_romania:
        if path[c] == b[0] and path[c + 1] == b[1]:
            total_cost += b[2]
            break

print("\nthe Bidirectional BFS path :", path)
print("total cost of path =", total_cost)
