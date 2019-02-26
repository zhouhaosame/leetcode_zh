def f():
    nums=[1,2,3]
    nums=str(nums)
    print(type(nums))#str
    nums1=list(nums)
    print(nums1)#['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
    nums=nums[1:-1]
    print(nums)#1, 2, 3
    nums=nums.split(",")
    print(nums)#['1', ' 2', ' 3']
    for x in range(len(nums)):
        nums[x]=int(nums[x])
    print(nums)#[1, 2, 3]
    print(type(nums))#<class 'list'>

from binary_tree import stringToTreeNode
from binary_tree import binary_tree
def serialize(root):
    if not root:
        return "[]"
    queue_node,ans=[root],[]
    while(queue_node):
        node=queue_node.pop(0)
        if not node:
            ans.append(None)
        else:
            queue_node.extend([children for children in [node.left,node.right]])
            ans.append(node.val)
    print(ans)
    for i in range(len(ans)-1,0,-1):
        if ans[i]!=None:
            """这里一定要使用：！=None。因为里面可能有0的存在，且在最后。要不然的话，很有可能把0删掉了"""
            break
        else:
            ans.pop()

    return "["+",".join([str(x) for x in ans])+"]"

def deserialize(data):
    data = data[1:-1]
    if not data:
        return None
    #这个是用来删除第一个和最后一个那个[]的
    data = data.split(",")
    #不要使用这种的，因为可能里面只有一个元素。那么逗号就不能这么用了!!!!
    #reject,即使是一个元素，里面还是能用,来划分的啊
    """
    if data=="[]":
        return None
    flag,data=-1,[]
    for item in data:
        if flag==1:
            data.append(item)
        flag*=-1
        这个完全是错误的啊！！！因为里面每一个都是c，比如None，12等都是好几个char。所以还是要划分
    """
    #跳着读可以得到所有的元素。
    #queue_node,index=[binary_tree(data[0])],1
    #root=queue_node[0]
    root,index=binary_tree(data[0]),1
    queue_node=[root]
    while(queue_node and index<len(data)):
        node=queue_node.pop(0)
        #这个是左孩子
        if data[index]!="None":
            node.left=binary_tree(data[index])
            queue_node.append(node.left)
        index+=1
        if index>=len(data):
            break
        if data[index]!="None":
            node.right=binary_tree(data[index])
            queue_node.append(node.right)
        index+=1
    return root

nums=[1,2,0]
root=stringToTreeNode(nums)
prenums,innums=[],[]
from binary_tree import print_tree_preorder_recurse,print_tree_inorder_recurse
print_tree_preorder_recurse(root,prenums)
print_tree_inorder_recurse(root,innums)
print(prenums)
print(innums)
data=serialize(root)
print(data)
root=deserialize(data)
prenums,innums=[],[]
print_tree_preorder_recurse(root,prenums)
print_tree_inorder_recurse(root,innums)
print(prenums)
print(innums)
