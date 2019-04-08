from binary_tree import binary_tree
from binary_tree import inorder_not_recurse
def inorder_first_item(root):
    """返回中序遍历的第一个元素"""
    if not root.left:
        return root
    else:
        return inorder_first_item(root.left)
def find_next_node_in_inorder(root,node):
    if not node.right:
        if (node.parent and node.parent.left==node) or not node.parent:
            return node.parent
        else:
            while(node!=root and node.parent.right==node):
                node=node.parent
            return None if node==root else node.parent
    elif node.right:
        return inorder_first_item(root.right)
    """一共分为两种情况，如果右子树为空，若已经遍历过的node是node.parent的左节点，那么直接返回node.parent，如果不是
    叶子节点，则返回它的第一个以左孩子都很分出现的祖先节点。
    如果右子树不为空，那么就是node.right为根的树的中序遍历的第一个元素，没有检验，但是应该是对的"""

