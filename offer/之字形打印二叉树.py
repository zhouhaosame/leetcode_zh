from binary_tree import stringToTreeNode
def zigzaglevelorder(root):
    if not root:
        return []
    ans = []  # 分别表示当前层还剩的节点和下一层一共需要打印的节点
    queue_1, temp_list = [root], []  # temp_list是用来临时存储某一层的所有节点的
    cur_level_rest_node, next_level_node_number, direction = 1, 0, 1  # 1表示从左往右，-1表示从右往左
    while (queue_1 or temp_list):
        if cur_level_rest_node:
            temp_node = queue_1.pop(0)
            temp_list.append(temp_node.val)
            children_node = [x for x in [temp_node.left, temp_node.right] if x]
            queue_1.extend(children_node)
            next_level_node_number += len(children_node)
            cur_level_rest_node -= 1
        elif direction == 1:
            ans.append(temp_list)
            temp_list=[]
            direction *= -1
            cur_level_rest_node = next_level_node_number
            next_level_node_number = 0
        else:
            ans.append(temp_list[::-1])
            temp_list=[]
            direction *= -1
            cur_level_rest_node = next_level_node_number
            next_level_node_number = 0
    return ans
nums=[3,9,20,None,None,15,7]
root=stringToTreeNode(nums)
print(zigzaglevelorder(root))