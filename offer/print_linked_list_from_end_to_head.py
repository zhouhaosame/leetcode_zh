import listnode
def print_linked_list_from_end_to_head(phead):
    """从尾巴到头打印链表，因为是一定要先遍历到最后的，
    所以不如把遍历的存在list中，或者直接先将列表反转，然后
    再从头到尾输出"""
    cur=phead
    nodes=[]
    while(cur.next):
        nodes.append(cur.next.val)
        cur=cur.next
    print(nodes[::-1])

    cur=phead.next
    phead.next=None
    pre=None
    while(cur):
        post=cur.next
        cur.next=pre
        pre=cur
        cur=post
    phead.next=pre
    nodes=[]
    while(phead.next):
        nodes.append(phead.next.val)
        phead=phead.next
    print(nodes)
def using_recur(phead):#使用递归的方法
    if phead.next==None:
        return
    if phead.next.next==None:
        print(phead.next.val)
    else:
        using_recur(phead.next)
        print(phead.next.val)
    #没有改变链表结构
if __name__=="__main__":
    #nums=[]
    #nums=[1]
    nums=[1,2,3]
    #都对了
    phead=listnode.ListNode(-1)
    print(id(phead))
    cur=phead
    for x in nums:
        cur.next=listnode.ListNode(x)
        cur=cur.next
    phead1=listnode.ListNode(-1)
    print(id(phead1))#生成了两个不同的phead节点
    print(id(phead))
    print_linked_list_from_end_to_head(phead)
    print(id(phead))
    print_linked_list_from_end_to_head(phead)
    using_recur(phead)
    #虽然地址是一样的，但是内容已经修改啦，因为phead代表的是地址啊





    
    
    