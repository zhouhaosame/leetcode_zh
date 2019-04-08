
class Solution:
    def EntryNodeOfLoop(pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        fast,slow=pHead,pHead.next.next
        while(fast and slow and slow.next and fast!=slow):
            fast=fast.next
            slow=slow.next.next
        if not fast==slow:
            return None
        meet_pointer=fast
        count=1
        meet_pointer=meet_pointer.next
        while(meet_pointer!=fast):
            meet_pointer=meet_pointer.next
            count+=1
        #其中count是环中链表的长度
        head,post=pHead,pHead
        for _ in range(0,count):
            head=head.next
        while(post!=head.next):
            head=head.next
            post=post.next
        return post