from binary_tree import binary_tree
from binary_tree import preorder_not_recurse
from binary_tree import inorder_not_recurse
from binary_tree import postorder_not_recurse


def reconsruct_binary_according_pre_in(preorder, inorder):
    """这里面preorder是表示的先序序列，inorder表示的是中序序列
    一般来说，和树有关的题目大部分都可以使用递归
    """

    def create_binary(left, right, pre_index):
        """这里的参数分别是，中序序列的左边，右边，和root节点在先序序列中的位置，这里没必要加上root在中序序列中的位置
        因为知道了pre_index就能知道了in_index。通过inorder.index(preorder[pre_index])可以得到，如果把in_index作为参数，那么
        在递归的时候，preorder[pre_index+1]可能会out of list index。所以直接用在先序列表中的索引，在函数开始之前判断，
        就解决这个问题啦"""
        if left > right or pre_index >= len(preorder) or pre_index < 0:
            return
        """这里是很重要的，因为树中不满足的话说明都是遇到了空节点，只要返回就好啦"""
        if left == right:
            return binary_tree(preorder[pre_index])#叶子节点
        else:
            root = binary_tree(preorder[pre_index])
            root.left = create_binary(left, inorder.index(preorder[pre_index]) - 1, pre_index + 1)
            """左子树中，root节点在先序中的索引是pre_index+1"""
            root.right = create_binary(inorder.index(preorder[pre_index]) + 1, right,
                                       pre_index + inorder.index(preorder[pre_index]) - left + 1)
            """右子树中，root节点在先序中的索引是什么？对于中序中的left到right之间的排列，是左子树，根节点，右子树
            所以在先序中，root节点的索引应该是pre_index(原来的)+inorder.index(preorder[pre_index]) - left...这个是左子树的节点
             个数+ 1得到右子树的节点在先序中的索引
             注意一下，如果不匹配的话，是无法index的。那么如果考虑这种情况的实例的话，需要在外面判断一下"""
            return root#一定要加上这个return，要不然无法返回，千万不要忘记了

    root = create_binary(0, len(nums1) - 1, 0)
    return root


def reconstruct_binary_tree_according_post_in(postorder, inorder):
    """postorder是后续，inorder是中序，后续的最后一个节点是root，左子树，右子树，root"""
    if not (inorder and postorder): return None
    def create_binary(left, right, post_index):
        if left > right or post_index >= len(postorder) or post_index < 0:
            return
        if left == right:
            return binary_tree(postorder[post_index])
        else:
            root = binary_tree(postorder[post_index])
            root.left = create_binary(left, inorder.index(postorder[post_index]) - 1,
                                      post_index - (right-inorder.index(postorder[post_index]) + 1))
            """post_index减去右子树的个数，得到左子树节点的索引信息"""
            root.right = create_binary(inorder.index(postorder[post_index]) + 1, right, post_index - 1)
            return root

    root = create_binary(0, len(postorder) - 1, len(postorder) - 1)
    return root


nums1 = [1, 2, 4, 7, 5, 8, 3, 6, 9]
nums2 = [7, 4, 2, 8, 5, 1, 6, 9, 3]
nums3 = [7, 4, 8, 5, 2, 9, 6, 3, 1]
root = reconsruct_binary_according_pre_in(nums1, nums2)
innums = inorder_not_recurse(root)
print(innums)
prenums = preorder_not_recurse(root)
print(prenums)

root = reconstruct_binary_tree_according_post_in(nums3, nums2)
innums = inorder_not_recurse(root)
print(innums)
prenums = postorder_not_recurse(root)
print(prenums)
