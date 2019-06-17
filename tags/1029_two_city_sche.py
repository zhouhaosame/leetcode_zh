def twoCitySchedCost(costs) -> int:
    temp = [abs(costs[i][0] - costs[i][1]) for i in range(len(costs))]
    temp_index = [i for i in range(len(temp))]
    temp_index.sort(key = lambda x: temp[x], reverse = True)
    A_list = []
    B_list = []
    for i in range(len(temp_index)):
        if costs[temp_index[i]][0] > costs[temp_index[i]][1] and len(B_list) < len(costs) // 2:
            B_list.append(costs[temp_index[i]][1])
        elif len(A_list)< len(costs) // 2:
            A_list.append(costs[temp_index[i]][0])
        else:
            B_list.append(costs[temp_index[i]][1])
    print(A_list)
    print(B_list)
    return sum(A_list + B_list)
a=[[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
print(twoCitySchedCost(a))