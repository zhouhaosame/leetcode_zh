class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
def graph_solve(intervals):
    def init_intervals(intervals):
        intervals=[Interval(s[0],s[1]) for s in intervals]
        return intervals
    import collections
    def overlap(a, b):
        return a.start <= b.end and b.start <= a.end

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):#因为是无向图，所以，j从i+1之后
                if overlap(interval_i, intervals[j]):
                    graph[interval_i].append(intervals[j])
                    graph[intervals[j]].append(interval_i)#这两部才是一个完整的图连接
        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(nodes):
        min_start = min(node.start for node in nodes)
        max_end = max(node.end for node in nodes)
        return Interval(min_start, max_end)

    # gets the connected components of the interval overlap graph.
    def get_components(graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])#这才是深度优先搜索啊，“子树”上所有的interval都会作为node被访问，直到stack为空
#生成图后，是一个森林，里面有许多的子树，每一个子树都可以合并成一个大的interval，一个dfs处理一个子树
        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number#ndoes_in_comp得到的是哪些node在子图1,2,3....因为是图，所以可以从任意一个node开始遍历子图

    def merge(intervals):
        intervals=init_intervals(intervals)
        graph = build_graph(intervals)
        nodes_in_comp, number_of_comps = get_components(graph, intervals)
        # all intervals in each connected component must be merged.
        return [[item.start,item.end] for item in [merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]]

        #return [merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]
        #如果是这样的话，结果是[<__main__.Interval object at 0x000001A0F6E78320>,
        #  <__main__.Interval object at 0x000001A0F6E78908>, <__main__.Interval object at 0x0000
    return merge(intervals)

def sort_value_insert(intervals):
    def init_intervals(intervals):
        intervals=[Interval(s[0],s[1]) for s in intervals]
        return intervals
    intervals=init_intervals(intervals)
    intervals.sort(key=lambda x: x.start)#
    """这个是蛮有意思的。必须要记下来"""
    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1].end = max(merged[-1].end, interval.end)
    return [[itme.start,itme.end] for itme in merged]
intervals=[[1,5]]

print(Interval(6,8).start)
print(graph_solve(intervals))
print(sort_value_insert(intervals))