class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """这题其实蛮有趣的"""
        """思路是，肯定是使用递归的。创建一个递归函数，它的参数是root树和greater_value,
        greater_value的含义是比root树大的节点的数的和，递归函数的含义是：根据greater_value和root，完成题目要求的操作
        。现在想一想，因为我的本意是从最大值开始计算的，只要在计算最大的那个时候，把greater_value加上不就好了吗？
        如果每一个节点都加上最大值的话，由于节点一直在改变，相当于多加了k*greater)_value
        """
        if not root or not root.left and not root.right:
            return root
        def reverse(root,greater_value):#greater_value的含义是比root树大的节点的数的和
            if not root:
                return#空的时候只要结束就好了，不需要返回，因为node的改变是跟随着的
            elif not root.right:#如果root的右子树为空，说明root就是最大的了啊，然后更新即可
                root.val+=greater_value
                reverse(root.left,root.val)#因为可能有左子树，所以还要递归下去，这时候的greater_value改变了
            else:
                #如果有右子树的话，先把右子树递归，因为所有树的和是在右子树中左下的（原来是最小的），所以要找到它
                reverse(root.right,greater_value)#递归右子树的时候，greater没有改变
                node=root.right
                while(node.left):
                    node=node.left                
                root.val+=node.val
                """这里是最重要的，因为我们已经将greater_value融入右子树了，所以只要加上右子树的“原最小值node”即可
                不需要加上greater_value"""
                reverse(root.left,root.val)#然后再递归左子树
        reverse(root,0)
        return root