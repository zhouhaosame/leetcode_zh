def merge_two_sorted_linked_list(l1,l2):
    if l1 and l2:
        if l1.val<l2.val:
            head = pre = l1
            l1=l1.next
        else:
            head = pre = l2
            l2 = l2.next
        while (l2!=None and l1!=None):
            if l2.val<l1.val:
                pre.next = l2
                l2=l2.next
                pre=pre.next
            else:
                pre.next=l1
                l1=l1.next
                pre = pre.next
        if l1==None and l2!=None:
            pre.next=l2
        else:
            pre.next=l1
        return  head
    elif l1:
        return l1
    else:
        return l2
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
s1=[]
s2=[0]
head1=l1=ListNode(-1)
head2=l2=ListNode(-1)
for i in range(len(s1)):
    l1.next=ListNode(s1[i])
    l1=l1.next
for i in range(len(s2)):
    l2.next=ListNode(s2[i])
    l2=l2.next

l=merge_two_sorted_linked_list(head1.next,head2.next)
while(l!=None):
    print(l.val)
    l=l.next