import numpy as np
class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None#原来空是None，不是NULL

def add_two_numbers(l1,l2):
    head_1=l1
    carry=0
    while(l1.next and l2.next):#与while(l1.next!=None and l2.next!=None):一样
        sum=l1.val+l2.val+carry
        l1.val=sum%10
        carry=sum//10
        l1=l1.next
        l2=l2.next
    sum = l1.val + l2.val + carry
    l1.val = sum % 10
    carry = sum // 10
    l1.next=l1.next if l1.next else l2.next
    while(l1.next and carry):
        l1 = l1.next
        sum=l1.val+carry
        l1.val=sum%10
        carry=sum//10
    if carry:
        l1.next=ListNode(carry)
    return head_1

nums=[[2,4,3,9,9,9,9,9],[5,6,9,9,9]]
head_0 = l = ListNode(-1)
for j in range(len(nums[0])):
    l.next=ListNode(nums[0][j])
    l=l.next
head_1 = l = ListNode(-1)
for j in range(len(nums[1])):
    l.next=ListNode(nums[1][j])
    l=l.next
list=add_two_numbers(head_0.next,head_1.next)
while(list):
    print(list.val)
    list=list.next