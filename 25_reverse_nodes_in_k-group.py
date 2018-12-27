class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
def reverseKGroup(head,k):
    if k == 1: return head#k==1的时候就不需要反转了
    head_new=ListNode(0)
    pre=head_new
    list_finger=[None]*k
    pre.next=head
    for i in range(k):
        if head:
            list_finger[i]=head
            head=head.next
        else:return head_new.next
    while(1):#这里要想不断执行while中的，要加上(1)，不能是（）
        i = k
        pre.next=list_finger[i-1]
        list_finger[0].next=list_finger[i-1].next
        j=1
        while(j<i):
            list_finger[j].next=list_finger[j-1]
            j+=1
        pre=list_finger[0]
        list_finger[0]=pre.next
        for i in range(k-1):
            if list_finger[i] and list_finger[i].next:
                list_finger[i+1] =list_finger[i].next
            else:
                return head_new.next
x=[1,2,3,4,5]
head=ListNode(0)
finger=head
for i in x:
    finger.next=ListNode(x)
    finger=finger.next
reverseKGroup(head.next,2)