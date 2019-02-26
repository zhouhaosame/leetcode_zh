def f(days:list,costs:list)->int:
    if not days or not list:
        return None
    ans=[]
    def reverse(invalid_day,cost,cur_day_index):
        if cur_day_index>=len(days):
            ans.append(cost)
        else:
            if invalid_day>=days[cur_day_index]:
                reverse(invalid_day,cost,cur_day_index+1)
            else:
                reverse(days[cur_day_index],cost+costs[0],cur_day_index+1)
                reverse(days[cur_day_index]+7-1, cost + costs[1], cur_day_index + 1)
                reverse(days[cur_day_index]+30-1, cost + costs[2], cur_day_index + 1)
    reverse(0,0,0)
    return min(ans)
#时间超出限制了。
days=[1,4,6,7,8,20]
costs=[2,7,15]
print(f(days,costs))