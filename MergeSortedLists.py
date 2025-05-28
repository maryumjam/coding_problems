class ListNode:
    def __init__(self, val=0, next= None):
        self.val= val
        self.next = next
    
    def build_linked_list(self, values):
        if not values:
            return None    
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def print_linked_list(self, head):
        while head:
            print(head.val, end=" -> " if head.next else "\n")
            head = head.next


class Solution:
    def merge_lists(self, sorted_list1, sorted_list2):
        dummy= ListNode(-1)
        current= dummy
        while sorted_list1 and sorted_list2:
            # If list 1 value is less than list2 value then current next should point to this low value and this all list should be point by next of its pointers
            if sorted_list1.val <= sorted_list2.val:
                current.next =sorted_list1
                sorted_list1 = sorted_list1.next
            #else list 2 value is less than the list 1 then current next should point to this low value
            else:
                current.next =sorted_list2
                sorted_list2 = sorted_list2.next
            current= current.next
        # Attach the remaining nodes, if any
        current.next = sorted_list1 if sorted_list1 else sorted_list2

        return dummy.next
    

if __name__=='__main__':
    solution1 = Solution()
    linkedlist=ListNode()
    list1= linkedlist.build_linked_list([1,2,3,3,4,5])
    list2= linkedlist.build_linked_list([1, 3,5,6])

    linkedlist.print_linked_list(solution1.merge_lists(list1,list2))




   