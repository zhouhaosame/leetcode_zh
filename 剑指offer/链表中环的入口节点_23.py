def compute_len_of_circle(phead):
    slow_pointer,quick_pointer=phead.next,phead.next.next
    while(quick_pointer and quick_pointer.next and quick_pointer!=slow_pointer):
        #每次像后面跳两次，所以一定要判断quick_pointer.next是不是为空，要不然会出现错误
        slow_pointer=slow_pointer.next
        quick_pointer=quick_pointer.next.next
    if not quick_pointer or not quick_pointer.next:
        return 0
    len_circle=1
    quick_pointer=quick_pointer.next
    while(slow_pointer!=quick_pointer):
        len_circle+=1
        quick_pointer=quick_pointer.next
    return len_circle

def identify_enter(phead):
    """如果存在环的话，那么肯定是长度大于等于3的.
    这句话是错误的，因为即使只有一个节点也可以自己连自己啊！！！"""
    if not phead:
        return None
    pre_pointer,post_pointer=phead.next,phead.next
    len_circle=compute_len_of_circle(phead)
    if not len_circle:
        return None
    for i in range(0,len_circle):#因为是一个环。当都走到入口的时候停止。所以要向后面提前移动环长度个节点
        post_pointer=post_pointer.next
    while(post_pointer!=pre_pointer):
        post_pointer=post_pointer.next
        pre_pointer=pre_pointer.next
    return post_pointer.val

class Solution:
    def EntryNodeOfLoop(self,pHead):
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
        for _ in range(0,count-1):
            head=head.next
        while(post!=head.next):
            head=head.next
            post=post.next
        return post.val

from listnode import create_listnode
nums=[1,2,3,4,5,6,7,8,9]
pos=3
phead=create_listnode(nums)
i=phead
for count in range(0,pos):
    i=i.next
j=phead
while(j.next):
    j=j.next
j.next=i
i=phead.next
for _ in range(0,22):
   print(i.val)
   i=i.next
test=Solution()
print(test.EntryNodeOfLoop(phead.next))
#print(identify_enter(phead))
"""测试过了，边界结果都是对的"""


