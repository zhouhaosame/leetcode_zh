class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
def find_kth_node_in_linked_list(phead,k):
    if not phead or k<=0:
        return 0
    i,j=phead,phead
    for count in range(0,k):
        if i:
            i=i.next
        else:
            return False
    while(i):
        j=j.next
        i=i.next
    return j.val
nums=[1,2,3,4,5,6,7,8,9,10]
phead=ListNode(-1)
i=phead
for x in nums:
    i.next=ListNode(x)
    i=i.next
print(find_kth_node_in_linked_list(phead,3))
print(find_kth_node_in_linked_list(phead,-3))
print(find_kth_node_in_linked_list(phead,33))
print(find_kth_node_in_linked_list(phead,10))
print(find_kth_node_in_linked_list(phead,11))
print(find_kth_node_in_linked_list(phead,0))


