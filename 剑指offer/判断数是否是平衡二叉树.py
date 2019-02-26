def isbalance_tree(root):
    if not root:
        return True
    def reverse(node):
        if not node:
            return 0,True
        else:
            left_number,left_isbalance=reverse(node.left)
            right_number,right_isbalance=reverse(node.right)
            isbalance=left_isbalance and right_isbalance and abs(left_number-right_number)<=1
            return max(left_number,right_number)+1,isbalance
    return reverse(root)[1]

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        isbalance=[True]#表示，到目前为止，是否是平衡二叉树
        def reverse(node):
            if not node:
                return 0
            else:
                left_number=reverse(node.left)
                right_number=reverse(node.right)
                isbalance[0]=isbalance[0] and abs(left_number-right_number)<=1
                return max(left_number,right_number)+1
        reverse(root)
        return isbalance[0]


