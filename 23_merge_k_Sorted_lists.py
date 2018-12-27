def merge_k_sorted_linked_lists(lists):
    from functools import reduce
    def merge_two_sorted_linked_list(l1, l2):
        if l1 and l2:
            if l1.val < l2.val:
                head = pre = l1
                l1 = l1.next
            else:
                head = pre = l2
                l2 = l2.next
            while (l2 != None and l1 != None):
                if l2.val < l1.val:
                    pre.next = l2
                    l2 = l2.next
                    pre = pre.next
                else:
                    pre.next = l1
                    l1 = l1.next
                    pre = pre.next
            if l1 == None and l2 != None:
                pre.next = l2
            else:
                pre.next = l1
            return head
        elif l1:
            return l1
        else:
            return l2
    return reduce(merge_two_sorted_linked_list,lists,[])
    #最好赋一个初值，要不然输入时空的话，可能会出现问题

"""自己写的超时了，别人的faster 50%"""

def merge_divide_and_conquer(lists):
    def merge2Lists(l1, l2):
        head = point = ListNode(0)#point代替了pre,并且，直接生成了头结点
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next#也就是说point永远是在l1指针的前面
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            #即使amount=2,i还是能够取到0.应该说是先取0，然后内部，然后+2，与amount-interval比较
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists

def similar_two_sorted_lists(lists):
    if len(lists)==1:return lists[0]
    def min_node(nodes):
        #要确保nodes都不为空
        min=nodes[0].val
        min_node=nodes[0]
        index=0
        for i in range(len(nodes)):
            if min>nodes[i].val:
                min=nodes[i].val
                min_node=nodes[i]
                index=i
        return min_node,index
    def del_empty_node(lists):
        lists_temp=[]
        for i in lists:
            if i!=None:
                lists_temp.append(i)
        return lists_temp
    lists=del_empty_node(lists)
    if lists:
        pre,index_min=min_node(lists)
        node1=lists[index_min]
        lists[index_min]=node1.next
        head=pre
        while(lists):
            lists=del_empty_node(lists)
            if len(lists)==1:
                pre.next=lists[0]
                return head
            find_node,index_min=min_node(lists)
            pre.next=find_node
            pre=pre.next
            lists[index_min] = lists[index_min].next
        return head
    else:return []

#别人的优化之后的方法

import queue
def mergeKLists(lists):
    head = point = ListNode(0)
    q =queue.PriorityQueue()
    for l in lists:
        if l:
            q.put((l.val, l))
    while not q.empty():
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))
    return head.next
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
def brute_force(lists):
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    for x in sorted(nodes):
        point.next = ListNode(x)
        point = point.next
    return head.next
#这种暴力法反而比我之前的两种方法都要快，这说明我的方法有待精简

s1=[1]
s2=[1]
s3=[2]
head1=l1=ListNode(-1)
head2=l2=ListNode(-1)
head3=l3=ListNode(-1)
for i in range(len(s1)):
    l1.next=ListNode(s1[i])
    l1=l1.next
for i in range(len(s2)):
    l2.next=ListNode(s2[i])
    l2=l2.next
for i in range(len(s3)):
    l3.next=ListNode(s3[i])
    l3=l3.next
lists=[head1.next,head2.next,head3.next]
#l=merge_k_sorted_linked_lists(lists)
"""之前这里没有注释掉，因为lists是全局变量，所以当然改变啦，导致结果出错"""
#l=similar_two_sorted_lists(lists)
l=mergeKLists(lists)
while(l!=None):
    print(l.val)
    l=l.next