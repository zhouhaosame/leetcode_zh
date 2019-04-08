# 这题和leetcode中113 path_sum II是一样的，都是find all root-to-leaf paths
from binary_tree import stringToTreeNode
def pathSum(root, sum):
    if not root:
        return []
    ans= []
    def back_tracking_find_path(res, cur_node, res_sum):
        if not cur_node:
            return
        if not cur_node.left and not cur_node.right and cur_node.val + res_sum == sum:
            ans.append(res + [cur_node])
        else:
            back_tracking_find_path(res + [cur_node], cur_node.left, res_sum + cur_node.val)
            back_tracking_find_path(res + [cur_node], cur_node.right, res_sum + cur_node.val)
    back_tracking_find_path([],root,0)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            ans[i][j]=ans[i][j].val
    return ans
nums=[5,4,8,11,None,13,4,7,2,None,None,5,1]
root=stringToTreeNode(nums)
print(pathSum(root,22))