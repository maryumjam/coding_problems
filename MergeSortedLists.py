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
    def merge_llists(self, sorted_list1, sorted_list2):
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
    def merge_list(self, sorted_list1, sorted_list2):
        i= 0
        j=0
        merge_list=[]
        while i< len(sorted_list1) and j<len(sorted_list2):
            if sorted_list1[i]<= sorted_list2[j]:
                merge_list.append(sorted_list1[i])
                i= i+1
            else:
                merge_list.append(sorted_list2[j])
                j= j+1
        merge_list.extend(sorted_list1[i:])
        merge_list.extend(sorted_list2[j:])
        return merge_list
    

if __name__=='__main__':
    solution = Solution()
    linkedlist=ListNode()
    llist1= linkedlist.build_linked_list([1,2,3,3,4,5])
    llist2= linkedlist.build_linked_list([1, 3,5,6])

    linkedlist.print_linked_list(solution.merge_llists(llist1,llist2))
    list1 = [1,2,3,3,4,5]
    list2 =[1,3,5,6]
    print(solution.merge_list(list1,list2))
    




   