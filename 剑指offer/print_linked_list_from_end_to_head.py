def print_linked_list_from_end_to_head(phead):
    """从尾巴到头打印链表，因为是一定要先遍历到最后的，
    所以不如把遍历的存在list中，或者直接先将列表反转，然后
    再从头到尾输出"""
    cur=phead
    nodes=[]
    while(cur.next):
    
    
    