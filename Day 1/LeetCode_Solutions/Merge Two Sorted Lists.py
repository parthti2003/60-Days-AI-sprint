class Solution:
    def mergeTwoLists(self, list1, list2):
        # Step 1: Convert linked lists to Python list
        values = []
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next

        # Step 2: Sort the list
        values.sort()

        # Step 3: Convert back to linked list
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
