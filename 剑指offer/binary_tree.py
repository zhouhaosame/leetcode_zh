class binary_tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def create_full_binary_tree_1(nums):
    #递归生成二叉树，nums是完全二叉树的层序遍历
    if not nums:return
    L=len(nums)
    def create_tree(i):#生成以i为根节点val的树
        root = binary_tree(nums[i])#先生成根节点
        if not (2*i+1)<L and not (2*i+2)<L:#如果是叶子节点直接返回
            return root
        else:
            if (2*i+1)<L:#如果左边结点存在
                left=create_tree(2*i+1)
                root.left = left#连接左子树
            if (2*i+2)<L:#如果右边结点存在
                right=create_tree(2*i+2)
                root.right = right
            return root#返回根节点的地址
    return create_tree(0)

def print_tree_preorder_recurse(root,prenums):
    #按理说可以打印所有的树结点
    if root:
        prenums.append(root.val)
        print_tree_preorder_recurse(root.left,prenums)
        print_tree_preorder_recurse(root.right,prenums)
        #这是先序遍历
def print_tree_inorder_recurse(root,innums):
    if root:
        print_tree_inorder_recurse(root.left,innums)
        innums.append(root.val)
        print_tree_inorder_recurse(root.right,innums)
        #中序遍历

def print_tree_postorder_recurse(root,postnums):
    if root:
        print_tree_postorder_recurse(root.left,postnums)
        print_tree_postorder_recurse(root.right,postnums)
        postnums.append(root.val)
        #后序遍历

def preorder_not_recurse(root):
    if not root:return []
    stack,pcur,prenums=[],root,[]
    while(stack or pcur):#pcur==1是入口，而且当root只有右子树的时候，需要pcur保证继续执行函数（此时stack是空）
        if pcur:
            prenums.append(pcur.val)#先序就需要先访问
            stack.append(pcur)#加入栈，是为了到时候找到他的右子树
            pcur=pcur.left#先遍历左子树
        else:
            pcur=stack.pop()#得到需要遍历右子树的节点
            pcur=pcur.right#再遍历右子树
    return prenums

def inorder_not_recurse(root):
    if not root:return []
    stack,pcur,innums=[],root,[]
    while(stack or pcur):
        if pcur:
            stack.append(pcur)#先放入栈中
            pcur=pcur.left
        else:
            pcur=stack.pop()#当左子树访问完成之后，就可以访问root节点了
            innums.append(pcur.val)
            pcur=pcur.right#访问root节点之后，就将右边访问
    return innums

def postorder_not_recurse(root):
    if not root: return []
    stack,pcur,pvisited,postnums=[],root,None,[]
    while(pcur):#一直左边遍历，作为启动原料
        stack.append(pcur)
        pcur=pcur.left
    while(stack):#这里没有使用 or pcur,因为pcur的两个功能，启动和防止root只有右子树的作用。因为当stack为空的时候，说明
        #左右以及root都已经访问了，所以与pcur无关了
        if pcur:
            stack.append(pcur)
            pcur=pcur.left#一直遍历左边
        else:#说明遍历到左子树为空的节点了
            pcur=stack.pop()#这时候pop一个
            if pvisited==pcur.right or pcur.right==None:#如果pcur的右边已经遍历或者右边为空，说明可以访问pcur了。
                #注意，之前忽略了  pcur.right==None，有时候，pvisited==pcur.left 且右子树为空。
                postnums.append(pcur.val)
                pvisited=pcur
                pcur=None#这里很重要，当root被访问之后，pcur要置空，这样才能够继续从stack中pop下一个root。
            else:
                stack.append(pcur)#右子树没有访问，所以要将root再次放在stack中
                pcur=pcur.right#操作右子树
    return postnums
    #1%

def postorderTraversal(root):
    #宏观上看，后续是先访问左子树，在访问右子树，最后访问root，顺序是左，右，root
    ret, stack = [], root and [root]
    while stack:
        node = stack.pop()
        ret.append(node.val)
        stack += [child for child in (node.left, node.right) if child]#right在后面，所以会先出，先被访问
        #那么ret中是node，右，左
    return ret[::-1]#所以要逆转

def preorderTraversal(root):
    ret, stack = [], root and [root]
    while stack:
        node = stack.pop()
        ret.append(node.val)
        stack += [child for child in (node.right, node.left) if child]
    return ret
#想法同上

"""中序没有上述的性质，要使用自己的"""

def stringToTreeNode(inputValues):
    """首先说明一下，输入的都是字符数组，虽然像是完全二叉树的形式，但是它不是，只是每一个节点的左右子节点都是成对出现的,
    如果左右字数都不存在，用None代替，缺失也用None代替"""
    if not inputValues: return []
    root = binary_tree(int(inputValues[0]))
    nodeQueue = [root]
    front = 0#front是树中的节点编号
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1
        item = inputValues[index]
        index = index + 1
        """很明显，每一个树中的节点都有左右两个节点"""
        if item!=None:
            leftNumber = int(item)
            node.left = binary_tree(leftNumber)
            nodeQueue.append(node.left)
        if index >= len(inputValues):
            break
        item = inputValues[index]
        index = index + 1
        if item!=None:
            rightNumber = int(item)
            node.right = binary_tree(rightNumber)
            nodeQueue.append(node.right)
    return root

def levelorder(root):
    queue,levelnums=root and [root],[]
    while(queue):
        qcur=queue.pop(0)#删除并返回第一个元素
        levelnums.append(qcur.val)
        queue.extend([child for child in [qcur.left,qcur.right] if child])
    return levelnums
#这是普通层序遍历

def levelorder_fenceng(root):
    if not root: return []
    queue,levelnums=root and [(root,0)],[]#一定要注意一下不能为空哦
    while(queue):
        qcur=queue.pop(0)#删除并返回第一个元素
        levelnums.append((qcur[0].val,qcur[1]))
        queue.extend([(child,qcur[1]+1) for child in [qcur[0].left,qcur[0].right] if child])
    newnums=[[levelnums[0][0]]]
    for index in range(1,len(levelnums)):
        if levelnums[index][1]==levelnums[index-1][1]:
            newnums[-1].append(levelnums[index][0])
        else:
            newnums.append([levelnums[index][0]])
    return newnums
#这是按照每层返回的层序遍历，用i来表示每层的元素\
if __name__=="__main__":
    nums=[1,2,3,4,5,6,7,8,9,10]
    prenums,innums,postnums=[],[],[]
    root=create_full_binary_tree_1(nums)#层序遍历生成完全二叉树
    print_tree_preorder_recurse(root,prenums)
    print_tree_inorder_recurse(root, innums)
    print_tree_postorder_recurse(root, postnums)
    print(id(innums))
    print(id(postnums))
    print(prenums)
    print(innums)
    print(postnums)
    root=stringToTreeNode(["1","2","3",None,'4','5','6',None,None,None,None,'7','8',None,None,"9",None,None,None])
    postnums=inorder_not_recurse(root)
    print(postnums)
    print(levelorder_fenceng(root))




