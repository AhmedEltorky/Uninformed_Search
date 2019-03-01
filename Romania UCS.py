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

goal_found = False
possible_solutions = romania.copy()

# initialize the the possible_solution list
for branch in romania:
    if branch[0] != start_city:
        possible_solutions.remove(branch)
print(possible_solutions)

while goal_found is False:
    # finding the minimum cost branch in possible_solutions list
    i = -1
    mini_branch_index = -1
    minimum_cost = 1000
    for mini_branch in possible_solutions:
        i += 1
        if mini_branch[len(mini_branch) - 1] <= minimum_cost:
            minimum_cost = mini_branch[len(mini_branch) - 1]
            mini_branch_index = i

    temp = possible_solutions.pop(mini_branch_index)  ####
    temp_parent = temp[len(temp) - 2]
    # check for goal
    if temp_parent == goal_city:
        temp_mini = temp[len(temp) - 1]
        for check in possible_solutions:
            if check[len(check) - 1] < temp_mini:
                temp_mini = check[len(check) - 1]
                break
        if temp_mini == temp[len(temp) - 1]:
            goal_found = True
            total_cost = temp.pop()
            print("\nthe UCS path is :", temp)
            print("total cost of path =", total_cost)
            break

    save_temp = temp.copy()
    for branch in romania:
        if temp_parent == branch[0]:
            temp_cost = temp.pop()
            temp.append(branch[1])
            temp.append(temp_cost + branch[2])
            possible_solutions.append(temp)
            print(possible_solutions)
            temp = save_temp.copy()
