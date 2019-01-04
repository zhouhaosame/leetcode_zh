class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
def swapPairs(head):
    pre=ListNode(0)
    head_new,pre.next=pre,head
    if head and head.next:first,second=head,head.next
    else:return head
    while(second):
        pre.next=second
        first.next=second.next
        second.next=first
        pre=first
        if first.next:first,second=first.next,first.next.next
        else:break
    return head_new.next