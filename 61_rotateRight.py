class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
def rotateRight(head,k):
    """超过99%
    本体思路
    每个都向右移动，可能移动好几个轮回
    倒数第一个右移1变成正数第一个
    倒数第二个右移2变成正数第1个
    ...
    倒数第k个右移k变成正数第一个
    所以我们要找到倒数第k个
    也就是正数第n-k+1个，因为暂时不知道（除非遍历一遍列表）
    所以用两个指针：分别指向1和k来一起向后移动，这样，当指向k的指针移动到最后一个node，指向1的指针就
    就指向倒数第k个指针，但是为了将k前面的node的next变成none，所以也要记住前面的那一个
    """
    if k == 0: return head
    if not head: return head
    a_pointer=head
    b_pointer=head
    l=0
    count=0
    while(count<k):
        a_pointer=a_pointer.next
        count+=1
        """
        这里面一共执行了k次，如果a之前指向1的话，现在a指向k+1了，移动后就变成了倒数第k+1和倒数第一个"""
        if not a_pointer:
            a_pointer=head
            l=count#
            k=k%l#
            count=0#
            """这三部非常的重要，如果不加，就是时间超时，加了的话就是超过99%，因为类似这样的情况
            【1,2,3】，400000000"""
    while(a_pointer.next):
        a_pointer=a_pointer.next
        b_pointer=b_pointer.next
    a_pointer.next = head
    k_pointer=b_pointer.next
    b_pointer.next=None
    return k_pointer

nums=[1,2,3,4,5]
from functools import reduce
head=ListNode(0)
start=head
for item in [ListNode(x) for x in nums]:
    start.next=item
    start=start.next
head=rotateRight(head.next,2)
while(head):
    print(head.val)
    head=head.next
