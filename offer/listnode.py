class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
def create_listnode(nums):
    phead=ListNode(0)
    pointer=phead
    for x in nums:
        pointer.next=ListNode(x)
        pointer=pointer.next
    return phead

def remove_all_listnode(phead,x):
    """删除所有的x"""
    pre=phead
    while(pre.next):
        if pre.next.val==x:
            pre.next=pre.next.next
        else:
            pre=pre.next
    return phead

def remove_first_listnode(phead,x):
    """删除第一个x"""
    pre=phead
    while(pre.next):
        if pre.next.val==x:
            pre.next=pre.next.next
            break
        else:
            pre=pre.next
    return phead
def add_node_in_end(phead,x):
    """在最后增加一个元素"""
    cur=phead
    while(cur.next):
        cur=cur.next
    cur.next=ListNode(x)
    return phead
def add_node_after_nodey(phead,x,y):
    cur=phead
    exist_nodey=0
    while(cur.next):
        if cur.next.val==y:
            post=cur.next.next
            exist_nodey=1
            break
        else:
            cur=cur.next
    if exist_nodey==1:
        insert_node=ListNode(x)
        cur.next.next=insert_node
        insert_node.next=post
    return phead

def print_ListNode(phead):
    cur=phead
    nums=[]
    while(cur.next):
        nums.append(cur.next.val)
        cur=cur.next
    print(nums)
    return True

import heapq






