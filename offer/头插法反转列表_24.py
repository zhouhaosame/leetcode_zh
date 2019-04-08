def reverse_linked_list(phead):
    """其中j表示未反转列表的首节点"""
    if not phead or not phead.next or not phead.next.next:
        return phead
    i=phead.next
    j=phead.next.next
    i.next=None###头插法，一定要把已经翻转好的最后一个节点的next设置为空啊！！要不然就是死循环了
    while(j):
        phead.next=j
        j=j.next
        phead.next.next=i
        i=phead.next
    return phead
from listnode import create_listnode
from listnode import print_ListNode
nums=[1,2,3,4,5,6,7,8]
phead=create_listnode(nums)
phead1=reverse_linked_list(phead)
print_ListNode(phead1)