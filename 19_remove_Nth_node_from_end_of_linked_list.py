def remove_Nth_node_from_end_of_list(head,n):
    first, tail, i = head, head, n
    while (i > 1):
        tail = tail.next
        i -= 1
        if tail == None: return None
    tail = tail.next#这里first指向的是被删除节点的前一个节点！！！！！！
    if tail == None:  # 意味着被删除的是第一个节点
        return first.next
    while (tail.next != None):
        tail = tail.next
        first = first.next
    first.next = first.next.next
    return head