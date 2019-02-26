"""这里是找数最左下角的值，很明显应该是先序+加上动态规划去找最长的一条路径。
这样的话还会一定程度上需要树深度大小的空间，不如就直接用num和一个tail值去比较和存储吧
反正又没有要求吧那条路也找出来"""
def find_left_bottom_value(root):
    if not root:
        return root
    value=[""]
    def search_tree(max_len,cur_len,tree_node):
        """一定要注意，这里的max_len要是list形式的，因为每一轮的改变都是需要保存的（即时刻记录着已经遍历的
        最长的路径长度），这样才能够找到最左边的。想想如果不是list而是一个数，那么例子是1,2,3。2是根节点，1是
        左节点，3是右节点的情况"""
        cur_len += 1
        if max_len[0]<cur_len:
            max_len[0]=cur_len
            value[0]=tree_node.val
        for node in [node for node in [tree_node.left,tree_node.right] if node]:
            search_tree(max_len,cur_len,node)
    search_tree([-1],0,root)
    return value[0]

def findLeftMostNode(root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val
