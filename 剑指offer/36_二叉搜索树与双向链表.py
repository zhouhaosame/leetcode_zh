"""
def Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked_List(root):
    很明显，这个需要将树的指针都重新改变，正好左右子树就是双向指针啊
    if not root:
        return root
    def reverse(node):
        if node:
            if not node.left and not node.right:
                return node,node
            else:
                left_start,left_end=reverse(node.left)
                right_start,right_end=reverse(node.right)
                left_end.right=node
                node.left=left_end
                node.right=right_start
                right_start.left=node
                return left_start,right_end
    start,end=reverse(root)
    return start,end
这种解法明显是错误的，没有考虑只有一个孩子为空的情况
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def Convert(pRootOfTree):
    # write code here
    if not pRootOfTree:
        return pRootOfTree
    def contact(node):
        if not node or (not node.left and not node.right):
            return node,node
        else:
            left_head,left_tail=contact(node.left)
            right_head,right_tail=contact(node.right)
            if not left_head:
                node.right=right_head
                right_head.left=node
                node.left=None#一定要加上这一行啊，因为不加上的话，node的左边或者右边仍然指向一些东西，可能导致死循环
                return node,right_tail
            if not right_head:
                left_tail.right=node
                node.left=left_tail
                node.right=None#############
                return left_head,node
            #因为最前面已经考虑了左右孩子都为空的情况，所以上述两个if只有一个会执行
            left_tail.right=node
            node.left=left_tail
            node.right=right_head
            right_head.left=node
            return left_head,right_tail
    return contact(pRootOfTree)
from binary_tree import stringToTreeNode
nums=[10,6,14,4,8,12,16]
root=stringToTreeNode(nums)
head,tail=Convert(root)
while(head):
    print(head.val)
    head=head.right
while(tail):
    print(tail.val)
    tail=tail.left

