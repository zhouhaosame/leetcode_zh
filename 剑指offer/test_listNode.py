from unittest import TestCase
import listnode
class TestListNode(TestCase):
    def test_listnode(self):
        #nums=[1,2,3,4,3,4,5]
        nums=[]
        phead=listnode.create_listnode(nums)
        listnode.print_ListNode(phead)
        phead=listnode.remove_all_listnode(phead,4)
        listnode.print_ListNode(phead)
        phead=listnode.remove_first_listnode(phead,3)
        listnode.print_ListNode(phead)
        phead=listnode.add_node_after_nodey(phead,9,1)
        listnode.print_ListNode(phead)
        phead=listnode.add_node_in_end(phead,88)
        listnode.print_ListNode(phead)

