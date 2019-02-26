#这题和leetcode中的138一样
#深度拷贝一个复杂链表
class RandomListNode(object):
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None
def using_hash(head):
    if not head or not head.next:
        return head
    #使用空间换取时间的方式，创建一个hash表去保存相对位置记录，然后直接查询连接即可
    #先将原始链表的random指针的相对位置表示出来，遍历原始链表
    number_to_random_address,address_to_number={},{}
    #到此为止，number_to_random_address存的是当前节点编号对应的random节点的编号，从1开始的
    #然后生成复制的链表，一遍生成链表，一遍生成编号:address对
    clon_head,pointer=RandomListNode(head.label),head
    clon_pointer=clon_head
    clon_number_to_address,count={},1
    while(pointer.next):
        number_to_random_address.update({count:pointer.next.random})
        address_to_number.update({pointer.next:count})
        node=RandomListNode(pointer.next.label)
        clon_pointer.next=node
        clon_pointer=clon_pointer.next
        pointer=pointer.next
        clon_number_to_address.update({count:node})
        count+=1
    #这样的话，生成了一个用next相连的复制链表，而且也生成了number address的对应链表
    for key in number_to_random_address.keys():
        number_to_random_address[key]=address_to_number.setdefault(number_to_random_address[key],None)
    #这里原来是number_to_random_address[key]=address_to_number(number_to_random_address[key])。
    #会出现dict is not callable的错误
    clon_pointer,count = clon_head,1
    while(clon_pointer.next):
        clon_pointer.next.random=clon_number_to_address.setdefault(number_to_random_address[count],None)
        """这里和上面的那个for循环里面的setdefault应该是最重要且容易错的地方了，因为可能number对应的是None，也就是说
        在字典中找不到出相应的key，所以这时候就应该返回一个None
        """
        count+=1
        clon_pointer=clon_pointer.next
    return clon_head




def correct(head):
    """这个应该是最好的方法了"""
    pointer=head
    if not head or not head.next:
        return head
    while(pointer.next):
        node=RandomListNode(pointer.next.label)
        node.next=pointer.next.next
        pointer.next.next=node
        pointer=pointer.next.next
    pointer=head
    while(pointer.next):
        if not pointer.next.random:
            pointer.next.next.random=None
        else:
            pointer.next.next.random=pointer.next.random.next
        pointer=pointer.next.next
    clone_pointer=head
    while(clone_pointer.next):
        clone_pointer.next=clone_pointer.next.next
        clone_pointer=clone_pointer.next
    return head





nums=[-1,2,3,4,5]
head=RandomListNode(-1)
pointer=head
label_to_address={}
for x in nums:
    node=RandomListNode(x)
    pointer.next=node
    pointer=pointer.next
    label_to_address.update({x:node})
pointer=head
n={1:3,2:5,4:2}
count=1
while(pointer.next):
    if count in n.keys():
        pointer.next.random=label_to_address[n[count]]
    count+=1
    pointer=pointer.next
print(head)
#head=using_hash(head)
head=correct(head)
print(head)
#print
pointer=head
while(pointer.next):
    temp=[]
    if not pointer.next.random:
        temp.append([pointer.next.label,None])
    else:
        temp.append([pointer.next.label,pointer.next.random.label])
    print(temp)
    pointer=pointer.next






