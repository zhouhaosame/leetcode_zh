def f(root):
    if not root:
        return root
    stack,ans=[root],[]
    while(root.left):
        stack.append(root.left)
        root=root.left
    while(stack):
        node=stack.pop()
        ans.append(node.val)
        if node.right:
            node=node.right
            stack.append(node)
            while(node.left):
                stack.append(node.left)
                node = node.left
    return ans
from binary_tree import stringToTreeNode as bi
nums=[1,2,3,4,5,6]
root=bi(nums)
print(f(root))
from binary_tree import binary_tree
def middle_tree(Root):
    stack = []
    while(Root or stack):
        while(Root):
            stack.append(Root)
            Root = Root.left
        Root= stack.pop(0)
        print(Root.val)
        Root = Root.right
print(middle_tree(root))