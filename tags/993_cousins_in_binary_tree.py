def f(root,x,y):
    dct={x:[0,None],y:[0,None]}
    values=[x,y]
    if not root or (not root.left and not root.right) or root.val in [x,y]:
        return False
    def reverse(node,depth,parent):
        if not node:
            return
        if node.val in values:
            dct[node.val][0]=depth
            dct[node.val][1]=parent
            values.remove(node.val)
        else:
            reverse(node.left,depth+1,node)
            reverse(node.right,depth+1,node)
    reverse(root,0,None)
    if dct[x][0]==dct[y][0] and dct[x][1]!=dct[y][1]:
        return True
    else:
        return False
from binary_tree import stringToTreeNode
root=stringToTreeNode([1,2,3,None,4,None,5])
print(f(root,4,5))
