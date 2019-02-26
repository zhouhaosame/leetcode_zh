def sub_tree(rootA,rootB):
    #判断树B是否是A的子结构
    if not rootB:
        return True
    if not rootA:
        return False
    def identify_subtree(roota,rootb):
        """这个函数的作用是，判断rootb是否和roota相同，
        且他们的孩子结构是否都相同，就是相当于把b嵌入
        a的上面.
        注意了，这个函数的作用只是，将rootb从roota开始的地方嵌入。
        #return identify_subtree(roota.left,rootb) or identify_subtree(roota.right,rootb)
        向这样的明显是有问题的。因为这样的话，rootb就有可能分开了
        总的来说，这个函数就是一个判别函数"""
        if not rootb:
            return True
        elif not roota:
            return False
        elif roota.val==rootb.val and identify_subtree(roota.left,rootb.left) and\
            identify_subtree(roota.right,rootb.right):
            return True
        return False

    if identify_subtree(rootA,rootB):
        return True
    else:
        return sub_tree(rootA.left,rootB) or sub_tree(rootA.right,rootB)
    """这里才是很正的递归。将rootb看成一个整体。"""


#from reconstruct_binary_tree_7 import reconsruct_binary_according_pre_in
from binary_tree import stringToTreeNode
#rootA_pre=[8,8,9,2,4,7,7]
#rootA_in=[9,8,4,2,7,8,7]
"""因为中间有重复元素，所以不能用普通的先序中序的方式生成"""
#rootB_pre=[8,9,2]
#rootB_in=[9,8,2]
A=[8,8,7,9,2,None,None,None,None,4,7]
B=[8,None,7]
B=[8,8,None,None,2]
"""这里也要注意一下，因为之前创造testcase的时候，一定不要忘记加上None
比如，B=[8,7]返回的就是iNone，B=[8,None,7]返回的才是True"""
rootA=stringToTreeNode(A)
rootB=stringToTreeNode(B)
from binary_tree import print_tree_preorder_recurse
a_list=[]
b_list=[]
print_tree_preorder_recurse(rootA,a_list)
print_tree_preorder_recurse(rootB,b_list)
print(a_list)
print(b_list)
print(sub_tree(rootA,rootB))




